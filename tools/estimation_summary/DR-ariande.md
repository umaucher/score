# Decision Record: Use Ariadne for Code Generation

## Context

We need a way to interact with GitHub’s GraphQL API efficiently while keeping
maintenance overhead low. The goal is to minimize boilerplate code and improve type
safety without introducing unnecessary complexity.

Initially, a **manual approach** was used, where queries were written as strings, and
the results were manually parsed into Python data structures. This required a lot of
boilerplate code but gave full control over the API calls.

To improve this, **Ariadne Codegen** was introduced to generate query-code and
schema-based data models automatically. The hypothesis was that this would reduce manual
work and improve maintainability.

---

## Alternatives Considered

### Manual Queries
This version manually defines queries and parses responses. While it works, it requires
writing and maintaining a lot of boilerplate code. The main issues:
- Queries are **hardcoded as strings** in Python.
- Responses must be **manually parsed** into the correct data structures.
- Schema changes require **manual updates**.

### Using Ariadne Codegen
This approach leverages **Ariadne Codegen** to:
- **Automatically generate** Python methods for GraphQL queries.
- **Generate Pydantic-based schema models** for type safety.
- **Reduce boilerplate** by handling query execution and result parsing.

The main goal was to see if Ariadne Codegen simplifies query execution and reduces
maintenance costs.

---

## Conclusion

### Query Code

The generated query code does not provide significant benefits. Originally executing a
query was already a simple one-liner: `fetch_all_elements(query=query_str, ...)`. Using
Ariadne Codegen, it becomes: `fetch_all_elements(query=fetch_all_elements_query, ...)`.
The difference is minimal, and the additional complexity of generating query methods
does not justify its use.

### Schema Code
The generated schema models add some value by providing:
* Type safety: Errors due to incorrect data structures are reduced.
* Auto-completion: IDE support improves while writing parsing logic.

However, this benefit is localized—it mainly helps within the parsing layer but does not
impact the broader application structure.

### Summary
Ariadne Codegen does not seem worth the extra complexity for this use case.

When to Revisit the Decision:
* If the schema-generated models become more widely used across the project.
* If the schema-based models simplify more complex data structures.
* If the current parser approach becomes too cumbersome to maintain.

Next Steps:
* Explore schema-only code generation without query methods. Consider
  datamodel-code-generator as an alternative, since it focuses solely on schema
  generation without adding unnecessary query-handling complexity.
