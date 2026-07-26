# Data mappings & integration

## What it is

Most organisations already hold their data in several places: a CRM, a spreadsheet somebody
maintains by hand, an old database nobody wants to touch, a partner's system reached over an API.
Data mappings & integration is the work of connecting those existing sources into the shared
semantic model (see [modelling / ontology](semantic-ontology-modelling.md)), so that a record in one
system and a record in another can be recognised as the same thing, or correctly related, without a
person doing that reconciliation by hand every time.

## The problem it solves

Without this, "combine the data" means somebody exporting spreadsheets and matching rows by eye, an
error-prone job that has to be repeated every time the data changes. A client who has already invested
in modelling their domain still can't get value from it if their real, messy, pre-existing data never
gets connected to that model. This service exists to close that gap: to turn "the model" and "the
existing systems" into one connected picture instead of two things that describe the same
organisation but never actually meet.

## What's included

**This block currently has no owning skill.** `semantic-consulting-coach`'s service-family list
already names "data mapping & interoperability" as something Meaningfy sells (see
[`semantic-consulting-coach`](../../../skills/semantic-consulting-coach/SKILL.md)), but nothing in this
catalogue yet codifies how that work gets scoped, built, or quality-checked. Until such a skill
exists, the block is delivered as bespoke engineering, scoped case by case and following the general
software-development practice (see [software-development.md](software-development.md)) rather than
any purpose-built mapping method.

## What you get (deliverable)

Not yet standardised. Once a mapping/integration engineering skill exists, this section states the
concrete artefact (e.g. a mapping specification plus the running pipeline that executes it). Today,
the deliverable is whatever is agreed case by case in the engagement's Decision Package.

## Owning skill(s)

**No owning skill exists.** A search of every skill under `skills/` for data-mapping, integration, or
ETL-specific content found none (a genuine gap, not an oversight). The nearest adjacent skills,
[`cosmic-python`](../../../skills/cosmic-python/SKILL.md) and
[`architecture`](../../../skills/architecture/SKILL.md), would structure the *code* that carries out
this work, but neither one owns the mapping method itself: knowing how to layer a pipeline isn't the
same as knowing how to design the mapping it executes.

## Where it fits

Data mappings & integration is one of the six building blocks the Semantic Layer decomposes into;
see
[`engagement-lifecycle.md#the-outcome-semantic-layer-adoption`](../engagement-lifecycle.md#the-outcome-semantic-layer-adoption).
A client can still buy and receive this block today; the missing piece is a dedicated method, not
the willingness to deliver it.
