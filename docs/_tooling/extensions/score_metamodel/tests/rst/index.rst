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
