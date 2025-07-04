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

.. _time_feature:

Time
#############

.. document:: Time
   :id: doc__time
   :status: valid
   :safety: ASIL_B
   :realizes: wp__feat_request
   :tags: time, feature_request, change_management


.. .. toctree::
..    :hidden:

..    requirements.rst


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_time``


Abstract
========


Motivation
==========

Efficient and accurate time management is critical in automotive systems, affecting functionality, safety, and reliability across various applications. Time handling spans several layers, from synchronization with external time sources to the consistent use of logical time within in-vehicle software cycles. For this reason, the motivation section describes the context broadly, even if the actual feature request later focuses on a more specific scope.

External Time Synchronization
-----------------------------

.. figure:: _assets/timesync-external.drawio.svg
   :alt: External Time Synchronization
   :align: center

External time synchronization establishes a reference to a global time standard, such as UTC, through methods like GPS-based synchronization or backend servers accessed via cellular networks. These time sources are relevant for fleet-wide timestamping, telematics, and ensuring regulatory compliance (e.g., event logging, cybersecurity).

The details of external synchronization are out of scope for this request but are included to clarify the overall context.

In-Vehicle Time Synchronization
-------------------------------

.. figure:: _assets/timesync-vehicle.drawio.svg
   :alt: In-Vehicle Time Synchronization
   :align: center

Within the vehicle, synchronization ensures that all ECUs reference a consistent internal time. In modern architectures, this is achieved by designating a statically defined Time Grand Master, typically a zonal controller equipped with a fast-booting microcontroller and responsible for early vehicle functions such as key detection. This controller synchronizes with the external time source and propagates time over the in-vehicle network.

The synchronization protocols relevant here are primarily Ethernet-based. The focus lies on gPTP (IEEE 802.1AS) and the corresponding specifications in AUTOSAR Adaptive to ensure compatibility with existing ECUs. Syntonization, the alignment of clock frequency, is as essential as synchronization and must be supported to maintain long-term timing consistency.

Bridging between different network domains (e.g., Ethernet to CAN) is outside the scope of this feature. In the system context, the High-Performance Computer (HPC) is assumed to be a slave in the time distribution topology and connects via Ethernet to the grandmaster. Time synchronization within CAN segments, typically handled by zonal controllers, is not covered by this feature.

Clocks, Accuracy, and Reading Current Time
------------------------------------------

Modern software environments contain several types of clocks (or time bases), including:

* Local clocks, such as monotonic or steady clocks
* Synchronized clocks, aligned with a vehicle-wide or external time base
* Secure or authentic clocks, protected against tampering

Mixing clock types unintentionally can lead to non-deterministic behaviors, negatively affecting system stability and correctness. Therefore, explicit selection of the time base by the application is mandatory.

Applications must be able to detect when a chosen time base is invalid or unsynchronized, enabling them to define appropriate fallback or error-handling strategies. Error states or drift conditions must be detectable by the application.

Clock introspection capabilities are required, allowing applications to determine synchronization status and time elapsed since the last successful synchronization. This information is vital during error handling or fallback situations.

Access to timestamps should be as performant as technically feasible due to their frequent use in control loops and high-frequency applications. Although specific latency targets are not defined here, low latency is a fundamental design consideration.

For cryptographic scenarios the feature also targets secure or authentic clocks. In such cases, a tamper-resistant time source is needed to ensure that time cannot be rolled back to re-enable expired certificates or bypass security controls. Authentic clocks might be signed or verified using hardware security modules.

To integrate cleanly with modern programming languages, the time access API should align with idiomatic constructs (e.g., ``std::chrono`` in C++, ``time`` in Rust), while making clear that the source of time is provided by the S-CORE platform. A dedicated namespace such as ``score::chrono`` may wrap native types to make the time source explicit.

Consistent Logical Time Within Cause-Effect Cycles
--------------------------------------------------

.. figure:: _assets/timesync-chain.drawio.svg
   :alt: Consistent Logical Time Within Cause-Effect Cycles
   :align: center

In distributed automotive applications, control logic is often structured into cause-effect chains. These chains consist of multiple interdependent tasks executing concurrently. Within each cycle of these chains, it is critical that all tasks perceive the same logical timestamp, even if their execution occurs at different actual CPU times.

Sharing a consistent logical timestamp ensures deterministic computations. For instance, integrating sensor measurements such as speed over time into position data requires stable and jitter-resilient timestamps shared across tasks. Additionally, consistent logical time enables reproducibility in testing, simulation, and validation scenarios, as the sequence and timing of events can be reliably replayed.

Logical time must be explicitly provided to the tasks within these cause-effect chains, but its availability in background processes or non-time-sensitive tasks is not required.






