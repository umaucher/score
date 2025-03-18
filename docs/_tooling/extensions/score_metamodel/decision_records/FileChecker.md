# Idea: Define tests for the metamodel in .rst files instead of in python files

Instead of writing lots and lots of unit tests, we could define the tests in a more human-readable format.
This would allow us to:
* Run this file through sphinx and check the output
* Run this file as a unit test replacement

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

```rst
.. test:: parent need
   :id: feat_req__2
   :status: draft

#EXPECT: id is not lower case
#EXPECT: has a parent requirement(s): `feat_req__2` with an invalid status.
.. test:: need for testing
   :id: TOOL_REQ__1
   :status: valid
   :satisfies: feat_req__2
```

Approach:
* Parse this .rst file
* Optionally remove all lines starting with #
* Start sphinx
* Compare stdout with the expected output

Idea:
* Either parse the file in python (trivial) or use https://llvm.org/docs/CommandGuide/FileCheck.html


### Considered alternatives

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
