# Decision Record: use ariande for code generation


## Alternatives

### v1 - Using the `manual` queries

It's not quite in a working state, but this is simply due to careless moving of files
and functions. You can still see all the code.

Basically it has the queries and manual code to parse those queries. It's a lot of
boilerplate.

### v2 - Using 'ariande' code generation

This is the approach I'm currently working on. The goal is to reduce manually written
code to a minimum.

We'll see whether it's actually better or not.

# Decision

## query-code
The generated query-code does not add any benefit. `run_query` in v1 was a 1-liner:

```python
fetch_all_elements(query=query_str, ...)
```

In v2 it's something like:

```python
fetch_all_elements(query=fetch_all_elements_query, ...)
```

## schema-code
The generated schema-code adds some benefit, as it provides type safety and auto-completion while writing the "parsers" as they were coined in v1.

However it's a rather localised benefit, as the schema-code is only used in the
"parsers".

# Conclusion

Ariande doesn't seem to be worth the extra complexity.

Revisit decision when:
* the schema-code is used in more places
* the schema-code is used in more complex ways

Opon revisiting investigate schema-only code generation by other tools.
e.g. via datamodel-code-generator.
