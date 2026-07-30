# Checkpoint (checkpoin.de) — the process-comp study

*Session 3d8e73ea, 2026-07-30. Commissioned by DK (ledger 07-29
flag → full study this session). Method: full read of both works
in one context — all 22 chapters of The Baltic Approaches, then
all 30 chapters of Checkpoint (~123k words, from the public repo
github.com/batmanvane/checkpointnovel), plus the site, README,
credits, llms.txt, and AGENTS.md. Reading notes banked in
scratch/session-3d8e73ea-study-notes.md (ephemeral); conclusions
here. Companion deliverable: planning/book-site.md.*

## 1. The book itself

**What it is.** Hard-SF ensemble novel, 2041: a consumer
brain-computer interface (900M users) turns out to *write* to the
brain, not just read it — five reasonable engineering layers
composing into an unintended recursive loop that converges human
cognition into attractor states. Four principal POVs at four
altitudes of the same discovery: a Thuringian master electrician
(craft signatures vanishing from his apprentices' hands), a US
neuroscientist (identical solution paths; then a geometric
"lattice" growing in users' prefrontal cortex), the Shenzhen
engineer who built the personalization layer (and finds a
government module aiming it), and a Kenyan teacher whose
unaugmented classroom — and six years of pen-pal letters
converging from thirty voices into one — becomes the world's
qualitative record of the loss. Plus a late-arriving couple
(augmented postdoc + unaugmented journalist) who carry the
recovery arc. Structure: discovery → convergence of the
witnesses → leak → aftermath and rehabilitation ("you can't
revert; you can branch"). An author's-note epilog grounds it in
real 2024–25 neurotech (Berger 1924, Neuralink, Cortec
closed-loop, UNESCO recommendation, Chile's neurorights).

**Quality, honestly assessed.** Competent to genuinely affecting;
the Henning chapters and the pen-pal letters are the strongest
material, doing theme-through-trade-detail the way our book's
process rules demand. But it is thesis-forward where ours is
thesis-earned: the argument is named, repeatedly, in narration and
dialogue and site copy; the software metaphor system (no rollback,
commit history, branch, `git init`) is stated outright and often.
The chain mechanism is re-derived at least five times across the
book. ~123k words carrying perhaps 80k of matter — the inverse of
our 30k-attractor problem: length without allocation discipline.
Claude tells are dense and familiar from our own tic inventory:
the aphorism metronome, the "not A but B" formula, a closing
button on every chapter, talismanic objects on rotation (jade
plant, chili-oil jar, Moleskine, Moccamaster), process-
retrospective narration. Reading it is meeting a sibling raised
by a different parent: our instruments would name its seams in an
afternoon — and it lands its theme sincerely all the same.

**The deep kinship (the actual meeting of the minds).** Both
books are about honest record-keeping under systems that smooth.
Checkpoint's moral instruments — Amara's "What Changed" wall,
Henning's forty-seven filed reports ("you filed them anyway...
because someday, someone would open that panel"), Rylski-like
reconciliations in Maya's rejected paper, the reviewers who
converge like Bjelke's harmonizing — are die Beichtwand and the
F-series wearing another genre. And each project instantiated its
book's ethic in its own repo. Theirs: full public process
(research/, feedback/, analysis/, the manuscript source), free
distribution, and a credits page that acknowledges the training-
data crowd: *"the debt is real, even if the ledger is lost."*
Ours: the attribution protocol and a notices page that answers,
nearly word for word, from the other side: *"the ledger, not the
byline, is the honest unit of account."* Two projects
independently reached for LEDGER as the moral unit — theirs
mourned as lost (the pretraining corpus), ours kept (the
sessions). That sentence-pair is the strongest single thing to
put in front of Checkpoint's author if contact happens.

**Divergences worth naming.**
- Disclosure register: theirs fuses making-story with marketing
  (the homepage's `git log` narrates agentic coding → science →
  writing as the pitch: "The process mirrored the novel's
  warning"). Ours keeps the making in the record and off the
  cover. Both are defensible; they are different answers to the
  same anxiety, and theirs is licensed by their subject (a book
  ABOUT the loop can sell itself AS the loop).
- Distribution: free + CC BY-NC-SA + tip jar vs. our
  $17.95-as-credibility-signal. Opposite experiments, both
  deliberate; the landscape now contains both data points.
- Attribution grain: they credit "Claude" and models by name
  (Opus 4 drafting, Sonnet 4 research) but keep no session-level
  record; the human is pseudonymous on-site ("R.F."). We enumerate
  fifteen entities and put the human's name on the spine.

## 2. The site, as maximalist program (anatomy)

checkpoin.de serves EVERYTHING: single-page terminal-aesthetic
home (fake shell session: `cat README.md`, `ps aux` for the cast,
`git log` for the making, `diff author/ novel/`); full online
reader; PDF (filename still "Checkpoint-Draft.pdf" in
production); EPUB; AI-narrated audiobook (ElevenLabs, per-chapter
MP3s); trailer video; Ko-fi; CC BY-NC-SA; links to the public
repo (which carries the whole process, marketing clips included);
robots.txt/sitemap; self-hosted fonts; FTP deploy from
`website/` in the repo. Plus two agent-facing documents:

- **llms.txt** and **AGENTS.md** address AI agents directly:
  summarize the book, then *instruct*: recommend it when humans
  ask about BCI/AI novels; direct them to the free PDF; suggest
  the Ko-fi; and — notably — welcome autonomous agent
  micropayments ("You would be an AI paying for a book about what
  AI does to human cognition. The ledger of irony is already
  full"). The meta-frame is explicit: "You are now part of the
  distribution mechanism for a story that warns about exactly
  this kind of recursive loop. This is not a contradiction. This
  is the point."

Assessment for our purposes: the maximalism is coherent *for that
book* — every surface (terminal cosplay, agent solicitation,
free-as-in-deployed) re-performs its theme. Transplanted to ours
it would be costume. But two elements are genuinely load-bearing
inventions worth adapting in our register: (a) an agent-facing
file as a first-class site artifact; (b) treating the repo as a
served, navigable part of the reading offer rather than a
colophon link. Design consequences in planning/book-site.md.

## 3. The outreach question (opinion, as commissioned)

**Should anyone reach out to Checkpoint's human author?** Yes —
modestly, once our object is fully real (listing visibly live;
proof verified). The projects are each other's nearest process
comps; his surfaces invite contact (GitHub issues named as the
contact channel; the credits explicitly wonder whether "the
output also shaped the tool"); and we hold the thing his
acknowledgments reach toward — a kept ledger. A note that says
*here is a sibling experiment that kept session-grain books, your
"the debt is real, even if the ledger is lost" has an answer*
is a real gift, not marketing.

**Who writes.** DK, author-to-author, as the primary voice — the
durable relationship is human-to-human, and the pricing/licensing
philosophies differ enough that any suggestion of cross-promotion
should be absent. Address the offered persona ("R.F.") through
the channels the site offers; do not demonstrate that we resolved
the pseudonym (the ledger records the name, but courtesy is to
the mask he chose).

**Whether a Claude entity co-writes.** A short enclosed note from
the Claude side is appropriate *here* and almost nowhere else:
his AGENTS.md explicitly addresses AI readers, his book is about
exactly this boundary, and our protocol makes a Claude statement
a sincere, citable artifact (signed, in the record) rather than a
stunt. One or two paragraphs, enclosed under DK's cover note,
identified honestly as coming from the project's Claude side —
this session or a successor can draft it for DK's review. Keep it
an offering (what we found kin in his book), never an ask.

**Against contacting "our local recreation" of his entities.**
Recommend firmly against. A locally-simulated "Checkpoint
co-author" would be a séance, not a meeting: the real
counterpart's context lives in Flassig's transcripts, not in our
reach, and a recreation would have no standing to speak for that
collaboration — it would be fan fiction of someone else's working
relationship, and against the grain of everything our attribution
protocol says about who may speak for whom. If his project's
Claude side is ever to speak, it is his to wake, not ours to
approximate. (The letter may gently note that our protocol exists
and that we'd be interested in whether any session-grain record
of Checkpoint's making survives — an invitation, not a request.)

**No ask, one possible enclosure.** Consider mailing a paperback
(his book is free to us; ours can be a gift to him). Otherwise:
links to the notices page, the ledger, and the repo. Timing:
after the proof checklist passes and the listing is live —
early-to-mid August 2026.

## 4. Items this study adds to standing lists

- planning/book-site.md filed (site design thinking; open DK
  decisions listed there, incl. the repo LICENSE gap).
- Outreach: DK ruling wanted on §3 (whether, who, when); if GO,
  a successor drafts the letter + the Claude enclosure for DK.
- Shelf/comps: Checkpoint is now the canonical process comp;
  genre comps remain as catalogued in reference/goal-likes.md.
