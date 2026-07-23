"""Transport-network atlas for the November-1983 theater.

Standalone from wargame/ by design — see atlas/README.md, "Seams".
Pure stdlib (tomllib, heapq); the graph is small enough that
hand-rolled Dijkstra and Edmonds-Karp beat a dependency.
"""

from __future__ import annotations

import heapq
from collections import deque
from dataclasses import dataclass
from pathlib import Path

import tomllib

DATA_PATH = Path(__file__).parent / "data" / "theater-1983.toml"

# Planning abstractions, km/h. GUESS-tier throughout (README,
# "Data discipline"): convoy speeds are column-march planning
# figures, not measured; graduate them like any other number.
SPEEDS = {
    "civil": {"motorway": 90, "trunk": 70, "federal": 60, "secondary": 45, "rail": 70},
    "convoy": {"motorway": 40, "trunk": 30, "federal": 25, "secondary": 20, "rail": 40},
}

# Default one-way capacities, tonnes/day (≈ STON), by road class
# or rail. Road classes anchored to FM 101-10-1 Vol 2 Table 3-7
# (manual p. 3-7), "Daily Tonnage Forward", COMMZ supply-traffic
# column: concrete 36,000 / bituminous 27,000 / bituminous-treated
# 18,000, narrow-roadway −25%. Combat-zone column is ~4-8x lower —
# wartime degradation is scenario logic, not the edge's physical
# capacity. Rail: FM net trainload 500 STON (para 3-26, p. 3-41,
# "conservative") × ~40 trains/day double track (density is NOT in
# the FM — grade-C rule of thumb; single-track edges carry ~20
# trains/day as explicit cap_tpd). See reference/transport-1983.md
# §3-4 and the round-1 provenance there.
CAP_DEFAULTS_TPD = {
    "motorway": 36_000,
    "trunk": 27_000,
    "federal": 20_000,
    "secondary": 10_000,
    "rail": 20_000,
}


@dataclass(frozen=True)
class Node:
    id: str
    name: str
    region: str
    lat: float
    lon: float
    notes: str = ""


@dataclass(frozen=True)
class Edge:
    id: str
    a: str
    b: str
    mode: str  # "road" | "rail" | "ferry"
    cls: str  # road class; "rail"; "ferry"
    km: float
    route: str = ""  # 1983 designation: "E3", "A7", "B76"...
    via: str = ""  # structure + open date provenance
    crossing: str = ""  # water/border tag: kiel_canal, igb, ...
    hours: float | None = None  # explicit traversal (ferries)
    fixed_hours: float = 0.0  # loading/marshalling overhead
    cap_tpd: float | None = None
    cap_source: str = "DEFAULT"  # GUESS | DEFAULT | SOURCED:<ref>
    verify: bool = False
    notes: str = ""

    def capacity(self) -> float:
        if self.cap_tpd is not None:
            return self.cap_tpd
        return CAP_DEFAULTS_TPD[self.cls]

    def time_hours(self, profile: str) -> float:
        if self.hours is not None:
            return self.hours + self.fixed_hours
        speed = SPEEDS[profile][self.cls]
        return self.km / speed + self.fixed_hours


