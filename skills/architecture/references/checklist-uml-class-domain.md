# UML Class Diagram Checklist – Domain & Conceptual Models

Use this checklist when validating or creating a UML Class diagram for domain concepts and data structures (L4).

## Scope & Purpose
- [ ] Diagram represents domain concepts (what the business cares about)
- [ ] NOT: implementation classes, technical infrastructure, or design patterns
- [ ] Focus: entities, value objects, relationships that matter to the business
- [ ] This should be expressible in LinkML (our canonical data definition language)

## Classes = Domain Concepts
- [ ] Each class represents a business entity or value object
- [ ] Class names are business-meaningful ("Customer", "Entity", "Order")
- [ ] NOT: technical names ("UserDTO", "DatabaseRecord", "ServiceImpl")
- [ ] Classes describe what exists, not how it's implemented
- [ ] No infrastructure/framework details in class names

## Attributes = Business Semantics
- [ ] Attributes represent meaningful properties (not database columns)
- [ ] Attribute names are business language ("email", "orderId", "resolvedAt")
- [ ] NOT: database jargon ("varchar_col_1", "id_seq", "ts_updated")
- [ ] NOT: infrastructure annotations visible (@Entity, @Column, @Id)
- [ ] Types are semantic ("Date", "Currency", "Status") not technical ("java.util.Date")
- [ ] Cardinality/optionality shown (required vs optional, collection vs single)

## Relationships & Associations
- [ ] Each association shows a meaningful business relationship
- [ ] Names describe relationship meaning ("orders to customer", "entity to resolution")
- [ ] Multiplicity is intentional and meaningful (1-to-1, 1-to-many, many-to-many)
- [ ] NOT: foreign key relationships (that's database design)
- [ ] NOT: implementation details (backreferences, cascade settings)
- [ ] Bidirectional associations are justified (does the business need both directions?)

## Inheritance & Hierarchies
- [ ] Inheritance used for genuine specialization (not technical abstraction)
- [ ] Example: "Customer" → "Individual Customer" vs "Corporate Customer"
- [ ] NOT: "Entity" → "PersistableEntity" → "AuditableEntity" (technical)
- [ ] Abstract classes are business concepts, not just interfaces
- [ ] Depth limited: 2-3 levels max (deeper suggests technical, not domain)

## What Must NOT Be Included
- ❌ Database tables or persistence details
- ❌ ORM annotations (@Entity, @Table, @Column)
- ❌ Technical infrastructure (Serializable, @Override methods)
- ❌ Design patterns as classes (Adapter, Factory, Strategy)
- ❌ Implementation concerns (getters/setters, equals(), hashCode())
- ❌ Lifecycle methods (onCreate, onUpdate, onDelete)
- ❌ Framework-specific attributes (Spring beans, JPA fields)
- ❌ Storage concerns (schema names, indexes, partitions)

## Expressibility in LinkML
- [ ] Can each class be expressed as a LinkML "Class"?
- [ ] Can each relationship be expressed in LinkML?
- [ ] Are enumerations/value sets definable?
- [ ] Could this schema be shared with non-technical stakeholders?
- [ ] Is it independent of any specific technology?

## Red Flags & Anti-Patterns
- ❌ Classes matching database tables exactly (e.g., "UserAccount" with "id", "created_ts")
- ❌ Technical superclasses ("BaseEntity", "Auditable", "Versionable")
- ❌ Methods beyond data definition (business logic, getters/setters)
- ❌ Annotations visible (@Entity, @JsonProperty, @RestResource)
- ❌ Multiple inheritance (suggests design pattern, not domain concept)
- ❌ Too many classes (> 15-20 suggests too much detail)
- ❌ Incomplete: missing key business concepts
- ❌ Too abstract: classes like "Thing", "Object", "Data"

## Validation Against Business Understanding
- [ ] Could non-technical stakeholders understand this diagram?
- [ ] Does it match their mental model of the business?
- [ ] Are all key business entities represented?
- [ ] Are critical relationships visible?
- [ ] Would a business person agree with the structure?

## Relationship to LinkML
- [ ] Is there a corresponding LinkML schema?
- [ ] Does this class diagram match the LinkML definition?
- [ ] Could this be auto-generated from LinkML?
- [ ] Are there differences? If so, why?

## Completeness Checks
- [ ] All entities that flow through architecture are here?
- [ ] Master data entities represented?
- [ ] Key relationships documented?
- [ ] Enumerations/controlled vocabularies shown?
- [ ] Temporal concerns (versioning, validity dates) visible?

## Questions to Ask
1. **Is this domain or technical?** Could a business person understand it?
2. **Why this inheritance?** Is it domain specialization or technical abstraction?
3. **Are all relationships needed?** Or are some just implementation details?
4. **Could I describe this in plain English?** If not, it's too technical.
5. **Does this match LinkML?** Should it be the source of truth?
6. **What's missing?** Key entities, relationships, value sets?
7. **Is this at the right level?** Too abstract (too few concepts) or too detailed (database schema)?
8. **Could this change per technology choice?** If yes, it's implementation, not domain.

## Example: Good vs Bad

### ❌ BAD (Too Technical)
```
UserAccount
  - id: Long (PK)
  - username: String (UK)
  - password_hash: String
  - created_ts: Timestamp
  - updated_ts: Timestamp
  - is_active: Boolean
  - role_id: Long (FK)

UserRole
  - id: Long (PK)
  - role_name: String
```

### ✅ GOOD (Domain Concept)
```
User
  - email: Email (unique identifier)
  - name: String
  - role: UserRole (enumeration: Admin, Analyst, Viewer)

Contact
  - email: Email
  - phone: PhoneNumber
  - address: Address
```
