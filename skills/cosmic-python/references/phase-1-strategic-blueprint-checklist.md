# Phase 1: Strategic Blueprint Checklist

**Duration:** 40% of total project time
**Goal:** Answer the 7 Questions so clearly that Phase 2 implementation is obvious
**Output:** Strategic Blueprint document + ADRs for major architecture decisions

---

## Pre-Phase 1: Documentation Audit (If Applicable)

**Only complete this if you have existing documentation.**

- [ ] Read through ALL existing documentation (specs, READMEs, notes, etc.)
- [ ] For each document, apply the Clarity Test:
  - [ ] **Actionable** – Can AI act on this? (Delete aspirational)
  - [ ] **Current** – Is this still true? (Update or remove)
  - [ ] **Single Source** – Is this repeated elsewhere? (Consolidate)
  - [ ] **Decision** – Is this decided or wished? (Keep decisions only)
  - [ ] **Prompt-Ready** – Would you feed this to AI? (Delete if no)
- [ ] Delete everything that fails the Clarity Test
- [ ] Target: 40-50% reduction in volume
- [ ] Consolidate remaining content into single-source documents

**When done:** Proceed to The 7 Questions below

---

## The 7 Questions Framework

Answer each question with **specificity**. Vague answers = vague architecture = vague code.

### Question 1: What exact problem are you solving?

**❌ Reject:**
- "Help users manage tasks"
- "Make it easier to track stuff"
- "Improve productivity"

**✅ Require:**
- Specific persona: "Solo SaaS founders building their first MVP"
- Specific outcome: "Ship to production in <3 months without hiring a full team"
- Specific context: "Working 10 hours/week on product, managing 1000+ users"

**Your Answer:**

```
Persona: [Who specifically?]
Problem: [What specific pain do they have?]
Context: [In what situation does this happen?]
Outcome: [What measurable outcome do they want?]
```

**Implementation Implication:**
_How does this constrain your technical choices? (e.g., must be solo-buildable, low maintenance ops)_

---

### Question 2: What are your success metrics?

**❌ Reject:**
- "Users save time"
- "Better experience"
- "Faster performance"

**✅ Require:**
- Numbers: "100 users by month 3"
- Conversion: "25% conversion from free to paid"
- Timeline: "Achieve product-market fit by Q2 2025"
- Retention: "80%+ monthly active users"

**Your Answer:**

```
Primary Metric: [The ONE thing that means success?]
Target: [Specific number?]
Timeline: [By when?]

Secondary Metrics:
- [Metric 2]: [Target]
- [Metric 3]: [Target]
```

**Implementation Implication:**
_How does this shape your MVP scope? (What features directly drive these metrics?)_

---

### Question 3: Why will you win?

**❌ Reject:**
- "Better UI"
- "More features"
- "We're faster"

**✅ Require:**
- Structural advantage: "We're the only ones using [data model] approach"
- Network effect: "Our data moat grows with each user"
- Business model: "We're profitable at 1/5 the customer acquisition cost"
- Technology: "We can deliver 10x faster because of [architecture choice]"

**Your Answer:**

```
Competitive Advantage: [Why will this win against alternatives?]
Why Now: [Why can this succeed in 2025?]
Defensibility: [What makes this hard to copy?]
```

**Implementation Implication:**
_What technical choices protect this advantage?_

---

### Question 4: What's the core architecture decision?

**❌ Reject:**
- "Let AI decide the architecture"
- "We'll figure it out as we go"
- "Stack X because it's trendy"

**✅ Require:**
- Explicit trade-off: "Monolithic backend (faster to ship) vs microservices (easier to scale)"
- Data model decision: "Relational (ACID) vs document (flexibility)"
- Deployment: "Serverless (low ops) vs containers (cost control)"

**Your Answer:**