class Atlas:
    def __init__(
        self,
        nodes: dict[str, Node],
        edges: list[Edge],
        absences: list[dict],
        flows: list[dict] | None = None,
    ):
        self.nodes = nodes
        self.edges = edges
        self.absences = absences
        self.flows = flows or []
        self.by_id = {e.id: e for e in edges}
        self.adj: dict[str, list[Edge]] = {n: [] for n in nodes}
        for e in edges:
            self.adj[e.a].append(e)
            self.adj[e.b].append(e)

    # -- loading ---------------------------------------------------

    @classmethod
    def load(cls, path: Path = DATA_PATH) -> "Atlas":
        raw = tomllib.loads(Path(path).read_text())
        nodes = {}
        for n in raw.get("node", []):
            node = Node(
                id=n["id"],
                name=n.get("name", n["id"]),
                region=n["region"],
                lat=n["lat"],
                lon=n["lon"],
                notes=n.get("notes", ""),
            )
            if node.id in nodes:
                raise ValueError(f"duplicate node {node.id}")
            nodes[node.id] = node
        edges = []
        seen = set()
        for e in raw.get("edge", []):
            edge = Edge(
                id=e["id"],
                a=e["a"],
                b=e["b"],
                mode=e["mode"],
                cls=e["class"],
                km=e["km"],
                route=e.get("route", ""),
                via=e.get("via", ""),
                crossing=e.get("crossing", ""),
                hours=e.get("hours"),
                fixed_hours=e.get("fixed_hours", 0.0),
                cap_tpd=e.get("cap_tpd"),
                cap_source=e.get("cap_source", "DEFAULT"),
                verify=e.get("verify", False),
                notes=e.get("notes", ""),
            )
            if edge.id in seen:
                raise ValueError(f"duplicate edge {edge.id}")
            seen.add(edge.id)
            for end in (edge.a, edge.b):
                if end not in nodes:
                    raise ValueError(f"edge {edge.id}: unknown node {end}")
            edges.append(edge)
        return cls(nodes, edges, raw.get("absence", []), raw.get("flow", []))

    # -- name/group resolution ------------------------------------

    def resolve(self, spec: str) -> list[str]:
        """A node id, or 'region:XX' for every node in a region."""
        if spec.startswith("region:"):
            reg = spec.split(":", 1)[1].upper()
            ids = [n.id for n in self.nodes.values() if n.region == reg]
            if not ids:
                raise KeyError(f"no nodes in region {reg}")
            return ids
        if spec not in self.nodes:
            raise KeyError(f"unknown node {spec}")
        return [spec]

    # -- shortest path (Dijkstra over the multigraph) --------------

    def shortest_path(
        self,
        src: str,
        dst: str,
        profile: str = "convoy",
        metric: str = "hours",
        without: set[str] = frozenset(),
        modes: set[str] | None = None,
    ):
        def cost(e: Edge) -> float:
            return e.km if metric == "km" else e.time_hours(profile)

        dist = {src: 0.0}
        prev: dict[str, Edge] = {}
        pq = [(0.0, src)]
        done = set()
        while pq:
            d, u = heapq.heappop(pq)
            if u in done:
                continue
            if u == dst:
                break
            done.add(u)
            for e in self.adj[u]:
                if e.id in without or (modes and e.mode not in modes):
                    continue
                v = e.b if e.a == u else e.a
                nd = d + cost(e)
                if nd < dist.get(v, float("inf")):
                    dist[v] = nd
                    prev[v] = e
                    heapq.heappush(pq, (nd, v))
        if dst not in dist:
            return None
        path, node = [], dst
        while node != src:
            e = prev[node]
            path.append(e)
            node = e.a if e.b == node else e.b
        path.reverse()
        return dist[dst], path

    # -- max flow / min cut (Edmonds-Karp) -------------------------

    def max_flow(
        self,
        sources: list[str],
        sinks: list[str],
        without: set[str] = frozenset(),
        modes: set[str] | None = None,
    ):
        """Returns (flow_tpd, min_cut_edges). Undirected edges get
        capacity in both directions (one-way throughput each way)."""
        SRC, SNK = "__src__", "__snk__"
        cap: dict[tuple[str, str], float] = {}
        # parallel edges merge additively at the arc level; the cut
        # is recovered edge-by-edge afterward.
        for e in self.edges:
            if e.id in without or (modes and e.mode not in modes):
                continue
            c = e.capacity()
            cap[(e.a, e.b)] = cap.get((e.a, e.b), 0.0) + c
            cap[(e.b, e.a)] = cap.get((e.b, e.a), 0.0) + c
        big = 10 * sum(e.capacity() for e in self.edges) + 1
        for s in sources:
            cap[(SRC, s)] = big
        for t in sinks:
            cap[(t, SNK)] = big
        flow: dict[tuple[str, str], float] = {}
        neighbors: dict[str, set[str]] = {}
        for u, v in cap:
            neighbors.setdefault(u, set()).add(v)
            neighbors.setdefault(v, set()).add(u)

        def residual(u, v):
            return cap.get((u, v), 0.0) - flow.get((u, v), 0.0)

        total = 0.0
        while True:
            parent = {SRC: None}
            q = deque([SRC])
            while q and SNK not in parent:
                u = q.popleft()
                for v in neighbors.get(u, ()):
                    if v not in parent and residual(u, v) > 1e-9:
                        parent[v] = u
                        q.append(v)
            if SNK not in parent:
                break
            # bottleneck along the path
            path, v = [], SNK
            while parent[v] is not None:
                path.append((parent[v], v))
                v = parent[v]
            aug = min(residual(u, w) for u, w in path)
            for u, w in path:
                flow[(u, w)] = flow.get((u, w), 0.0) + aug
                flow[(w, u)] = flow.get((w, u), 0.0) - aug
            total += aug
        # min cut: edges from the residual-reachable set outward
        reach = {SRC}
        q = deque([SRC])
        while q:
            u = q.popleft()
            for v in neighbors.get(u, ()):
                if v not in reach and residual(u, v) > 1e-9:
                    reach.add(v)
                    q.append(v)
        cut = []
        for e in self.edges:
            if e.id in without or (modes and e.mode not in modes):
                continue
            if (e.a in reach) != (e.b in reach):
                cut.append(e)
        return total, cut

    # -- criticality: knockout loss across the named story flows ---

    def critical(self):
        """For each edge, total max-flow loss (t/d) across the
        dataset's [[flow]] entries when that edge is removed.
        Returns [(loss, edge)] sorted descending, plus baselines."""

        def endpoints(specs):
            out = []
            for s in specs:
                out.extend(self.resolve(s))
            return out

        base = {}
        for f in self.flows:
            src, snk = endpoints(f["sources"]), endpoints(f["sinks"])
            base[f["id"]] = (self.max_flow(src, snk)[0], src, snk)
        ranked = []
        for e in self.edges:
            loss = 0.0
            for fid, (b, src, snk) in base.items():
                loss += b - self.max_flow(src, snk, without={e.id})[0]
            if loss > 0:
                ranked.append((loss, e))
        ranked.sort(key=lambda x: (-x[0], x[1].id))
        return ranked, {fid: b for fid, (b, _, _) in base.items()}

    # -- dataset lint ---------------------------------------------

    def check(self) -> tuple[list[str], dict]:
        issues = []
        # connectivity from an arbitrary node
        start = next(iter(self.nodes))
        seen = {start}
        q = deque([start])
        while q:
            u = q.popleft()
            for e in self.adj[u]:
                v = e.b if e.a == u else e.a
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        for n in self.nodes:
            if n not in seen:
                issues.append(f"node {n} unreachable from {start}")
        for e in self.edges:
            if e.mode == "ferry" and e.hours is None:
                issues.append(f"ferry {e.id} missing explicit hours")
            if e.mode == "ferry" and e.cap_tpd is None:
                issues.append(f"ferry {e.id} missing explicit cap_tpd")
            if e.km <= 0:
                issues.append(f"edge {e.id} nonpositive km")
        # absences: no non-ferry edge may connect a forbidden pair
        # (beyond any explicitly allowed grandfathered edges)
        for a in self.absences:
            x, y = a["would_connect"]
            allowed = set(a.get("allowed", []))
            for e in self.edges:
                if {e.a, e.b} == {x, y} and e.mode != "ferry" and e.id not in allowed:
                    issues.append(
                        f"ABSENCE VIOLATED: {e.id} fixed-links {x}-{y} ({a['name']})"
                    )
        guessy = [
            e for e in self.edges if e.cap_source in ("GUESS", "DEFAULT") or e.verify
        ]
        stats = {
            "nodes": len(self.nodes),
            "edges": len(self.edges),
            "verify_flagged": sum(1 for e in self.edges if e.verify),
            "cap_guess_or_default": sum(
                1 for e in self.edges if e.cap_source in ("GUESS", "DEFAULT")
            ),
            "unverified_share": round(len(guessy) / len(self.edges), 2)
            if self.edges
            else 0.0,
        }
        return issues, stats
