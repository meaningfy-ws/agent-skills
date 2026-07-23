# Antipatterns — how writing fails, and how to spot it

Sixteen failure modes, grouped by what they damage. Each carries a real example, the cost it
imposes on the reader, a **detection cue** you can run without judgement, and the fix.

Every example is drawn from one real document: an internal marketing and delivery plan, forty
pages, six revisions, three audiences. That is deliberate. These patterns cluster, because they
share a cause: a document that grew by accretion, served readers nobody had authority to
separate, and was written by someone who was not the person who decides.

> **Precedence.** Structure antipatterns outrank texture antipatterns. Fixing the rhythm of a
> document whose spine is repeated eight times is wasted effort. Work top down through the
> groups below.

---

## A. Structure

### A1. The Stage Loop

One underlying sequence, walked from start to finish once per section, each time with a
different column set, and never labelled as a view of the same thing.

- **Example:** the stage list (research, alpha, analysis, beta, controlled launch) is traversed in
  section 3 as conditions, section 4 as current actions, section 5 as later actions, section 6 as
  messages, section 7 as weeks, section 8 as metrics, then twice more in the annex as channels
  and materials. Eight passes over one spine.
- **Cost:** the reader cannot tell whether a section is new information or a re-cut, so they diff
  every table against the previous seven from memory. This is usually the single largest source
  of difficulty in a long document. It also guarantees drift: change the entry criteria once and
  two of the eight views now disagree.
- **Detection cue:** list the first column of every table in the document. If the same set of
  values appears three or more times, you have a Stage Loop.
- **Fix:** one master table carrying all columns. Prose around it explains only exceptions and
  judgement calls. Where a genuine second view is needed, say so in the sentence above it.

### A2. Topic-as-thought

The document states what it covers instead of what it concludes.

- **Example:** "The objective of the plan: to coordinate how we attract and involve the relevant
  senders and carriers at each stage." That describes the folder, not the position.
- **Cost:** there is no sentence a reader can repeat, agree with, or object to. Everything reads
  as administration.
- **Detection cue:** can you find one sentence that survives alone and tells someone what to do?
  If not, the antipattern is present. Being unable to write it is a signal the decision is not
  made, not a signal to try harder at phrasing.
- **Fix:** write the governing sentence before anything else, and lead with it.

### A3. The distributed decision register

Open questions scattered across the document instead of collected in one place.

- **Example:** unresolved decisions appear in section 2 (route), section 5 (unconfirmed
  features), section 8 (open decisions) and annex D6 (information to confirm). Four lists, some
  overlapping, none ranked.
- **Cost:** nobody can see what is actually blocking, so nothing gets closed in order of
  importance. For discovery work this is fatal, because the ranked list of open questions *is*
  the plan.
- **Detection cue:** grep for the words "open", "to confirm", "not yet decided", "TBD". Count
  distinct locations. More than one is the antipattern.
- **Fix:** one register at the front, ranked by how much each item blocks, each with the evidence
  that would close it and the person who owns closing it.

### A4. Overlapping buckets

Two or more sections that are not mutually exclusive, so the same content can legitimately live
in either.

- **Example:** sections 4 and 5 are both titled "action plan". Sections 3 and 8 both carry
  transition conditions.
- **Cost:** the reader must check both to be sure they have the whole picture, and the author
  must edit both to keep them true.
- **Detection cue:** read the table of contents alone. If you cannot say, for any two headings,
  what belongs in one and not the other, they are not MECE.
- **Fix:** re-cut until each section owns its content exclusively.

### A5. The flat priority list

Every priority stated at equal weight.

- **Example:** "the five immediate priorities", listed as five equal bullets with no ordering.
- **Cost:** five equal priorities are none. The team self-selects, usually toward the easiest.
- **Detection cue:** are the priorities ranked, or split into immediate, short-term and later?
  If neither, the antipattern is present.
- **Fix:** rank them, and name one owner each.

### A6. Label headings

Headings that name a topic rather than assert a conclusion.

- **Example:** "Choosing the route for the alpha test" versus what the section actually
  concludes: "We choose one route, on confirmed carriers rather than diaspora size."
- **Cost:** the contents page carries no information, so the document cannot be skimmed and
  cannot be read in ninety seconds by someone who only needs the shape.
- **Detection cue:** does every heading contain a verb and a claim? Nouns-only is the
  antipattern.