```
The Big Decision: [The ONE architecture choice that defines the system?]

Trade-off Analysis:
Option A: [Choice]
  Pros: [Why this is good]
  Cons: [Why this is risky]
  Risk: [What can go wrong?]

Option B: [Choice]
  Pros: [Why this is good]
  Cons: [Why this is risky]
  Risk: [What can go wrong?]

Winner: [A or B? Why?]
Rationale: [Decision documented for future review (this is your ADR)]
```

**Implementation Implication:**
_This becomes Cosmic Python architectural decision in Phase 2_

---

### Question 5: Why this tech stack?

**❌ Reject:**
- "Node because I like it"
- "Python is popular"
- "React because that's what everyone uses"

**✅ Require:**
- Team expertise: "Python—3 years production experience, ship fast"
- Business rationale: "PostgreSQL—proven at scale, costs $50/month, team knows it"
- Strategic fit: "Serverless backend—matches our "no-ops" competitive advantage"

**Your Answer:**

```
Backend:
- Language: [Python/Node/Go/Rust/etc]
- Framework: [Django/FastAPI/Express/etc]
- Database: [PostgreSQL/MongoDB/etc]
- Why: [Business rationale for EACH choice]

Frontend:
- Framework: [React/Vue/Svelte/etc]
- Why: [Business rationale]

DevOps:
- Deployment: [Serverless/Docker/VPS/etc]
- Why: [Business rationale]
- Cost estimate: [$/month]
```

**Implementation Implication:**
_This tech stack shapes your Cosmic Python layer design in Phase 2_

---

### Question 6: What are the MVP features?

**❌ Reject:**
- 10+ features
- "Everything sounds important"
- Nice-to-haves mixed with must-haves

**✅ Require:**
- Maximum 3-5 features
- Each one directly drives success metric from Question 2
- Everything else explicitly deferred

**Your Answer:**

```
MVP Must-Haves (3-5 only):
1. [Feature 1]: Why essential? [How does it drive Question 2 metric?]
2. [Feature 2]: Why essential? [How does it drive Question 2 metric?]
3. [Feature 3]: Why essential? [How does it drive Question 2 metric?]

Post-MVP (Explicitly Deferred, with rationale):
- [Feature 4]: Why not now? [When will you build this?]
- [Feature 5]: Why not now? [When will you build this?]
- [Feature 6]: Why not now? [When will you build this?]
```

**Implementation Implication:**
_This MVP scope directly translates to your Cosmic Python services/entrypoints_

---

### Question 7: What are you NOT building?

**❌ Reject:**
- "We'll see what users want"
- "Everything is possible"
- No explicit boundaries

**✅ Require:**
- Explicit exclusions with rationale
- Examples: "No mobile app (cost vs benefit)", "No AI personalization (premature)", "No multi-tenancy (future)"

**Your Answer:**

```
Explicit Out-of-Scope (with rationale):
- [Feature]: Why not now? [When might it happen?]
- [Feature]: Why not now? [When might it happen?]
- [Feature]: Why not now? [When might it happen?]

Top 3 Risks & Mitigation:
1. Risk: [What could go wrong?]
   Mitigation: [How will you prevent/handle it?]
2. Risk: [What could go wrong?]
   Mitigation: [How will you prevent/handle it?]
3. Risk: [What could go wrong?]
   Mitigation: [How will you prevent/handle it?]
```

**Implementation Implication:**
_These exclusions prevent scope creep. Include in Phase 2 anti-patterns and error handling_

---

## Phase 1 Deliverables

### Strategic Blueprint Document

Create a document answering all 7 questions with **Implementation Implications** for each section.

**Minimum structure:**

