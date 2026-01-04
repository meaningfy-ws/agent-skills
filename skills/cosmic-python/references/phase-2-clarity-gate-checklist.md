# Phase 2: AI-Ready Documentation & Clarity Gate Checklist

**Duration:** 40% of total project time
**Goal:** Write specifications so clear that code generation becomes automatic
**Gate:** Clarity Gate (13 items) must pass before Phase 3

---

## Phase 2 Overview: The 4 Mandatory Sections

Every implementation document MUST include these 4 sections. Without them, AI guesses—and guesses create rework.

---

## Section 1: Anti-Patterns (DO NOT)

**Purpose:** AI needs to know what NOT to do. Prevents hallucination and bad patterns.

**Minimum:** 5 anti-patterns per implementation document

**Format:** Table with concrete examples

**Checklist:**

- [ ] **5+ anti-patterns identified** for this module/component
- [ ] **Each has 3 columns:**
  - What NOT to do
  - What to do instead
  - Why (the consequence of doing it wrong)
- [ ] **Anti-patterns are specific to THIS module**, not generic
- [ ] **Examples are concrete**, not abstract (e.g., "Store timestamps as Date objects" not "Use proper data types")
- [ ] **Every row addresses a real risk** in this codebase

**Template:**

```markdown
## Anti-Patterns (DO NOT)

| ❌ Don't | ✅ Do Instead | Why |
|----------|---------------|-----|
| [Concrete anti-pattern] | [Correct approach] | [Consequence of wrongness] |
| [Concrete anti-pattern] | [Correct approach] | [Consequence of wrongness] |
| [Concrete anti-pattern] | [Correct approach] | [Consequence of wrongness] |
| [Concrete anti-pattern] | [Correct approach] | [Consequence of wrongness] |
| [Concrete anti-pattern] | [Correct approach] | [Consequence of wrongness] |
```

**Examples that work:**

✅ "Store timestamps as Date objects" → "Use ISO 8601 strings" → "Date serialization varies by timezone"
✅ "Hardcode API endpoints" → "Use config env vars" → "Endpoint changes require code restart"
✅ "Skip input validation on internal APIs" → "Validate everything" → "Internal bugs cascade to production"

**Examples that don't work:**

