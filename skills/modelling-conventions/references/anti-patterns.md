# Modelling anti-patterns

Representation-agnostic smells. Each is a signal that meaning is leaking out of the model into code,
strings, or a single overloaded class. When you see one, stop and fix the model.

## Free strings where a controlled set belongs

A property whose values are drawn from a closed set modelled as a bare string. The set then lives
implicitly in whatever code compares against it (`if kind == "resource"`), and no two consumers agree
on the spelling.

**Fix:** model the set as an enumeration; every value is a stable key with its own definition (and a
`meaning:` URI where a published vocabulary has one). No semantic label should exist only as a raw
string literal.

## God-class

One class accreting every attribute in sight because "it's all about the order". It has no cohesion, its
name stops predicting its contents, and every consumer depends on all of it.

**Fix:** split by cohesion into smaller classes and value objects; factor shared attributes into
reusable properties (see [`naming-and-identity.md`](naming-and-identity.md)).

## Validation buried in code, not the model

Cardinality, required-ness, numeric bounds, patterns, and uniqueness expressed only in hand-written
validators. The model looks permissive; the real contract is scattered and drifts from it.

**Fix:** put the constraint in the model (required, multivalued, bounds, pattern, unique keys). The
model is the contract; code enforces what the model declares, it does not invent new rules.

## Attributes redefined per class instead of reused

The same attribute (same meaning) copy-pasted onto several classes. Change its meaning and you must find
every copy.

**Fix:** the reusable-property principle — define once, reference everywhere.

## Identity as an afterthought

Elements with no stable identity, or identity encoded from mutable facts (a version number or file path
in the local name). Rename or move the element and every reference breaks; a semantic target cannot be
generated cleanly.

**Fix:** the URI-everywhere principle — mint stable, opaque identity at authoring time, implicit by
default.

## Missing definitions

Classes and properties with names but no prose definition. The model is unusable as ubiquitous language
and the generated docs/contracts ship empty descriptions.

**Fix:** every class and property gets a real, prose definition — treat it as documentation that ships,
not a formality.

## Flattening a value object into loose properties

A composite concept (an address, a version range, a money amount) spread as loose sibling properties on
a parent class, so its identity and invariants can't be expressed.

**Fix:** model it as its own small class with its own identity and uniqueness rules; reference it.
