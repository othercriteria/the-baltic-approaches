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
# Sessions' JSONLs live in a Claude project dir keyed to the checkout
# PATH. Every session through the making (and e3137278, wrapped but
# not yet raw-archived) lives under the old working-title path; after
# the post-COMPLETE local rename, new sessions land under the new one.
# The hygiene targets scan both so neither era is stranded.
OWN_DIR = $(HOME)/.claude/projects/-home-dlk-workspace-the-mission-1986
NEW_DIR = $(HOME)/.claude/projects/-home-dlk-workspace-the-baltic-approaches

# --- Manuscript build (reading apparatus; the production assembly
# --- arrives later, WB assemble.py-style, when there is art/apparatus
# --- to inject)
TITLE = The Baltic Approaches
OUTPUT_DIR = build
DRAFT_DIR = drafts
SOURCES = $(sort $(wildcard $(DRAFT_DIR)/*.md))
# Front matter: apparatus, not narrative — in the PDF, never in wordcount
FRONT_MATTER = $(wildcard apparatus/front-matter.md)
# Bumped from "Draft three" at the post-COMPLETE wrap work (DK
# directive 2026-07-28): the book is made; the stamp keeps date +
# commit as build provenance on the notices page.
DRAFT_STAMP = Final · $(shell date +%Y-%m-%d) · $(shell git rev-parse --short HEAD)

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

.PHONY: archive transcripts transcripts-founding raw-archive shelf hooks test demo atlas maps stamp pdf pdf-screen epub proof cover cover-wrap manuscript wordcount clean

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
	@pandoc $(FRONT_MATTER) $(SOURCES) $(BACK_MATTER) $(PDF_OPTS) $(METADATA) -o $(OUTPUT_DIR)/the-baltic-approaches.pdf
	@pdfinfo $(OUTPUT_DIR)/the-baltic-approaches.pdf 2>/dev/null | grep Pages || true
	@echo "Created $(OUTPUT_DIR)/the-baltic-approaches.pdf (trade interior)"

# Screen-reading affordance (same content, one-sided), bookended by
# the cover as page 1 and the wrap's back panel as the last page
# (DK directives 2026-07-27) — the one-file product view. Both are
# cropped to trim so page sizes match the interior; qpdf keeps the
# interior as primary so its metadata survives.
pdf-screen: $(OUTPUT_DIR) maps stamp cover cover-wrap
	@pandoc $(FRONT_MATTER) $(SOURCES) $(BACK_MATTER) $(SCREEN_OPTS) $(METADATA) -o $(OUTPUT_DIR)/screen-interior.pdf
	@pdfjam --quiet --trim '0.125in 0.125in 0.125in 0.125in' --clip true --papersize '{5.5in,8.5in}' \
		--outfile $(OUTPUT_DIR)/cover/cover-trim.pdf $(OUTPUT_DIR)/cover/the-baltic-approaches-cover.pdf 1
	@rt=$$(awk 'BEGIN{printf "%.4fin", 5.625+$(SPINE_IN)}'); \
	pdfjam --quiet --trim "0.125in 0.125in $$rt 0.125in" --clip true --papersize '{5.5in,8.5in}' \
		--outfile $(OUTPUT_DIR)/cover/back-trim.pdf $(OUTPUT_DIR)/cover/the-baltic-approaches-wrap.pdf 1
	@qpdf $(OUTPUT_DIR)/screen-interior.pdf \
		--pages $(OUTPUT_DIR)/cover/cover-trim.pdf 1 $(OUTPUT_DIR)/screen-interior.pdf 1-z $(OUTPUT_DIR)/cover/back-trim.pdf 1 -- \
		$(OUTPUT_DIR)/the-baltic-approaches-screen.pdf
	@pdfinfo $(OUTPUT_DIR)/the-baltic-approaches-screen.pdf 2>/dev/null | grep Pages || true
	@echo "Created $(OUTPUT_DIR)/the-baltic-approaches-screen.pdf (screen, cover p.1 + back panel last)"

# eBook edition (planning/ebook-brief.md). Same sources, parallel
# apparatus: epub-front-matter/epub-back-matter (imprint + colophon
# wording pending DK ratification, marked in the brief), epub-chapters
# filter (two-deck heads, asterism, message divs via CSS), epub.css.
# Plates render to PNG via rsvg; the eBook cover is the ratified front
# panel trimmed and rasterized. Print targets untouched.
EPUB_DIR = $(OUTPUT_DIR)/epub
epub: $(OUTPUT_DIR) cover
	@mkdir -p $(EPUB_DIR)
	@for p in $(PLATES); do \
		python3 -m atlas render $$p --face "$(BODYFACE)" --out $(EPUB_DIR)/plate-$$p.svg; \
		rsvg-convert --width=2000 --keep-aspect-ratio --background-color=white \
			--output $(EPUB_DIR)/plate-$$p.png $(EPUB_DIR)/plate-$$p.svg; \
	done
	@pdfjam --quiet --trim '0.125in 0.125in 0.125in 0.125in' --clip true \
		--papersize '{5.5in,8.5in}' \
		--outfile $(EPUB_DIR)/cover-ebook-trim.pdf \
		$(OUTPUT_DIR)/cover/the-baltic-approaches-cover.pdf 1
	@pdftoppm -r 300 -jpeg -jpegopt quality=90 -singlefile \
		$(EPUB_DIR)/cover-ebook-trim.pdf $(EPUB_DIR)/cover-ebook
	@sed "s|@DRAFTSTAMP@|$(DRAFT_STAMP)|" apparatus/epub-front-matter.md > $(EPUB_DIR)/front-matter.md
	@pandoc $(EPUB_DIR)/front-matter.md $(SOURCES) apparatus/epub-back-matter.md \
		--from=markdown-implicit_figures --to=epub3 --standalone \
		--toc --toc-depth=1 -V toc-title="Contents" \
		--lua-filter=apparatus/epub-chapters.lua \
		--css=apparatus/epub.css \
		--epub-cover-image=$(EPUB_DIR)/cover-ebook.jpg \
		--resource-path=$(EPUB_DIR) \
		--metadata-file=apparatus/epub-metadata.yaml \
		-o $(OUTPUT_DIR)/the-baltic-approaches.epub
	@ls -la $(OUTPUT_DIR)/the-baltic-approaches.epub
	@echo "Created $(OUTPUT_DIR)/the-baltic-approaches.epub (eBook edition)"

# Front cover (Müller ratified 2026-07-27; planning/cover-brief.md).
# Recomposes the raster from the museum source, sets vector type in
# Heros via xelatex, and emits proof PNG + the 120px shelf-test
# thumbnail (a standing regression artifact per design pass 2).
cover: $(OUTPUT_DIR)
	@python3 scripts/cover-art.py
	@for pass in 1 2; do \
		TEXINPUTS=.: xelatex -interaction=batchmode -output-directory=$(OUTPUT_DIR)/cover apparatus/cover.tex >/dev/null || \
			{ tail -20 $(OUTPUT_DIR)/cover/cover.log; exit 1; }; \
	done  # two passes: tikz remember-picture needs the .aux to place against the page
	@mv $(OUTPUT_DIR)/cover/cover.pdf $(OUTPUT_DIR)/cover/the-baltic-approaches-cover.pdf
	@pdftoppm -r 300 -png -singlefile $(OUTPUT_DIR)/cover/the-baltic-approaches-cover.pdf $(OUTPUT_DIR)/cover/cover-proof
	@pdftoppm -r 14 -png -singlefile $(OUTPUT_DIR)/cover/the-baltic-approaches-cover.pdf $(OUTPUT_DIR)/cover/cover-thumb-120
	@python3 -c "from PIL import Image; im=Image.open('$(OUTPUT_DIR)/cover/cover-proof.png').convert('RGB'); im.crop((37,37,1687,2587)).save('$(OUTPUT_DIR)/cover/the-baltic-approaches-cover.jpg', quality=92)"  # trim-cropped JPG for catalog uploads (Bowker: JPG only, <=5MB)
	@echo "Cover: $(OUTPUT_DIR)/cover/the-baltic-approaches-cover.pdf (+proof, +120px thumb, +catalog JPG)"

# Full POD wrap: back + spine + front (cover-brief.md wrap program).
# SPINE_IN: 0.49in is the ACTUAL for the first edition — verified
# against KDP's cream-paper spec (196pp x 0.0025in/page) at
# publication, 2026-07-28 (status.md service log; cover-brief.md).
# Recompute only if page count or paper changes. Override:
# make cover-wrap SPINE_IN=…
SPINE_IN ?= 0.49

cover-wrap: $(OUTPUT_DIR)
	@python3 scripts/cover-art.py
	@awk -v s=$(SPINE_IN) 'BEGIN{printf "\\def\\spinein{%.4fin}\n\\def\\wrapw{%.4fin}\n\\def\\backhinge{5.6250in}\n\\def\\fronthinge{%.4fin}\n\\def\\frontcenter{%.4fin}\n\\def\\spinecenter{%.4fin}\n", s, 11.25+s, 5.625+s, 8.375+s, 5.625+s/2}' > $(OUTPUT_DIR)/cover/wrapgeom.tex
	@for pass in 1 2; do \
		TEXINPUTS=.: xelatex -interaction=batchmode -output-directory=$(OUTPUT_DIR)/cover apparatus/cover-wrap.tex >/dev/null || \
			{ tail -20 $(OUTPUT_DIR)/cover/cover-wrap.log; exit 1; }; \
	done
	@mv $(OUTPUT_DIR)/cover/cover-wrap.pdf $(OUTPUT_DIR)/cover/the-baltic-approaches-wrap.pdf
	@pdftoppm -r 150 -png -singlefile $(OUTPUT_DIR)/cover/the-baltic-approaches-wrap.pdf $(OUTPUT_DIR)/cover/wrap-proof
	@pdftoppm -r 14 -png -singlefile $(OUTPUT_DIR)/cover/the-baltic-approaches-wrap.pdf $(OUTPUT_DIR)/cover/wrap-thumb
	@python3 -c "from PIL import Image; s=$(SPINE_IN); im=Image.open('$(OUTPUT_DIR)/cover/wrap-proof.png'); w,h=im.size; sc=w/(11.25+s); strip=im.crop((round(5.625*sc),0,round((5.625+s)*sc),h)); strip.save('$(OUTPUT_DIR)/cover/spine-strip.png'); t=strip.resize((max(1,round(strip.width*96/h)),96),Image.LANCZOS); t.save('$(OUTPUT_DIR)/cover/spine-shelf-96px.png')"
	@echo "Wrap: $(OUTPUT_DIR)/cover/the-baltic-approaches-wrap.pdf (spine $(SPINE_IN)in assumed; +proof, +thumb, +spine shelf test)"

# Page-render proof loop (WB practice): thumbnails for eyeballing
# breaks, asterisms, caps blocks. Renders the trade build.
proof: pdf
	@mkdir -p $(OUTPUT_DIR)/proof
	@rm -f $(OUTPUT_DIR)/proof/*.png
	@pdftoppm -r 60 -png $(OUTPUT_DIR)/the-baltic-approaches.pdf $(OUTPUT_DIR)/proof/p
	@echo "Proof renders in $(OUTPUT_DIR)/proof/"

manuscript: $(OUTPUT_DIR)
	@pandoc $(SOURCES) $(PANDOC_OPTS) $(METADATA) -o $(OUTPUT_DIR)/the-baltic-approaches.md
	@echo "Created $(OUTPUT_DIR)/the-baltic-approaches.md"

# Narrative-only count (DK ruling 2026-07-23: apparatus excluded;
# ::: div-fence markup lines excluded — they are typesetting, not text)
wordcount:
	@for f in $(SOURCES); do printf "%6d %s\n" $$(grep -v '^:::' $$f | wc -w) $$f; done
	@printf "Narrative total: %d words (plan 50.5k, ceiling 54.2k)\n" $$(cat $(SOURCES) | grep -v '^:::' | wc -w)

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
	@if [ -d "$(OWN_DIR)" ] && [ "$$(pwd | tr / -)" != "-home-dlk-workspace-the-mission-1986" ]; then \
		python3 scripts/export-transcripts.py --source-dir $(OWN_DIR) $(if $(SKIP),--skip $(SKIP)); \
	fi
	@mkdir -p transcripts/raw
	@for d in $(OWN_DIR) $(NEW_DIR); do \
		[ -d $$d ] || continue; \
		for f in $$d/*.jsonl; do \
			[ -e $$f ] || continue; \
			id=$$(basename $$f .jsonl); \
			case $$id in agent-*) continue;; esac; \
			if [ -n "$(SKIP)" ]; then case $$id in $(SKIP)*) continue;; esac; fi; \
			if [ ! -f transcripts/raw/$$id.jsonl.gz ]; then \
				gzip -c $$f > transcripts/raw/$$id.jsonl.gz; \
				echo "raw-archived $$id"; \
			fi; \
		done; \
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
# (searches both project-dir eras; see OWN_DIR/NEW_DIR note above)
raw-archive:
	@test -n "$(SESSION)" || (echo "usage: make raw-archive SESSION=<uuid>" && exit 1)
	@mkdir -p transcripts/raw
	@src=""; for d in $(OWN_DIR) $(NEW_DIR); do \
		[ -f $$d/$(SESSION).jsonl ] && src=$$d/$(SESSION).jsonl && break; \
	done; \
	test -n "$$src" || { echo "no JSONL for $(SESSION) in either project dir"; exit 1; }; \
	gzip -c $$src > transcripts/raw/$(SESSION).jsonl.gz
	@echo "Archived $(SESSION). Update the ledger's lineage log."