❌ "Use bad code" → "Use good code" (too vague)
❌ "Don't be inefficient" → "Be efficient" (subjective)
❌ "Avoid bugs" → "Write tests" (doesn't explain the specific anti-pattern)

---

## Section 2: Test Case Specifications

**Purpose:** AI needs concrete verification criteria. Testable specs prevent assumptions.

**Minimum:** 5 unit tests + 3 integration tests per component

**Format:** Detailed tables with inputs, outputs, edge cases

**Checklist:**

- [ ] **5+ unit test specifications** defined
- [ ] **3+ integration test specifications** defined
- [ ] **Each test has:**
  - Test ID (TC-001, TC-002, etc.)
  - Component/system being tested
  - Input (what goes in)
  - Expected output (what should come out)
  - Edge cases (boundary conditions)
- [ ] **Edge cases explicitly named** (not left to AI to discover)
- [ ] **Tests cover both happy path AND error cases**

**Template:**

```markdown
## Test Case Specifications

### Unit Tests Required

| Test ID | Component | Input | Expected Output | Edge Cases |
|---------|-----------|-------|-----------------|------------|
| TC-001 | [Component] | [Specific input] | [Exact output] | [Empty, null, boundary values] |
| TC-002 | [Component] | [Specific input] | [Exact output] | [Edge condition 1, 2, 3] |
| TC-003 | [Component] | [Specific input] | [Exact output] | [Edge condition 1, 2, 3] |
| TC-004 | [Component] | [Specific input] | [Exact output] | [Edge condition 1, 2, 3] |
| TC-005 | [Component] | [Specific input] | [Exact output] | [Edge condition 1, 2, 3] |

### Integration Tests Required

| Test ID | Flow | Setup | Verification | Teardown |
|---------|------|-------|--------------|----------|
| IT-001 | [System flow] | [Create test conditions] | [What proves it worked?] | [Clean up test data] |
| IT-002 | [System flow] | [Create test conditions] | [What proves it worked?] | [Clean up test data] |
| IT-003 | [System flow] | [Create test conditions] | [What proves it worked?] | [Clean up test data] |
```

**Examples that work:**

✅ TC-001: Tier classifier | Input: 100 contacts | Output: 20-30 in Critical tier | Edge: empty list, all same score
✅ IT-001: Auth flow | Setup: Create test user | Verify: Token refresh works | Teardown: Delete test user

**Examples that don't work:**

❌ TC-001: Component | Input: valid data | Output: correct | Edge: various
❌ IT-001: System | Setup: data | Verify: working | Teardown: cleanup

---

## Section 3: Error Handling Matrix

**Purpose:** AI needs to know how to handle every failure mode. Prevents silent failures.

**Minimum:** All external services + all user-facing errors

**Format:** Separate matrices for external and user-facing errors

**Checklist:**

- [ ] **External Service Errors matrix complete** (all services listed)
  - [ ] Error type identified
  - [ ] Detection method specified
  - [ ] Response specified (what code does)
  - [ ] Fallback specified (if response fails)
  - [ ] Logging level specified
  - [ ] Alert condition specified (when ops should be notified)
- [ ] **User-Facing Errors matrix complete**
  - [ ] Error type identified
  - [ ] User message specified (exact text)
  - [ ] Error code specified (HTTP status or custom code)
  - [ ] Recovery action specified (what user does next)

**Template:**

```markdown
## Error Handling Matrix

### External Service Errors

| Error Type | Detection | Response | Fallback | Logging | Alert |
|------------|-----------|----------|----------|---------|-------|
| [Error] | [How detected?] | [What code does] | [Plan B] | [Log level] | [Alert condition] |
| [Error] | [How detected?] | [What code does] | [Plan B] | [Log level] | [Alert condition] |

### User-Facing Errors

| Error Type | User Message | Code | Recovery Action |
|------------|--------------|------|-----------------|
| [Error] | "[Exact text user sees]" | [HTTP code or custom] | [What user does] |
| [Error] | "[Exact text user sees]" | [HTTP code or custom] | [What user does] |
```

**Examples that work:**

✅ Error: API timeout | Detection: >5s response | Response: Retry 3x exponential backoff | Fallback: Return cached data | Logging: ERROR | Alert: If 3 in 5 min
✅ Error: Quota exceeded | Message: "You've used all checks this month" | Code: 403 | Recovery: Show upgrade CTA

**Examples that don't work:**

❌ Error: Network error | Detection: Error happens | Response: Handle it | Fallback: Do something | Logging: Log it
❌ Error: Bad input | Message: "Error" | Code: 400 | Recovery: Try again

---

## Section 4: Deep Links (All Documents)

**Purpose:** AI needs to navigate to exact locations. "See Technical Annexes" wastes time.

**Minimum:** Every reference has document path + section anchor

**Checklist:**

- [ ] **No vague references** like "see elsewhere", "technical details in separate doc"
- [ ] **Every reference has:**
  - Exact document path (e.g., `../specs/api.md`)
  - Section anchor/header (e.g., `#authentication`)
- [ ] **Reference format:** [Readable Name](../path/to/file.md#anchor)
- [ ] **All referenced sections exist** (no broken links)

**Template:**

```markdown
## References

### Schema References
| Topic | Location | Anchor |
|-------|----------|--------|
| [Entity name] | [../path/to/schema.md](../path/to/schema.md) | [#anchor] |
| [Entity name] | [../path/to/schema.md](../path/to/schema.md) | [#anchor] |

### Implementation References
| Topic | Document | Section |
|-------|----------|---------|
| [Topic] | [API Spec](../specs/api.md) | [#section-anchor](../specs/api.md#section-anchor) |
| [Topic] | [Auth Spec](../specs/auth.md) | [#section-anchor](../specs/auth.md#section-anchor) |

### Related Modules
| Related Component | Location |
|------------------|----------|
| [Module name] | [../services/module.md](../services/module.md) |
| [Module name] | [../services/module.md](../services/module.md) |
```

**Examples that work:**

✅ "User profiles" → `[Schema Ref](../schemas/schema.md#user_profiles)`
✅ "Auth flow" → `[API Spec](../specs/api.md#authentication)`

**Examples that don't work:**

❌ "See the schema file"
❌ "Error handling in the other doc"
❌ "Reference the implementation guide"

---

## THE CLARITY GATE (13 Items - MANDATORY)

⛔ **NEVER SKIP THIS GATE.** This is the difference between stream coding and vibe coding.

### Part A: Foundation Checks (7 items)

- [ ] **1. Actionable** – Does every section dictate a specific implementation detail? (No aspirational like "fast" or "scalable")
- [ ] **2. Current** – Is everything up-to-date? (No outdated decisions or old decisions still listed)
- [ ] **3. Single Source** – No duplicate information across docs? (Each decision documented once)
- [ ] **4. Decision, Not Wish** – Every statement is a decision, not a hope? (Not "we might", "we'll eventually", "ideally")
- [ ] **5. Prompt-Ready** – Would you put every section in an AI prompt? (If you wouldn't feed it to AI, delete it)
- [ ] **6. No Future State** – All "will eventually", "might", "ideally" language removed? (This is current state only)
- [ ] **7. No Fluff** – All motivational/aspirational content removed? (No "we believe in excellence" type language)

### Part B: Document Architecture Checks (6 items)

- [ ] **8. Type Identified** – Is each document clearly marked as Strategic, Implementation, or Reference?
- [ ] **9. Anti-patterns Placed** – Anti-patterns in implementation docs only? (Strategic docs reference them, don't duplicate)
- [ ] **10. Test Cases Placed** – Test specs in implementation docs only? (Strategic docs reference them)
- [ ] **11. Error Handling Placed** – Error matrix in implementation docs only? (Strategic docs reference it)
- [ ] **12. Deep Links Present** – Deep links in ALL documents? (No vague "see elsewhere" references)
- [ ] **13. No Duplication** – Strategic docs use pointers, not duplicate content from implementation docs?

### Gate Enforcement

```
- [ ] All 7 Foundation Checks pass
- [ ] All 6 Document Architecture Checks pass
- [ ] AI Coder Understandability Score ≥ 9/10

If ANY item fails → Fix before proceeding to Phase 3
```

---

## AI Coder Understandability Scoring

Score your documentation on 6 criteria. **Target: 9+/10 before Phase 3.**

### The 6-Criterion Rubric

| Criterion | Weight | 10/10 Means |
|-----------|--------|-------------|
| **Actionability** | 25% | Every section has specific implementation implication |
| **Specificity** | 20% | All numbers concrete, all thresholds explicit, no "etc" |
| **Consistency** | 15% | Single source of truth, no duplicates across docs |
| **Structure** | 15% | Tables over prose, clear hierarchy, predictable format |
| **Disambiguation** | 15% | Anti-patterns present (5+), edge cases explicit |
| **Reference Clarity** | 10% | Deep links only, no vague references |

### Score Interpretation

| Score | Meaning | Action |
|-------|---------|--------|
| 10/10 | AI can implement with zero clarifying questions | ✅ Proceed to Phase 3 |
| 9/10 | 1 minor clarification needed | Fix, then proceed |
| 7-8/10 | 3-5 ambiguities exist | Major revision required |
| <7/10 | Fundamental issues, not AI-ready | Return to Phase 2 |

### Self-Assessment Questions

Before Phase 3, ask yourself:

1. **Actionability:** "Does every section tell AI exactly what to do?"
2. **Specificity:** "Are there any numbers I left vague? Any 'etc' or 'etc'?"
3. **Consistency:** "Is any information stated in more than one place?"
4. **Structure:** "Could I convert any prose paragraphs to tables?"
5. **Disambiguation:** "Have I listed at least 5 anti-patterns per implementation doc?"
6. **Reference Clarity:** "Do any references say 'see elsewhere' without exact location?"

**If you answer "no" to ANY question that should be "yes":** Fix before proceeding.

---

## Phase 2 Deliverables Checklist

For each MVP feature and major system component:

- [ ] **Implementation Spec created** (not just a summary, an actual detailed spec)
- [ ] **Section 1: Anti-patterns** – 5+ specific, concrete anti-patterns
- [ ] **Section 2: Test Cases** – 5+ unit tests + 3+ integration tests
- [ ] **Section 3: Error Handling** – All external services + all user-facing errors
- [ ] **Section 4: Deep Links** – Exact document paths + section anchors
- [ ] **All 13 Clarity Gate items** checked and passing
- [ ] **AI Coder Score** ≥ 9/10
- [ ] **Validated by self-assessment questions** above

---

## Common Phase 2 Mistakes

❌ **Mistake 1:** Listing anti-patterns too generically
✅ **Fix:** Every anti-pattern should be specific to THIS module (e.g., "In the scheduler service, don't hardcode timeouts")

❌ **Mistake 2:** Forgetting edge cases in test specs
✅ **Fix:** For every test, list what breaks it: empty inputs, null values, boundary cases

❌ **Mistake 3:** Vague error messages
✅ **Fix:** "What is the EXACT text the user sees?" If you can't answer, be more specific

❌ **Mistake 4:** References without locations
✅ **Fix:** "See schema.md" is useless. "[See user schema](../schemas/schema.md#user)" is useful

❌ **Mistake 5:** Duplicating content between strategic and implementation docs
✅ **Fix:** Strategic doc says "See [Implementation](../specs/api.md#error-handling)" — no duplication

---

## Cosmic Python Integration Note

As you write Phase 2 specs, keep Cosmic Python architecture in mind:

- **Models section** → Domain logic (no I/O), validation rules, error types
- **Adapters section** → Infrastructure integration (external services, databases, APIs)
- **Services section** → Orchestration of adapters and models (error handling, retry logic goes here)
- **Entrypoints section** → User-facing APIs (CLI, HTTP, schedulers)
- **Test specs** → One test per layer (models, adapters, services, entrypoints)

When writing anti-patterns, test cases, and error handling, reference which Cosmic Python layer each applies to.

---

## Phase 2 Exit Criteria

- [ ] All MVP features have implementation specs
- [ ] All 4 mandatory sections complete per spec
- [ ] All 13 Clarity Gate items pass
- [ ] AI Coder score ≥ 9/10
- [ ] Self-assessment questions answered correctly
- [ ] Strategic and Implementation docs properly separated (no duplication)
- [ ] All references are deep links (not vague pointers)
- [ ] Ready for Phase 3 (code generation can proceed)

---

## Next: Phase 3

Once Clarity Gate passes:

1. Feed Phase 2 specs to AI (Claude Code, Cursor, or other tool)
2. Generate code for each component
3. Run tests immediately (they're specified in Phase 2)
4. If tests fail: **Fix the SPEC, not the code**
5. Regenerate from updated spec

**Golden Rule:** "When code fails, fix the spec—not the code."

---

## Clarity Gate Failure Recovery

If you score <9/10, here's how to fix:

| Issue | Fix |
|-------|-----|
| Actionability <25% | Add "Implementation Implication" to every section |
| Specificity <20% | Find vague words ("etc", "handle", "fast") and replace with numbers/concrete actions |
| Consistency <15% | Search for duplicates, consolidate to single source, add references instead |
| Structure <15% | Convert prose paragraphs to tables where possible |
| Disambiguation <15% | Add 5 anti-patterns if missing, explicitly list edge cases |
| Reference Clarity <10% | Replace vague references with deep links: `[text](../path/file.md#anchor)` |

After fixes, re-score. Don't proceed to Phase 3 until 9+/10.

---

*Checklist based on Stream Coding v3.4 by Francesco Marinoni Moretto. See github.com/frmoretto/stream-coding*