- **Fix:** write each heading as the sentence the section proves.

---

## B. Genre and placement

### B1. Genre fusion

Two or more document types bound into one file, written in a single register.

- **Example:** a decision brief (sections 1 to 3, 8), a work plan (4, 5, 7) and a reference
  registry (annexes B and D) in one forty-page file, all written in registry register.
- **Cost:** the register that suits one part actively harms the others. Decisions read like
  inventory, and no reader needs more than a third of the file, but none can tell which third.
- **Detection cue:** name the single reader and the single decision. If you need "and also" to
  answer either, the file is fused.
- **Fix:** split by genre. Decision brief as prose, work plan into the tool that tracks work,
  registry into a spreadsheet.

### B2. Inventory in the body

Reference data placed inline in a document meant to be read.

- **Example:** roughly sixty external links (community groups, operator pages, classified
  listings, supplier sites) inside the annex of a plan, all flagged as unverified.
- **Cost:** it inflates the document, it cannot be sorted or filtered, and its staleness is
  invisible. Unverified entries in a plan look like decisions to a casual reader.
- **Detection cue:** any table with more than roughly fifteen rows, or any table whose rows have
  a status that changes over time, is data, not prose.
- **Fix:** move it to a spreadsheet with a verification column and a last-checked date. Link to
  it once.

### B3. Reference craft applied to Explanation, or the reverse

Using the wrong Diátaxis register for the quadrant.

- **Example:** the "why we do it this way" sections are written as tables of conditions, while
  the sample messages in the annex, which are pure reference, are the warmest prose in the file.
- **Cost:** understanding-oriented content becomes lookup-shaped and stops teaching; lookup
  content becomes discursive and stops being findable.
- **Detection cue:** for each section, ask whether the reader is meant to understand it or to
  look it up. Then check whether the form matches.
- **Fix:** see the fit-map in `explanatory-writing`.

---

## C. Texture

### C1. The actorless action

Actions written as abstract nouns or reflexive passives, with the human deleted.

- **Example:** "Publication and controlled distribution of the questionnaire for senders."
  Also: *se confirmă, se evaluează, se reiau*. Compare: "Adrian publishes the questionnaire on
  Monday and distributes it in three groups."
- **Cost:** no actor, no tense, no verifiability. On Tuesday nobody can say whether it happened.
  In Romanian and other administrative registers this is the default setting, so it takes
  deliberate effort to avoid.
- **Detection cue:** grep for nominalised verb forms (`-area`, `-irea`, `-tion`, `-ment`) at the
  start of a list item, and for reflexive passives. Then ask of each: who, and by when?
- **Fix:** subject, verb, object. Name a person, not "the team".

### C2. The deferred legend

Coined terms used long before they are defined.

- **Example:** alpha, beta, controlled launch, resolved request, usable response and validated
  route all appear in section 1. Their definitions sit in annex D1, roughly forty pages later.
- **Cost:** every term is a loan the reader takes out early and repays at the end. Meanwhile
  they guess, and two readers guess differently.
- **Detection cue:** for each term in your glossary, find its first occurrence. If the gap is more
  than a page, the antipattern is present.
- **Fix:** coin and explain once, at first use, in one line. Keep the glossary as a reference copy.

### C3. The floating abstraction

An abstract claim with no concrete instance beside it.

- **Example:** "incomplete messages and repeated clarifications" is asserted roughly a dozen
  times. The team has those messages, and not one appears in the document.
- **Cost:** the claim cannot be checked against experience, so the reader spends effort decoding
  instead of understanding, and the argument never becomes vivid enough to act on.
- **Detection cue:** count the named examples per page. Under one is thin. Zero across a section
  that argues something is the antipattern.
- **Fix:** one real artefact. A screenshot, a quoted message, a specific week.

### C4. Hedge-as-register

Epistemic caution applied per sentence instead of stated once as a principle.

- **Example:** relevant, usable, sufficient, realistic, within the agreed interval, indicative,
  provisional, to be confirmed. Every claim arrives pre-qualified.
- **Cost:** this one is cruel, because the underlying honesty is a virtue. Spread thinly, it
  reads as indecision. Concentrated, it reads as discipline.
- **Detection cue:** count hedging adjectives per hundred words. If the same three recur on every
  page, they have become the register rather than a signal.