.. Rationale
.. ==========


Specification
=============

In-Vehicle Time Synchronization
-------------------------------

Definitions:

**Time Slave**
An actor that runs on the system and is responsible for

* synchronizing the local clock with an external Time Master using the PTP protocol (IEEE 802.1AS).
* providing the synchronization meta information to the clients, including score::time feature. Where meta information includes, but not limited to synchronization status (synchronized, not synchronized, unstable), time difference to the external time source, last synchronization time, current time point of the local clock and so on.

**Synchronization process metadata**
Data which is provided by the **Time Slave** and includes the current synchronized time, synchronization status, rate correction, and so on, which are the output or intermediate artifacts of the synchronization process.

Requirements:

* REQ_0001: the **Time Slave**, as part of score::time feature, shall synchronize the local clock with an external **Time Master** using the PTP protocol (IEEE 802.1AS).
* REQ_0002: the score::time shall get the current synchronized time and its metadata from the **Time Slave**.
* REQ_0003: the score::time shall maintain the current synchronized time, its synchronization status and **Synchronization process metadata**, to be able to provide the latest values by clients request.
* REQ_0004: the score::time shall validate the current synchronized time, which was received from the **Time Slave** and reflect the validation results in the time point status accordingly.
  Validation of the current synchronized time includes:

  * checking the time point for loss of synchronization
  * checking the time point for monotonicity
  * checking the time point for instability, like time jumps to the past or to the future

* REQ_0005: the score::time feature shall provide a mechanism to access (read only) to the synchronized time and its status across multiple applications within one ECU.
* REQ_0006: the score::time feature shall provide an access to the synchronized time and its status, see REQ_0005, in an efficient way without any additional overhead, like kernel calls, Resource manager involvement and so on.
  *Use case:* frequent access to the current synchronized time and its metadata by multiple clients within one ECU.
* REQ_0007: the score::time feature shall provide a mechanism to access (read only) to the internal state of the synchronization process, see **Synchronization process metadata**, across multiple applications within one ECU.
* REQ_0008: the score::time shall provide a mechanism to log the internal state of the synchronization process, see **Synchronization process metadata**, to be able to debug and diagnose the time synchronization process.
  *Use case:* Debugging and diagnostics of the time synchronization process.

The diagram above illustrates the data flow and interactions between the Time Slave, score::time middleware, and client applications within an ECU during PTP-based time synchronization.

.. uml:: data_flow.puml
   :caption: Data flow between Time Slave, score::time, and clients

Where

* The **Time Slave** (gPTP stack) communicates with an external Time Master to maintain accurate time synchronization using the PTP protocol.
* The **Time base provider** periodically reads the synchronized time from the Time Slave, validates it, and writes the results (including status flags and timestamps) into some shared resource towards **score::time** middleware. Different IPC mechanisms can be used for to provide actual synchronized time and its metadata to **Time base provider**, like:

  * shared memory, then the **Time Slave** writes the synchronized time and its metadata into the shared memory, which is then read by the **Time base provider** middleware.
  * **Time base provider** polls for current EMAC value with ``devctl`` calls.
  * other IPC methods.

* The **score::time** middleware accesses this shared resource to obtain the latest synchronized time and its metadata, adjusting the time as needed based on the local clock by requests from client applications.
* This architecture ensures efficient, low-overhead distribution of synchronized time and its status to multiple applications within the ECU, supporting both real-time and diagnostic use cases.

External Time Synchronization
-----------------------------

* REQ_0010: the score::time feature shall support synchronization with external time sources, such as GPS, based on SOME/IP messages.
* REQ_0011: the score::time shall maintain the current synchronized time and its synchronization status, to be able to provide the latest values by clients request.
* REQ_0012: the score::time feature shall provide a mechanism to access (read only) the current synchronized time from external time sources and its synchronization status.
* REQ_0013: the score::time feature shall provide a mechanism to log the internal state of the external time synchronization process, to be able to debug and diagnose the synchronization process.

High precision Clock
--------------------

* REQ_0014: the score::time feature shall provide a mechanism to access (read only) the high precision clock in nanoseconds precision.
  *Use case:* such clocks might be used for time-critical applications, such as audio/video streaming, event logging, and diagnostics.

Monotonic Clock
---------------

* REQ_0015: the score::time feature shall provide a mechanism to access (read only) to monotonic, not adjustable clock value, which is mapped from the known OS or HW clock.


.. Backwards Compatibility
.. =======================


Security Impact
===============


Safety Impact
=============


.. License Impact
.. ==============


How to Teach This
==================

.. Rejected Ideas
.. ==============

.. Open Issues
.. ===========

Glossary
========


.. _footnotes:

Footnotes
=========
