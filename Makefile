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
PDF_OPTS = $(PANDOC_OPTS) --pdf-engine=xelatex \
           --top-level-division=chapter \
           -V documentclass=book -V classoption=oneside \
           -V geometry:paperwidth=5.5in -V geometry:paperheight=8.5in \
           -V geometry:margin=0.75in -V fontsize=11pt \
           -V mainfont="$(BODYFACE)" \
           --include-in-header=apparatus/latex-header.tex

# Map plates (apparatus). data + PD base -> SVG (atlas render) -> vector
# PDF (scripts/svg2pdf.py, headless Chromium). Regenerated into
# build/maps/ and injected by apparatus/front-matter.md.
MAP_DIR = build/maps
PLATES = approaches neck
METADATA = --metadata title="$(TITLE)" \
           --metadata author="Daniel Klein" \
           --metadata date="$(DRAFT_STAMP)"

.PHONY: archive transcripts transcripts-founding raw-archive shelf hooks test demo atlas maps pdf manuscript wordcount clean

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

# Reading PDF: drafts/ in filename order (01..19, 19a, 20). Depends on
# maps so the front-matter plates are always present and current.
pdf: $(OUTPUT_DIR) maps
	@pandoc $(FRONT_MATTER) $(SOURCES) $(PDF_OPTS) $(METADATA) -o $(OUTPUT_DIR)/the-mission.pdf
	@pdfinfo $(OUTPUT_DIR)/the-mission.pdf 2>/dev/null | grep Pages || true
	@echo "Created $(OUTPUT_DIR)/the-mission.pdf"

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
