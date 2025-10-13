..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************

.. doc_tool:: gtest
   :id: doc_tool__gtest
   :status: draft
   :version: v1.15.0
   :tcl: LOW
   :safety_affected: YES
   :security_affected: YES
   :realizes: PROCESS_wp__tool_verification_report
   :tags: tool_management

Googletest (gtest) Verification Report
======================================

Introduction
------------
Scope and purpose
~~~~~~~~~~~~~~~~~
GoogleTest (gtest) is a C++ testing framework developed by Google to support the creation
of robust, maintainable, and portable tests. It is designed to help developers write
better tests by offering a rich set of assertions, test fixtures, and test discovery
mechanisms. gtest supports unit, integration, and system-level testing and is compatible
with various platforms.

Inputs and outputs
~~~~~~~~~~~~~~~~~~
Inputs: Software sources (C++), Test sources (C++)
Outputs: Test binary, Test execution logs, test report (txt, json, xml).

Available information
~~~~~~~~~~~~~~~~~~~~~
- Official repository: https://github.com/google/googletest
- Official documentation: https://google.github.io/googletest
- API Reference: https://google.github.io/googletest/reference/testing.html
- Version: 1.15.0


Installation and integration
----------------------------
Installation
~~~~~~~~~~~~
Provided as part of baselibs (https://github.com/eclipse-score/baselibs/blob/main/MODULE.bazel).
Fetched from the Bazel Central Registry (BCR): https://registry.bazel.build/modules/googletest/1.15.0

Integration
~~~~~~~~~~~
Integrated in bazel.

Environment
~~~~~~~~~~~
Requires C++ compiler (gcc, qcc?) and bazel build environment.

Evaluation
----------
This section evaluates gtest for use in safety-related projects.


.. list-table:: gtest safety evaluation
   :header-rows: 1
   :widths: 5 10 40 10 30 20 10 10

   * - Use case Identification
     - Use case Description
     - Malfunctions
     - Impact on safety?
     - Impact safety measures available?
     - Impact safety detection sufficient?
     - Further additional safety measure required?
     - Confidence (automatic calculation)
   * - 1
     - Execute unit tests
     - Fails to load input files
        gtest fails to load provided file even if file is present and accessible.
     - yes
     - Check the log information of gtest
     - HIGH
     - no
     - high
   * - 2
     - Execute unit tests
     - Fails to write result to file
        gtest was not able to save results in file(s).
     - yes
     - Check the log information of gtest
     - HIGH
     - no
     - high
   * - 3
     - Execute unit tests
     - Fails to collect results of the test(s)
        gtest was not able to collect results of executed test.
     - yes
     - Verify the test plan and test report
     - HIGH
     - no
     - high
   * - 4
     - Execute unit tests
     - Fails to detect an existing error
         gtest fails to detect the presence of existing errors.
     - yes
     - gtest qualification, Review the unit test implementations
     - LOW
     - yes
     - low
   * - 5
     - Execute unit tests
     - Fails to execute the test
         gtest fails to execute specific test from the test plan
     - yes
     - Verify the test plan and test report
     - HIGH
     - no
     - high
   * - 6
     - Execute unit tests
     - Indicates presence of a non-existing error
         gtest indicates the presence of errors that do not exist.
     - no
     - /
     - HIGH
     - no
     - high
   * - 7
     - Execute unit tests
     - Produces wrong test report
         gtest fails to save correct test result in test report.
     - yes
     - Check unit test results and test report correctness
     - HIGH
     - no
     - high

.. list-table:: gtest security evaluation
   :header-rows: 1

   * - Use case Identification
     - Use case Description
     - Threats
     - Impact on security?
     - Impact security measures available?
     - Impact security detection sufficient?
   * - 1
     - TBD
     - TBD
     - TBD
     - TBD
     - HIGH

Result
~~~~~~
gtest requires qualification for use in safety-related software development according to ISO 26262.


**Optional Section for Tool Qualification**
-------------------------------------------
Based on method: validation of the software tool

Requirements and testing aspects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Requirements defined in project documentation.
Test cases defined in test plans.
Coverage documented via gcov.

Analysis perspective
~~~~~~~~~~~~~~~~~~~~
Architecture and safety/security analysis documented in qualification strategy:
