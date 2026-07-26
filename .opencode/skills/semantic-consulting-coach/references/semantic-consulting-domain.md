# Semantic Consulting Domain Map

Reference for coaching a semantic-technologies / data consulting business. Use it
to ground questions in the real offering, business models, and market dynamics,
not to lecture the user (they know the domain) and not to push a solution. Always
flag a service or model as a *hypothesis* until the user confirms it applies.

## 0. Current positioning & vocabulary (meaningfy.ws)

Ground coaching in how the firm actually talks. Mirror the client's and the
firm's own words; do not impose generic consulting language.

**Mission.** "We empower organisations to build knowledge-centric systems where
information is clear, machines understand context, and people make better
decisions based on shared meaning."

**Live positioning.** A *semantic & datacentric partner* delivering
*interoperability solutions for EU organisations* (public and private). Named
pains: data harmonisation, data silos, turning raw data into actionable insight.
House phrases: "borrow our brain", "digital brain", "single source of truth",
"semantic consensus", "semantic enrichment".

**Emerging positioning (test site, likely repositioning).** From "EU
interoperability" toward *trusted enterprise AI*: "the semantic layer between
your enterprise data and your AI"; "We structure your data, AI extracts the
value"; "Trusted Data. Trusted Reporting. Trusted AI."; AI that is
"deterministic, not probabilistic" through knowledge-graph grounding; reporting
that is "audit-ready, board-ready, regulator-ready".

Coaching use: the **shift from interoperability-for-the-public-sector toward
semantic-layer-for-trusted-AI is a live positioning decision** (which market,
which message, which buyer). The AI-grounding frame is the sharpest new value
story, and the one most likely to commoditise if pitched as "just RAG". Probe
which framing wins which deal, and what stays uniquely Meaningfy's.

## 1. Service families (offering layer)

> **Keystone offering:** the **Decision Phase** (see `engagement-model.md`) sits
> at the head of "Strategic data & semantics advisory" below and gates everything
> downstream.

Grouped by intent. The **decide vs. build** axis matters most: advisory helps the
client *decide*; engineering helps them *build*. Blurring them silently is where
margin and IP leak.

| Family | Includes | Decide / Build | IP exposure | Natural stopping point / handover |
|--------|----------|----------------|-------------|-----------------------------------|
| **Strategic data & semantics advisory** | Data & semantic strategy, semantic-layer strategy, governance operating-model design, roadmaps, maturity assessment | Decide | High (method = the product) | Endorsed roadmap + decision; hand build to client or delivery arm |
| **Data governance & management** | Governance framework, **master data management (MDM)**, **metadata management**, **data quality**, **lineage / tracing**, **cataloguing**, stewardship model | Decide → Build | Medium–High (operating model is IP) | Operating model live + stewards trained |
| **Semantic engineering** | **Ontology engineering**, **taxonomy management**, **knowledge graph creation**, **data mapping**, vocabulary/standards alignment | Build | High (modelling patterns/method) | Validated model + tests + handover docs |
| **Semantic interoperability** | Cross-system mapping, standards conformance, shared vocabularies, exchange schemas | Build | Medium | Conformant exchange in production |
| **NLP & AI grounding** | Semantic search, information extraction, NER, document classification, topic modelling, semantic annotation; **RAG / LLM grounding** via the semantic layer | Build | Medium (method lives in pipelines & prompts) | Extraction or grounded AI in production |
| **Semantic-layer enablement** | Designing/standing up the semantic layer, capability transfer, training, accelerators | Build → Transfer | Medium (accelerators can scale) | Client team self-sufficient |
| **Applied research** | Semantic-domain R&D; Horizon Europe (RIA/IA/CSA), FNR INTER (Luxembourg); TRL 1–3 research-grade prototyping; "research-to-prototype gap"; consortia (e.g. EU Publications Office, infeurope, Univ. Luxembourg/Bologna) | Explore | Low–Medium (often publishable) | Deliverable / publication / prototype |
| **Product development** | Reusable products & accelerators, e.g. **Mapping Workbench** (proprietary), **RDF Differ** | Productise | IP becomes the asset | Released, licensable product |
| **Bespoke software** | Custom apps, PoC/prototype, pilot/MVP on data-centric foundations | Build | Low–Medium | Working software handed over + support |
| **Tool resale** | Reselling third-party platforms (triple stores, catalogues, MDM, taxonomy tools) | Transact | Low | Licence sold + (optionally) implementation |

