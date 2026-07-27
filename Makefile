# The Mission (1986) - Step-0 targets
#
# The manuscript build targets arrive with Phase 1 (see white-buffalo's
# Makefile for the shape they will take). What exists now is the
# provenance machinery from planning/attribution.md.
#
#   make archive SKIP=<live-session-uuid>
#              - The standing hygiene target: export transcripts and
#                gzip every wrapped session's JSONL into transcripts/raw/
#                (idempotent; never overwrites an existing archive;
#                SKIP excludes the live session, whose transcript would
#                be partial). Sessions run this themselves under DK's
#                standing authorization (2026-07-20; attribution.md,
#                refinement 1).
#   make transcripts           - Markdown exports only
#   make transcripts-founding  - One-time: export + raw-archive the
#                                founding session (656ec2ba, stranded
#                                in -home-dlk-workspace)
#   make raw-archive SESSION=<uuid>  - Raw-archive a single session

FOUNDING_ID = 656ec2ba-b295-4e5d-8712-5e270300dcde
FOUNDING_DIR = $(HOME)/.claude/projects/-home-dlk-workspace
OWN_DIR = $(HOME)/.claude/projects/-home-dlk-workspace-the-mission-1986

# --- Manuscript build (reading apparatus; the production assembly
# --- arrives later, WB assemble.py-style, when there is art/apparatus
# --- to inject)
TITLE = The Baltic Approaches
OUTPUT_DIR = build
DRAFT_DIR = drafts
SOURCES = $(sort $(wildcard $(DRAFT_DIR)/*.md))
# Front matter: apparatus, not narrative — in the PDF, never in wordcount
FRONT_MATTER = $(wildcard apparatus/front-matter.md)
DRAFT_STAMP = Draft three · $(shell date +%Y-%m-%d) · $(shell git rev-parse --short HEAD)

# Body face — the SINGLE source of truth for the book's face. Both the
# PDF build (mainfont) and the map plates (`make maps`, label face)
# read it here, so changing this one value re-letters the maps to match
# (map-spec.md §5).
BODYFACE = TeX Gyre Pagella

PANDOC_OPTS = --from=markdown --standalone
# Shared composition (both PDF targets). Chapter numbering is
# LaTeX's (--number-sections + the chapters.lua H1 strip →
# two-deck heads); secnumdepth=0 numbers chapters only.
PDF_COMMON = $(PANDOC_OPTS) --pdf-engine=xelatex \
           --top-level-division=chapter \
           --number-sections -V secnumdepth=0 \
           -V documentclass=book \
           -V geometry:paperwidth=5.5in -V geometry:paperheight=8.5in \
           -V fontsize=11pt -V indent=true \
           -V mainfont="$(BODYFACE)" \
           --lua-filter=apparatus/scenebreak.lua \
           --lua-filter=apparatus/chapters.lua \
           --include-in-header=$(OUTPUT_DIR)/draftstamp.tex \
           --include-in-header=apparatus/latex-header.tex
# Canonical trade interior: two-sided mirrored margins with
# binding gutter (WB values; 4.0in measure preserved), openright
# chapter openings (book-class default once oneside is dropped —
# deliberate divergence from WB, planning/assembly.md fork 2).
PDF_OPTS = $(PDF_COMMON) \
           -V geometry:inner=0.85in -V geometry:outer=0.65in \
           -V geometry:top=0.8in -V geometry:bottom=0.9in \
           -V geometry:headsep=0.18in
# Screen affordance: one-sided, uniform margins, no blank versos.
SCREEN_OPTS = $(PDF_COMMON) \
           -V classoption=oneside -V classoption=openany \
           -V geometry:margin=0.75in

# Map plates (apparatus). data + PD base -> SVG (atlas render) -> vector
# PDF (scripts/svg2pdf.py, headless Chromium). Regenerated into
# build/maps/ and injected by apparatus/front-matter.md.
MAP_DIR = build/maps
PLATES = approaches neck
# PDF catalog metadata only — title/author as *-meta so pandoc's
# template emits no \maketitle (the designed title page lives in
# apparatus/front-matter.md; design review fork 1). The draft
# stamp prints on the notices page via \draftstamp
# (build/draftstamp.tex, generated below).
METADATA = -V title-meta="$(TITLE)" \
           -V author-meta="Daniel Klein with Claude"
BACK_MATTER = apparatus/back-matter.md

.PHONY: archive transcripts transcripts-founding raw-archive shelf hooks test demo atlas maps stamp pdf pdf-screen proof manuscript wordcount clean

$(OUTPUT_DIR):
	@mkdir -p $(OUTPUT_DIR)

# Map plates: data -> SVG -> vector PDF. Regenerable from a clean
# checkout (needs headless Chromium for SVG->PDF; see scripts/svg2pdf.py).
maps: $(OUTPUT_DIR)
	@mkdir -p $(MAP_DIR)
	@for p in $(PLATES); do \
		python3 -m atlas render $$p --face "$(BODYFACE)" --out $(MAP_DIR)/plate-$$p.svg; \
		python3 scripts/svg2pdf.py $(MAP_DIR)/plate-$$p.svg $(MAP_DIR)/plate-$$p.pdf; \
	done
	@echo "Plates in $(MAP_DIR)/ (plate-approaches.pdf, plate-neck.pdf)"

# Draft stamp as a LaTeX macro for the notices page
stamp: $(OUTPUT_DIR)
	@printf '\\newcommand{\\draftstamp}{%s}\n' "$(DRAFT_STAMP)" > $(OUTPUT_DIR)/draftstamp.tex

# Canonical trade interior: drafts/ in filename order (01..22).
# Depends on maps so the front-matter plates are always current.
pdf: $(OUTPUT_DIR) maps stamp
	@pandoc $(FRONT_MATTER) $(SOURCES) $(BACK_MATTER) $(PDF_OPTS) $(METADATA) -o $(OUTPUT_DIR)/the-mission.pdf
	@pdfinfo $(OUTPUT_DIR)/the-mission.pdf 2>/dev/null | grep Pages || true
	@echo "Created $(OUTPUT_DIR)/the-mission.pdf (trade interior)"

# Screen-reading affordance (same content, one-sided)
pdf-screen: $(OUTPUT_DIR) maps stamp
	@pandoc $(FRONT_MATTER) $(SOURCES) $(BACK_MATTER) $(SCREEN_OPTS) $(METADATA) -o $(OUTPUT_DIR)/the-mission-screen.pdf
	@pdfinfo $(OUTPUT_DIR)/the-mission-screen.pdf 2>/dev/null | grep Pages || true
	@echo "Created $(OUTPUT_DIR)/the-mission-screen.pdf (screen)"

# Page-render proof loop (WB practice): thumbnails for eyeballing
# breaks, asterisms, caps blocks. Renders the trade build.
proof: pdf
	@mkdir -p $(OUTPUT_DIR)/proof
	@rm -f $(OUTPUT_DIR)/proof/*.png
	@pdftoppm -r 60 -png $(OUTPUT_DIR)/the-mission.pdf $(OUTPUT_DIR)/proof/p
	@echo "Proof renders in $(OUTPUT_DIR)/proof/"

manuscript: $(OUTPUT_DIR)
	@pandoc $(SOURCES) $(PANDOC_OPTS) $(METADATA) -o $(OUTPUT_DIR)/the-mission.md
	@echo "Created $(OUTPUT_DIR)/the-mission.md"

# Narrative-only count (DK ruling 2026-07-23: apparatus excluded)
wordcount:
	@wc -w $(SOURCES)
	@wc -w $(SOURCES) | tail -1 | awk '{printf "Narrative total: %s words (plan 50.5k, ceiling 54.2k)\n", $$1}'

clean:
	@rm -rf $(OUTPUT_DIR)

# One-time per clone: install the pre-commit guard (blocks document
# binaries and flattened holdings/ paths from the public repo)
hooks:
	@ln -sf ../../scripts/pre-commit .git/hooks/pre-commit
	@ln -sf ../../scripts/commit-msg .git/hooks/commit-msg
	@echo "Installed .git/hooks/pre-commit -> scripts/pre-commit"
	@echo "Installed .git/hooks/commit-msg -> scripts/commit-msg (wordcount stamp)"

# Measured bookkeeping — never hand-state these numbers
counts:
	@python3 scripts/counts.py

tics:
	@sh scripts/tics.sh

# Wargame instrument
test:
	@python3 -m pytest tests/ -q

demo:
	@python3 -m wargame wargame/scenarios/toy-landjut.toml --days 14

# Transport atlas: dataset lint + its tests (atlas/README.md)
atlas:
	@python3 -m atlas check
	@python3 -m pytest tests/test_atlas.py -q

# Fetch the research shelf (reference/pdf/, gitignored; manifest of
# record is reference/shelf.md)
shelf:
	@python3 scripts/fetch-shelf.py

archive:
	@python3 scripts/export-transcripts.py $(if $(SKIP),--skip $(SKIP))
	@mkdir -p transcripts/raw
	@for f in $(OWN_DIR)/*.jsonl; do \
		id=$$(basename $$f .jsonl); \
		case $$id in agent-*) continue;; esac; \
		if [ -n "$(SKIP)" ]; then case $$id in $(SKIP)*) continue;; esac; fi; \
		if [ ! -f transcripts/raw/$$id.jsonl.gz ]; then \
			gzip -c $$f > transcripts/raw/$$id.jsonl.gz; \
			echo "raw-archived $$id"; \
		fi; \
	done
	@echo "Archive current. New sessions? Update the ledger's lineage log."

transcripts:
	@python3 scripts/export-transcripts.py

transcripts-founding:
	@python3 scripts/export-transcripts.py --source-dir $(FOUNDING_DIR) $(FOUNDING_ID)
	@mkdir -p transcripts/raw
	@gzip -c $(FOUNDING_DIR)/$(FOUNDING_ID).jsonl > transcripts/raw/$(FOUNDING_ID).jsonl.gz
	@echo "Archived $(FOUNDING_ID) (raw + transcript). Update the ledger's lineage log."

# Archive a single session's raw JSONL: make raw-archive SESSION=<uuid>
raw-archive:
	@test -n "$(SESSION)" || (echo "usage: make raw-archive SESSION=<uuid>" && exit 1)
	@mkdir -p transcripts/raw
	@gzip -c $(OWN_DIR)/$(SESSION).jsonl > transcripts/raw/$(SESSION).jsonl.gz
	@echo "Archived $(SESSION). Update the ledger's lineage log."
