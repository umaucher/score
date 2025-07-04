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

Key-Value-Storage
#################

.. document:: Persistency Key-Value-Storage
   :id: doc__persistency_kvs
   :status: valid
   :safety: ASIL_B
   :tags: feature_request, persistency_kvs

.. toctree::
   requirements/index.rst
   architecture/index.rst


Feature flag
============

To activate this feature, use the following feature flag:

``persistency_kvs``


Abstract
========

This feature request describes the key-value storage (KVS) that is needed by
applications to store either temporary or permanent data in an easy way that
conforms to most programming languages that provide a hash, hashmap, dictionary
or similar data structure. Access to the KVS is possible from any support
language through language specific interfaces.


Motivation
==========

The current solutions available mostly don't meet the specific needs of the
S-CORE project like storing specific datatypes without a BASE64 conversation or
having no rollback/replay feature. Also the integration into analysis tools is
simpler when the solution grows with the needs instead having to adapt existing
data structures through wrapppers. Especially in the focus of security it will
be possible to build a system that integrates the layers from scratch and
provide them as API to any language whilst still using Rust as the backend.

A main USP of the solution will be the integration of a tracing framework that
allows to understand how events also in the context of other events interact.

A key-value storage is used within many applications to store e.g.
configuration data and is therefore seen crucial for the Eclipse S-CORE
platform.


Rationale
=========

1. | Requirement 1: Multiple key-value storages per application
   | Solution: Allow each application to have multiple key-value storages (KVS) to enable data separation and different levels of security.
2. | Requirement 2: Update mechanism for KVS versions
   | Solution: Implement an update mechanism to ensure compatibility through updates and rollbacks of different KVS versions.
3. | Requirement 3: Language-agnostic KVS interface
   | Solution: Design a flexible interface that allows the KVS to be read and written from multiple programming languages, including C++, Rust, and others.
4. | Requirement 4: Default values for KVS
   | Solution: Configure the KVS to store default values for all keys, returning either the default value or an error if the key needs to be written first.
5. | Requirement 5: Simple data representation for KVS
   | Solution: Utilize a simple data representation, such as JSON or Cap'n Proto, that supports versioned up- and downgrading and is easily debuggable by developers.
6. | Requirement 6: KVS integrity checking
   | Solution: Ensure the KVS maintains a consistent state, providing either the currently stored data or the previous snapshot if data retrieval is not possible.

Backwards Compatibility
=======================

The API for the specific language tries to represent the language specific
implementation like hashmaps or dictionaries to be mostly backwards compatible
to already existing key-value-storage usage cases. Access without a safe error
handling path, like the array-operator in Rust which can panic, must be
avoided.


Security Impact
===============

Access to the key-value-storage would allow a malicious user to control the
behaviour of the device, so it must be secured to prevent unauthorized access.
To achieve this, debug access should only be provided when a debug firmware
image is installed.


Safety Impact
=============

The expected ASIL level is ASIL-B. To reach this goal we will apply the S-CORE
development process. Key elements of it are listed in the process descriptions
of safety management and safety analysis. In the safety analysis we will
analyze the impact of the feature.

 .. note::
    TODO: Link to safety analysis.

We use an iterative development process and apply results from the next steps
back to the feature request. For TinyJSON we will perform a software component
classification.

  .. note::
    TODO: Link to component classification.

To ensure the freedom of interference the feature key-value storage should not
be used within different processes.


License Impact
==============

   .. note::
      The key-value storage itself uses the Apache-2.0 license. Licenses of
      used libraries are need to be checked.


How to Teach This
=================
