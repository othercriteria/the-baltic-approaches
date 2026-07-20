# The Mission (1986) - Step-0 targets
#
# The manuscript build targets arrive with Phase 1 (see white-buffalo's
# Makefile for the shape they will take). What exists now is the
# provenance machinery from planning/attribution.md.
#
#   make transcripts           - Export this project's session transcripts
#   make transcripts-founding  - Export + raw-archive the founding session
#                                (656ec2ba, stranded in -home-dlk-workspace)
#
# Run these as DK: moving session logs into the repo is a human act
# (attribution.md, refinement 1).

FOUNDING_ID = 656ec2ba-b295-4e5d-8712-5e270300dcde
FOUNDING_DIR = $(HOME)/.claude/projects/-home-dlk-workspace
OWN_DIR = $(HOME)/.claude/projects/-home-dlk-workspace-the-mission-1986

.PHONY: transcripts transcripts-founding raw-archive

transcripts:
	@python3 scripts/export-transcripts.py

transcripts-founding:
	@python3 scripts/export-transcripts.py --source-dir $(FOUNDING_DIR) $(FOUNDING_ID)
	@mkdir -p transcripts/raw
	@gzip -c $(FOUNDING_DIR)/$(FOUNDING_ID).jsonl > transcripts/raw/$(FOUNDING_ID).jsonl.gz
	@echo "Archived $(FOUNDING_ID) (raw + transcript). Update the ledger's lineage log."

# Archive a wrapped session's raw JSONL: make raw-archive SESSION=<uuid>
raw-archive:
	@test -n "$(SESSION)" || (echo "usage: make raw-archive SESSION=<uuid>" && exit 1)
	@mkdir -p transcripts/raw
	@gzip -c $(OWN_DIR)/$(SESSION).jsonl > transcripts/raw/$(SESSION).jsonl.gz
	@echo "Archived $(SESSION). Update the ledger's lineage log."
