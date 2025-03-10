# Decision Record: Use Ariadne for Code Generation (2)

## Summary

Based on [DR-ariande.md](DR-ariande.md), the code generator was removed. As so often in
live, you only miss something when it's gone. This decision record documents the
attempt to reintroduce of the Ariadne code generator.

It has not been completed, but is rather the next big step in this tool's development.

---

## Details

The generated schema models add *a lot of value* by providing:
* Type safety: Errors due to incorrect data structures are reduced.
* Auto-completion: IDE support improves while writing parsing logic.

Although this benefit is localized - it mainly helps within the parsing layer. It's a
significant improvement.

Example: At the moment the easiest approach to map response data to a Python object is
to print it, in order to see the structure. This is not ideal.