Coaching use: when the user describes an engagement, locate it in this table,
then probe the **decide/build blur**, **IP exposure**, and whether a **stopping
point** is defined.

**Map to the public service names** (meaningfy.ws): the website groups the same
work as *IT Business Consulting*, *Enterprise Knowledge Graph*, *Semantic Data
Strategy & Architecture*, *NLP Technologies Deployment*, *Software Development*,
and *Research & Development*. Frameworks/standards in play: **SEMIC Style Guide**
(EU interoperability), TOGAF/ArchiMate (architecture).

**Two engagement models, not one; reconcile them.** The public site presents a
four-step funnel (*Discovery → Proposal → Implementation → Delivery*); the
internal model is presale plus Discovery & Onboarding (Light/Deep tiers) and
Semantic Layer adoption's building blocks (see
[`docs/ai-sales/engagement-lifecycle.md`](../../../docs/ai-sales/engagement-lifecycle.md)
and `engagement-model.md`'s coaching frame). They are different axes (a
sales/delivery funnel vs. a free→paid value structure). A recurring coaching
task is aligning the public story with the internal boundaries so the paid
tiers are not lost inside a "Discovery" step that reads as free.

## 2. Business / revenue models (meta-layer)

Each model trades differently on leverage, margin, IP, and scarcity. The strategic
question is the *mix*, not any single one.

| Model | Leverage | Margin shape | IP / scarcity | Watch-outs |
|-------|----------|--------------|---------------|------------|
| **Day-rate / time advisory** | Low (sells hours) | Steady, capped by capacity | Judgement is scarce; method leaks if not protected | Becomes a labour business; no scale |
| **Fixed-scope delivery** | Medium | Depends on estimation & reuse | Patterns reusable across jobs | Scope creep destroys margin |
| **Grant-funded research** | Medium | Funded, low commercial margin | Often must be open / published | Can subsidise R&D and credibility, or distract from revenue |
| **Product / licensing** | High (scales beyond hours) | High once built | Product *is* the IP | Build cost, productisation discipline |
| **Tool resale** | Medium (margin on licences) | Thin but recurring | Little IP; channel relationship | Can anchor you as a reseller, not an advisor |
| **Partnering / subcontracting (subco)** | Varies | Prime keeps margin; sub trades margin for flow | Risk of becoming invisible capacity | Brand dilution; dependence on the prime |

Coaching use: "Where do you make money because of judgement, not labour?" maps the
current mix; "what should never be customised / must stay scarce?" protects the IP
that underwrites margin.

## 3. Markets: B2B vs. B2G

| Dimension | B2B | B2G (public sector / government) |
|-----------|-----|----------------------------------|
| Buying motion | Commercial sales cycle, ROI framing | Formal **tenders**, **framework agreements**, public-procurement rules |
| Cycle length | Shorter, relationship-led | Long, process-led, scheduled |
| Discovery | Can be bounded/paid by negotiation | Often constrained by tender rules; free PoC requests common |
| Partnering | Optional alliances | **Consortia / subco** often required to meet scale or eligibility |
| Drivers | Efficiency, competitive edge, time-to-value | Interoperability mandates, open standards/open data, transparency, compliance |
| IP risk | NDA-protected | Outputs may be public; competitors may see your method |

Concrete anchors: B2G centres on EU institutions and programmes (e.g. EU
Publications Office, Horizon Europe, SEMIC-aligned interoperability); B2B
references include large enterprises and advisories (e.g. KPMG, PwC, NTT Data,
Cargolux), where the AI-grounding / "trusted reporting" story lands.

Coaching use: in B2G, the free-PoC-before-tender trap and IP-exposure-to-rival-
bidders risk are acute; discovery must fit procurement rules. In B2B, the lever is
negotiating paid, bounded discovery and protecting the price anchor.

## 4. Where IP and scope risk concentrate

Highest-exposure (protect; demonstrate with reference patterns, not live method):
- Ontology engineering method and modelling patterns
- Data-mapping approach and reusable mapping patterns
- Governance / MDM operating model

Lower-exposure (safer to demo or give as teasers):
- Tool capabilities and standard platform features (resale)
- Published research outputs
- Generic maturity assessments and high-level roadmaps

Coaching use: every "should we do this for free / cheap / fast?" question should be
checked against *which* of the above it exposes, and whether the engagement blurs
decide-vs-build.
