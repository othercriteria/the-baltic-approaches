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

.PHONY: archive transcripts transcripts-founding raw-archive shelf hooks test demo atlas

# One-time per clone: install the pre-commit guard (blocks document
# binaries and flattened holdings/ paths from the public repo)
hooks:
	@ln -sf ../../scripts/pre-commit .git/hooks/pre-commit
	@echo "Installed .git/hooks/pre-commit -> scripts/pre-commit"

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