- **Fix:** state the principle once at the top ("we do not communicate what we cannot
  demonstrate"), then write declaratively underneath it, and reserve hedges for the specific
  claims that genuinely need them.

### C5. Ownership smear

Responsibility assigned to more than one person, or to a collective, or conditionally.

- **Example:** "Adrian; Eugen consulted on the process", "the team supports distribution",
  "owners to be confirmed after beta".
- **Cost:** two owners is no owner. The task survives to the next revision unchanged.
- **Detection cue:** count the names in each owner cell. More than one, or a collective noun, is
  the antipattern.
- **Fix:** one accountable name per line. Consultation is a separate column.

### C6. The prose gate

A transition condition written as description rather than as a testable predicate.

- **Example:** "at least one route can realistically be prepared", "sufficient evidence for
  go / hold / redo".
- **Cost:** the gate cannot be passed or failed, so it is passed by whoever wants to move on, and
  the argument happens afterwards.
- **Detection cue:** could a person declare this met or not met on a Friday afternoon, without
  discussion? If not, it is prose.
- **Fix:** a predicate with a threshold, a measurement method, an owner, a target date and a
  failure branch. Four lines is enough.

### C7. The terminal admin note

A document that ends on housekeeping instead of landing its point.

- **Example:** the final line explains which part of the file to consult and when.
- **Cost:** the momentum built over forty pages is discarded in the last sentence.
- **Detection cue:** read the last two sentences alone. Do they say anything a reader would carry
  out of the room?
- **Fix:** a confident, grounded close. Specific, not sweeping.

### C8. The bland sentence

A sentence that could appear in any organisation's document about any project.

- **Example:** "Each material has an audience, a single requested action and an owner."
  "Messages are hypotheses until the audience understands them and acts."
- **Cost:** true, wise, and weightless. Filler crowds out the specific number, the real trade-off
  and the actual next step.
- **Detection cue:** replace the project name with a competitor's. If the sentence still reads
  correctly, it is filler.
- **Fix:** replace with the specific. Generic is a defect, not a safe default.

---

## D. Form

### D1. Universal emphasis

Bold, capitals or colour applied to every label.

- **Example:** every table header, every row label and most lead-ins are bold.
- **Cost:** emphasis on everything is emphasis on nothing, and the genuinely important line
  cannot be found.
- **Detection cue:** what proportion of lines carry bold? Above roughly a fifth, it has stopped
  signalling.
- **Fix:** reserve emphasis for what would still matter if the rest were skimmed.

### D2. The centred table

Text columns centre-aligned.

- **Example:** every table in the document uses centred alignment.
- **Cost:** ragged left edges measurably slow scanning, which is the only thing tables are good
  for.
- **Detection cue:** grep the alignment row for `:-:` on text columns.
- **Fix:** left-align text, right-align numbers, centre nothing but short status flags.

### D3. Table-as-prose

Two-column tables whose cells are sentences, and cells that chain several items with semicolons
in non-parallel grammar.

- **Example:** "Guided request; identification of relevant carriers; response presented clearly;
  simple request states; clear communication on coverage." A noun, a nominalisation, a participle
  and two more nouns, in one cell.
- **Cost:** a table implies the columns relate. Here they do not, so the reader gets the overhead
  of a grid with none of the benefit. Non-parallel enumeration is one of the most reliable
  comprehension killers there is.
- **Detection cue:** does the table have a genuine second dimension, or is it a list with a label
  column? Are the items in each cell grammatically parallel?
- **Fix:** convert to a list. Make every item start with the same part of speech.

### D4. The versionless version

A numbered revision with no record of what changed.

- **Example:** v0.6, and nothing anywhere says what moved since v0.5.
- **Cost:** returning readers must re-read the whole document to find the delta, so they do not
  re-read it at all.
- **Detection cue:** does a version number exist without a changelog?
- **Fix:** three lines at the top: what changed, what it means, what still needs a decision.

---

## Running this as a check

Work in order. Group A first, because structure defects make texture work pointless. Then B,
then C, then D. Ten of the sixteen cues can be run mechanically, and those are worth automating
before anything else.

One caution. This list describes symptoms, and symptoms have causes. A document showing eight of
these usually has an organisational reason: it grew by accretion, or it serves readers nobody may
separate, or its author cannot make the decision the document keeps deferring. Fix the writing
and the same shape returns two revisions later. Name the cause in the review, or the review does
not hold.
