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

.PHONY: archive transcripts transcripts-founding raw-archive

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
