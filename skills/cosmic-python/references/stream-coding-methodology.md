# Stream Coding: Documentation-First Development Methodology

**From:** [Stream Coding v3.4](https://github.com/frmoretto/stream-coding) by Francesco Marinoni Moretto

This reference bridges the gap between strategic thinking and technical architecture. **Stream Coding provides the methodology for PLANNING and DOCUMENTING before coding.** Combined with Cosmic Python's architectural patterns, you have a complete end-to-end approach.

---

## The Core Insight

> **"When code fails, fix the spec—not the code. If your docs are good enough, AI writes the code."**

### The 40/40/20 Split

| Phase | % Time | Focus | Output |
|-------|--------|-------|--------|
| **Phase 1: Strategic Thinking** | 40% | WHAT to build, WHY it matters | Strategic Blueprint, ADRs |
| **Phase 2: AI-Ready Documentation** | 40% | HOW to build (specs so clear AI has zero decisions) | Technical Specs with 4 sections |
| **Phase 3: Execution** | 15% | Code generation + implementation | Production code |
| **Phase 4: Quality & Divergence Prevention** | 5% | Testing, refinement, prevent drift | Maintained specs = maintained code |

### Why This Works

**Traditional development:** 20% planning, 80% coding → 50% of time debugging/refactoring

**Stream Coding:** 80% planning, 20% coding → 10% of time on rework

The counterintuitive truth: **Documentation is the hard work. Code is just the printout.**

---

## PHASE 1: STRATEGIC THINKING (40% of time)

### Input: Do you have existing documentation?

**If YES:** Start with Documentation Audit
**If NO:** Skip audit, go straight to 7 Questions

### Documentation Audit (If Existing Docs)

Apply the Clarity Test to ALL existing documentation:

| Check | Question | Action |
|-------|----------|--------|
| **Actionable** | Can AI act on this? | Delete aspirational content |
| **Current** | Is this still the decision? | Update or remove outdated items |
| **Single Source** | Is this said elsewhere? | Consolidate to one place |
| **Decision** | Is this decided? | Don't include wishful thinking |
| **Prompt-Ready** | Would you put this in an AI prompt? | Delete if no |

**Target:** 40-50% reduction in volume without losing actionable information.

### The 7 Questions Framework

Before ANY documentation, answer these with specificity:

| # | Question | ❌ Reject | ✅ Require |
|---|----------|-----------|------------|
| 1 | **What exact problem are you solving?** | "Help users manage tasks" | "Help [persona] achieve [outcome] in [context]" |
| 2 | **What are your success metrics?** | "Users save time" | Numbers + timeline: "100 users, 25% conversion, 3 months" |
| 3 | **Why will you win?** | "Better UI and features" | Structural advantage: architecture, data moat, business model |
| 4 | **What's the core architecture decision?** | "Let AI decide" | Human decides based on explicit trade-off analysis |
| 5 | **Why this tech stack?** | "Node.js because I like it" | Business rationale: "Node—team expertise, ship fast" |
| 6 | **What are MVP features?** | 10+ "must-have" features | 3-5 truly essential, rest explicitly deferred |
| 7 | **What are you NOT building?** | "We'll see what users want" | Explicit exclusions with rationale |

### Phase 1 Deliverable: Strategic Blueprint

**Must include (with "Implementation Implication" for each):**

- **THE CORE**: Problem, User persona, Value proposition
- **ECONOMIC ENGINE**: Pricing, Unit economics, Distribution
- **TECHNICAL ARCHITECTURE**: The "big decision", Stack rationale, Data model
- **EXECUTION SCOPE**: MVP must-haves (3-5 only), Explicitly deferred, Top 3 risks
- **REFERENCES**: Links to implementation details (not duplicates!)

**Phase 1 Exit Criteria:**
- [ ] All 7 questions answered at "Require" level
- [ ] Strategic Blueprint created
- [ ] ADRs for major architectural choices
- [ ] Zero ambiguity about WHAT you're building

---

## PHASE 2: AI-READY DOCUMENTATION (40% of time)

### The 4 Mandatory Sections (Every Implementation Document)

#### 1. Anti-Patterns Section (DO NOT)

**Why:** AI needs to know what NOT to do. Prevents hallucination and bad patterns.

**Format:** Tables with concrete examples

```markdown
## Anti-Patterns (DO NOT)

| ❌ Don't | ✅ Do Instead | Why |
|----------|---------------|-----|
| Store timestamps as Date objects | Use ISO 8601 strings | Serialization issues |
| Hardcode configuration values | Use environment variables | Deployment flexibility |
| Use generic error messages | Specific error codes per failure | Debugging impossible otherwise |
| Skip validation on internal calls | Validate everything | Internal calls can have bugs too |
| Expose internal IDs in APIs | Use UUIDs or slugs | Security and flexibility |
```

**Rule:** Minimum 5 anti-patterns per implementation document.

#### 2. Test Case Specifications

**Why:** AI needs concrete verification criteria. Testable specs prevent guessing.

**Format:** Detailed tables with inputs, outputs, edge cases

```markdown
## Test Case Specifications

### Unit Tests Required
| Test ID | Component | Input | Expected Output | Edge Cases |
|---------|-----------|-------|-----------------|------------|
| TC-001 | Tier classifier | 100 contacts | 20-30 in Critical | Empty list, all same |
| TC-002 | Score calculator | Activity array | Score 0-100 | No events, >1000 events |

### Integration Tests Required
| Test ID | Flow | Setup | Verification | Teardown |
|---------|------|-------|--------------|----------|
| IT-001 | Auth flow | Create test user | Token refresh works | Delete test user |
```

**Rule:** Minimum 5 unit tests, 3 integration tests per component.

#### 3. Error Handling Matrix

**Why:** AI needs to know how to handle every failure mode. Prevents silent failures.

**Format:** Separate matrices for external service errors and user-facing errors

```markdown
## Error Handling Matrix

### External Service Errors
| Error Type | Detection | Response | Fallback | Logging | Alert |
|------------|-----------|----------|----------|---------|-------|
| API timeout | >5s response | Retry 3x exponential | Return cached | ERROR | If 3 in 5 min |
| Rate limit | 429 response | Pause 15 min | Queue for retry | WARN | If >5/hour |

### User-Facing Errors
| Error Type | User Message | Code | Recovery Action |
|------------|--------------|------|-----------------|
| Quota exceeded | "You've used all checks this month." | 403 | Show upgrade CTA |
| Session expired | "Please sign in again." | 401 | Redirect to login |
```

**Rule:** Every external service and user-facing error must be specified.

#### 4. Deep Links (All Document Types)

**Why:** AI needs to navigate to exact locations. "See Technical Annexes" is useless.

**Format:** Precise references with paths and anchors

```markdown
## References

### Schema References
| Topic | Location | Anchor |
|-------|----------|--------|
| User profiles | [Schema Ref](../schemas/schema.md#user_profiles) | `user_profiles` |
| Events table | [Schema Ref](../schemas/schema.md#events) | `events` |

### Implementation References
| Topic | Document | Section |
|-------|----------|---------|
| Auth flow | [API Spec](../specs/api.md#authentication) | Section 3.2 |
| Rate limiting | [API Spec](../specs/api.md#rate-limiting) | Section 5 |
```

**Rule:** NEVER use vague references. ALWAYS include document path + section anchor.

---

## ⚠️ THE CLARITY GATE (Mandatory Between Phase 2 & 3)

**NEVER SKIP THIS GATE.** This is the difference between stream coding and vibe coding.

### The 13-Item Clarity Gate Checklist

#### Foundation Checks (7 items)

- [ ] **Actionable** – Can AI act on every section? (No aspirational content)
- [ ] **Current** – Is everything up-to-date? (No outdated decisions)
- [ ] **Single Source** – No duplicate information across docs?
- [ ] **Decision, Not Wish** – Every statement is a decision, not a hope?
- [ ] **Prompt-Ready** – Would you put every section in an AI prompt?
- [ ] **No Future State** – All "will eventually," "might," "ideally" language removed?
- [ ] **No Fluff** – All motivational/aspirational content removed?

#### Document Architecture Checks (6 items)

- [ ] **Type Identified** – Document type clearly marked? (Strategic vs Implementation vs Reference)
- [ ] **Anti-patterns Placed** – Anti-patterns in implementation docs only? (Strategic docs have pointers)
- [ ] **Test Cases Placed** – Test cases in implementation docs only? (Strategic docs have pointers)
- [ ] **Error Handling Placed** – Error handling matrix in implementation docs only?
- [ ] **Deep Links Present** – Deep links in ALL documents? (No vague "see elsewhere")
- [ ] **No Duplicates** – Strategic docs use pointers, not duplicate content?

### AI Coder Understandability Scoring

**Score your documentation on 6 criteria:**

| Criterion | Weight | 10/10 = |
|-----------|--------|---------|
| **Actionability** | 25% | Every section has implementation implication |
| **Specificity** | 20% | All numbers concrete, all thresholds explicit |
| **Consistency** | 15% | Single source of truth, no duplicates |
| **Structure** | 15% | Tables over prose, clear hierarchy |
| **Disambiguation** | 15% | Anti-patterns present (5+), edge cases explicit |
| **Reference Clarity** | 10% | Deep links only, no vague references |

**Score Interpretation:**

| Score | Meaning | Action |
|-------|---------|--------|
| 10/10 | AI can implement with zero questions | Proceed to Phase 3 |
| 9/10 | 1 minor clarification needed | Fix, then proceed |
| 7-8/10 | 3-5 ambiguities exist | Major revision required |
| <7/10 | Not AI-ready, fundamental issues | Return to Phase 2 |

---

## PHASE 3: EXECUTION (15% of time)

### The Generate-Verify-Integrate Loop

```
1. GENERATE: Feed spec to AI → Receive code
2. VERIFY: Run tests → Check against spec
   - Does output match spec exactly?
   - Yes → Continue
   - No → Fix SPEC first, then regenerate
3. INTEGRATE: Commit → Update documentation if needed
```

### The Golden Rule

> **"When code fails, fix the spec—not the code."**

If generated code doesn't work:
1. ❌ Don't patch the code manually
2. ✅ Ask: "What was unclear in my spec?"
3. ✅ Fix the spec
4. ✅ Regenerate

**Why?** Manual code patches create **Divergence** between spec and reality. Divergence is technical debt that breaks the stream.

---

## PHASE 4: QUALITY & ITERATION (5% of time)

### The Rule of Divergence

> **Every time you manually edit AI-generated code without updating the spec, you create Divergence. Divergence is technical debt.**

**Why Divergence is Dangerous:**
- If you fix a bug in code but not spec, you can never regenerate that module
- Future AI iterations will reintroduce the bug
- You've broken the stream

### Preventing Divergence

| Scenario | ❌ Wrong | ✅ Right |
|----------|----------|----------|
| Bug in generated code | Fix code manually | Fix spec, regenerate |
| Missing edge case | Add code patch | Add to spec, regenerate |
| Performance issue | Optimize code | Document constraint, regenerate |
| "Quick fix" needed | "Just this once..." | No. Fix spec. |

### Day 2 Workflow

1. **Isolate the Module** – Target the specific module, not the whole app
2. **Update the Spec** – Add the new edge case, requirement, or fix
3. **Regenerate the Module** – Feed updated spec to AI
4. **Verify Integration** – Run test suite for regressions

This takes 5 minutes longer than a quick hotfix. But it ensures your documentation never drifts from reality.

---

## Integration with Cosmic Python

Stream Coding is **methodology and strategy** (WHAT to build, HOW to plan).
Cosmic Python is **architecture and execution** (HOW to structure code, HOW to test, HOW to maintain quality).

**Together:**

```
Stream Coding Phase 1     → Cosmic Python: Architectural Decisions (ADRs)
Stream Coding Phase 2     → Cosmic Python: Layers, Interfaces, Testing approach
Stream Coding Phase 3     → Cosmic Python: Code generation follows layer rules
Stream Coding Phase 4     → Cosmic Python: Maintain boundaries, run quality gates
```

When integrating:
1. **Phase 1 (Stream)**: Answer 7 Questions. For architecture decisions, reference Cosmic Python layer patterns
2. **Phase 2 (Stream)**: Write specs. Ensure they specify Cosmic Python layers (models, adapters, services, entrypoints)
3. **Phase 3 (Stream)**: Generate code. Code should naturally follow Cosmic Python patterns
4. **Phase 4 (Stream)**: Prevent divergence. Update specs when adding features, code regenerates with correct architecture

---

## The Stream Coding Contract

### YOU MUST:

**Documentation Audit (if existing docs):**
- [ ] Run Clarity Test on all existing documentation
- [ ] Remove aspirational/future state language
- [ ] Consolidate duplicates to single source
- [ ] Target 40-50% reduction without losing actionable content

**Phase 1:**
- [ ] Answer all 7 questions at "Require" level
- [ ] Create Strategic Blueprint with Implementation Implications
- [ ] Write ADRs for major architectural decisions
- [ ] Document which Cosmic Python patterns apply

**Phase 2:**
- [ ] Write implementation specs with all 4 mandatory sections
- [ ] Include anti-patterns (5+ per doc)
- [ ] Include test case specifications (5 unit + 3 integration minimum)
- [ ] Include error handling matrix
- [ ] Include deep links (no vague references)

**Clarity Gate:**
- [ ] All 13 items checked
- [ ] Documentation scores 9+/10 on understandability
- [ ] Ready for Phase 3 before generating code

**Phase 3:**
- [ ] Generate code from spec
- [ ] Run tests immediately
- [ ] If tests fail: fix SPEC, not code
- [ ] Commit spec + code together

**Phase 4:**
- [ ] Never manually patch AI-generated code
- [ ] Always update spec first
- [ ] Regenerate from updated spec
- [ ] Prevent divergence obsessively

---

## Key Differences: Stream Coding vs Traditional Development

| Aspect | Traditional | Stream Coding |
|--------|-------------|---------------|
| **Planning** | Loose, exploratory | Rigorous, comprehensive |
| **Documentation** | Afterthought | Mandatory, phase-gated |
| **Code** | Source of truth | Output of specs |
| **AI role** | Code suggestion | Code generation |
| **Rework** | 40-50% of time | <10% of time |
| **Debugging** | Code-first | Spec-first |
| **Quality gates** | After code | Before code |

---

## Summary

Stream Coding fills the gap between **strategic thinking** and **technical execution**:

1. **Strategic thinking** (Phase 1) – Figure out WHAT to build
2. **Documentation** (Phase 2) – Spec HOW to build it
3. **Execution** (Phase 3) – AI generates code automatically
4. **Maintenance** (Phase 4) – Prevent divergence, keep spec = reality

**When combined with Cosmic Python:**
- Stream Coding tells you WHAT and HOW to plan
- Cosmic Python tells you HOW to structure the code correctly
- Together: methodical planning + clean architecture = 10-20x velocity

**The core belief:** Documentation is not a step toward coding. Documentation IS the product. Code is just the compiled output.