```markdown
# Strategic Blueprint: [Project Name]

## 1. THE CORE
- Problem: [Answer to Q1]
- Success Metrics: [Answer to Q2]
- **Implementation Implication:** [How does this constrain technical choices?]

## 2. COMPETITIVE ADVANTAGE
- Why We Win: [Answer to Q3]
- **Implementation Implication:** [What technical choices protect this?]

## 3. TECHNICAL ARCHITECTURE
- Core Decision: [Answer to Q4]
- Tech Stack: [Answer to Q5]
- **Implementation Implication:** [Layer design, deployment approach]

## 4. EXECUTION SCOPE
- MVP Features (3-5): [Answer to Q6]
- Explicitly Deferred: [Answer to Q7]
- Top 3 Risks: [Risks and mitigations]
- **Implementation Implication:** [Scope for Phase 2 specs]

## 5. REFERENCES
- Links to implementation details (Phase 2 specs)
- Links to ADRs
```

### Architecture Decision Records (ADRs)

For each major architecture decision (from Question 4-5), write an ADR:

**ADR template:**

```markdown
# ADR: [Decision Title]

## Context
[What problem are we solving?]
[Why does this matter?]

## Decision
[What are we doing?]
[Why this option over others?]

## Rationale
[Explain the trade-offs]
[Why is this the best choice?]

## Consequences
[What becomes easier?]
[What becomes harder?]
[What future decisions does this enable/disable?]

## Related Decisions
[What other decisions does this relate to?]
```

---

## Phase 1 Exit Criteria

- [ ] Question 1 answered at "Require" level (specific problem, persona, outcome)
- [ ] Question 2 answered at "Require" level (concrete metrics + timeline)
- [ ] Question 3 answered at "Require" level (structural advantage documented)
- [ ] Question 4 answered at "Require" level (core architecture decision + trade-off analysis)
- [ ] Question 5 answered at "Require" level (tech stack + rationale for each choice)
- [ ] Question 6 answered at "Require" level (3-5 MVP features, everything else deferred)
- [ ] Question 7 answered at "Require" level (explicit exclusions + risk mitigation)
- [ ] Strategic Blueprint document created
- [ ] ADRs written for major architecture decisions
- [ ] Every section has "Implementation Implication" note
- [ ] Zero ambiguity about WHAT you're building
- [ ] Ready for Phase 2 (you can hand this to someone else and they'd understand everything)

---

## Validation Checklist

Before moving to Phase 2, verify:

- [ ] All 7 questions answered at specificity level
- [ ] No vague statements like "fast", "scalable", "user-friendly"
- [ ] All decisions have rationale (explain WHY)
- [ ] MVP scope is 3-5 features maximum
- [ ] Deferred features have explicit rationale
- [ ] Strategic Blueprint references Phase 2 specs (not duplicates)
- [ ] ADRs document major architecture choices
- [ ] Risk mitigations are concrete (not aspirational)

**If ANY item fails:** Fix Phase 1 before proceeding to Phase 2.

---

## Common Phase 1 Mistakes

❌ **Mistake 1:** Answering questions vaguely
✅ **Fix:** Every answer should have numbers, timelines, specific personas

❌ **Mistake 2:** Including too many MVP features
✅ **Fix:** Cut ruthlessly. If you can't explain why a feature is MVP, it's not MVP.

❌ **Mistake 3:** "Architecture TBD"
✅ **Fix:** Make the big decision NOW. Don't defer architecture choices.

❌ **Mistake 4:** Not documenting trade-offs
✅ **Fix:** Write out what you rejected and WHY. This is your ADR.

❌ **Mistake 5:** Forgetting Implementation Implications
✅ **Fix:** For every strategic decision, note "This means in Phase 2 we will..."

---

## Next: Phase 2

Once Phase 1 is complete and validated:
1. Move to Phase 2: AI-Ready Documentation
2. For each MVP feature and system component, write Implementation Specs
3. Include the 4 Mandatory Sections: Anti-patterns, Test Cases, Error Handling, Deep Links
4. Ensure all references point to specific sections (no vague "see technical annexes")
5. Run the Clarity Gate before proceeding to Phase 3

**See:** phase-2-clarity-gate-checklist.md
