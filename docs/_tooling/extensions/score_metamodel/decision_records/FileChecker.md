# Idea: Define tests for the metamodel in .rst files instead of in python files

Instead of writing lots and lots of unit tests, we could define the tests in a more human-readable format.
This would allow us to:
* Run this file through sphinx and check the output
* Run this file as a unit test replacement
* Allow process experts to read the tests
* Allow process experts to write the tests!!

Scope:
* Testing warnings (or absence of warnings) in the sphinx output
* Nothing else!!

## References

* [FileCheck](https://llvm.org/docs/CommandGuide/FileCheck.html)
* [Example of FileCheck](https://github.com/llvm/llvm-project/blob/main/clang-tools-extra/test/clang-tidy/checkers/bugprone/chained-comparison.cpp)


## Comparison

### Current approach

```python
def test_check_linkage_status_positive(self):
    logger = tests.fake_check_logger()
    app = Mock(spec=Sphinx)

    need_1 = NeedsInfoType(
        id="TOOL_REQ__1",
        status="valid",
        satisfies=[
            "feat_req__2",
        ],
    )

    need_2 = NeedsInfoType(
        id="feat_req__2",
        status="valid",
    )
    needs = [need_1, need_2]

    check_linkage_status(app, needs, logger)
    logger.assert_no_warnings()
```

Obviously we can optimize the above code a little bit, but the idea is to have a human-readable format that is easy to understand.
The above code will never be readable or even writeable by a non-programmer.


### Proposal

Hint: `#EXPECT` always applies to the next line without an `#` prefix.

```rst
#EXPECT-NOT: id is not lower case
.. stkh_req:: parent need
   :id: feat_req__2
   :status: draft

#EXPECT: id is not lower case
#EXPECT: has a parent requirement(s): `feat_req__2` with an invalid status.
.. stkh_req:: need for testing
   :id: TOOL_REQ__1
   :status: valid
   :satisfies: feat_req__2

-------------------------

no technical assurance that test cases don't interfere with each other!

#EXPECT: status is missing
.. stkh_req:: another need
   :id: TOOL_REQ__2

---

#EXPECT-NOT: status is missing
.. stkh_req:: another need
   :id: TOOL_REQ__3

.. needextend::
   :id: TOOL_REQ__3
   :status: valid
```

Approach:
* Parse this .rst file
* Optionally remove all lines starting with #
* Start sphinx
* Compare stdout with the expected output

Idea:
* Either parse the file in python (trivial) or use https://llvm.org/docs/CommandGuide/FileCheck.html


### Considered alternatives

#### Refactor the test code
However much we try, the test code will never be as readable as a human-readable format.

#### Use a different test framework
e.g. Cucumber was designed specifically for this purpose, but it is not a good fit for our needs. Cucumber is designed for BDD and not for testing a metamodel.


#### EXPECT attribute

Approach:
* We create .rst test files, with an on-demand sphinx project.
* We load the normal metamodel and extend it on the fly with an EXPECT attribute.
* We use a mock-logger, or a real logger, and compare the output with the expected output.

```rst
.. test:: parent need
   :id: feat_req__2
   :status: draft

.. test:: child need
   :id: TOOL_REQ__1
   :status: valid
   :satisfies: feat_req__2
   :EXPECT: has a parent requirement(s): `feat_req__2` with an invalid status., id is not lower case
```

However
* this proposal Problem with multiple EXPECT lines, see above!
* Changing the metamodel, or even mocking logging is a strange test level. It's not a unit test and not a black box product test.


#### Use content

Approach:
* We create .rst test files, with an on-demand sphinx project.
* We use a mock-logger, or a real logger, and compare the output with the expected output.


```rst
.. test:: parent need
   :id: feat_req__2
   :status: draft

.. test:: child need
   :id: TOOL_REQ__1
   :status: valid
   :satisfies: feat_req__2

   EXPECT: has a parent requirement(s): `feat_req__2` with an invalid status.
   EXPECT: id is not lower case
```


However
* Some tests may want to test the content of needs, which will be confusing
* Changing the metamodel, or even mocking logging is a strange test level. It's not a unit test and not a black box product test.
