..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

Bazel registry
##############

Documentation
**************

Description
===========

Score, as a multi repository projects requires a setup of it's own
registry, that will help managing the dependencies between various
parts.

The registry is located at:
https://github.com/eclipse-score/bazel_registry

In order to use it the following lines need to be added to the .bazelrc
file of a module:

.. code::

   common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
   common --registry=https://bcr.bazel.build

Score registry is set as first registry with the fallback to Bazel's
central registry for other open source modules.

References
==========

-  Bazel external dependency management:
   https://bazel.build/external/overview#bzlmod
-  Bazel central registry browser: https://registry.bazel.build/
-  Bzlmod usage examples:
   https://github.com/bazelbuild/examples/tree/main/bzlmod\
