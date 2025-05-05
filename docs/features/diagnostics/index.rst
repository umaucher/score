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

.. _diagnostics_feature:

Diagnostics
############

.. note:: Diagnostics

.. document:: Diagnostics
   :id: doc__diagnostics
   :status: draft
   :safety: QM
   :tags: feature_request


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_diagnostics``


Abstract
========

We propose adding support for Vehicle Diagnostics via Service-Oriented Vehicle Diagnostics (SOVD) within S-CORE.
SOVD offers a service-oriented, self-descriptive interface based on standardized RESTful APIs,
eliminating the need for manually modeling diagnostic interfaces as required in UDS.
This signifi-cantly reduces integration overhead and simplifies the onboarding of new ECUs.
Additionally, SOVD ena-bles scalable, secure, and cloud-ready diagnostics with real-time fault access and
advanced data han-dling across platforms. Integrating SOVD into S-CORE will enhance developer efficiency,
improve system maintainability, and support future-proof diagnostic workflows.

The intent of this feature request is to define a high-level architecture for the diagnostic system.
The com-ponents listed throughout this document require detailed feature requests in the future respectively.


Motivation
==========

Currently there is no solution for vehicle diagnostics in S-CORE.
Diagnostic is a core capability of automotive platform stacks and is required for various use-cases
such as field troubleshooting, quality assurance, after sales, production, development and more.


Rationale
=========

[Describe why particular design decisions were made.]


   .. note::
      The rationale should provide evidence of consensus within the community and discuss important objections or concerns raised during discussion.


Specification
=============


Architecture
------------

The proposed concept consists of three main parts:

1.	A library to aggregate faults and integrate the diagnostic system into S-CORE
2.	A SOVD based diagnostic system
3.	Components to interface the diagnostic system with the outside – e.g. Tester or UDS based ECUs

The diagram below shows the entire concept with the three subgroups connected.

.. image:: _assets/score-diagnostics-draft.drawio.svg
   :alt: Diagnostic stack component architecture


In scope components
-------------------

The following components are considered in scope of this feature request.

F lib (Fault Library)

- Provides an interface for FEO activities to report faults.
- Relays faults via IPC to central Diagnostic Fault Manager.
- Enables domain-specific error logic (e.g. debouncing) by exposing a configuration inter-face
- Reporting of faults additionally results in a log entry.
- The interface needs to be specified further but will likely include: Fault ID (FID), time, ENUM fault type (like DLT ENUMs), optional meta data.
- F lib is the base for activity specific, custom fault handling.

Diagnostic Fault Manager

- Aggregates and manages diagnostic fault data from F libs across the system.
- Provides centralized fault status to the SOVD Server.
- Interfaces with the Diagnostic DB (persistency) to store and retrieve data.
- Stores (persistently) central configuration (e.g. for debouncing thresholds) which can be loaded during startup by F libs.

Diagnostic DB

- Stores static and runtime diagnostic data
- Is considered in scope due to the domain specific data format but internally uses S-CORE::Persistency.
- The data format needs to be specified further but will likely include:
- Diagnostic Trouble Code (DTC): OEM specific code, relevant for end-user.
- Fault ID (FID): ECU specific ID to uniquely identify every fault.
- Count: occurrence count of DTC/fault.
- Meta data: meta data related to fault occurrence.

SOVD Server

- Central entry point for all diagnostic requests via SOVD.
- Implements the SOVD API and dispatches requests to services, DB, and fault manager.
- Manages authentication, configuration, and data access via IPC.

Service App

- Is a base concept to extend the system with system-specific diagnostic ser-vices/routines (e.g., DTC clear, ECU reset, Flash Master).
- Interfaces with the SOVD Server via IPC.

SOVD Gateway

- Forwards SOVD requests to appropriate backend targets (e.g., adapters, proxies, cli-ents).
- Acts as a router between clients and distributed SOVD components.
- Supports multi-ECU SOVD communication.

SOVD Client

- Off-board, on-board or cloud client that initiates diagnostics via SOVD protocol.
- Can be used by developers, testers, ECUs or cloud services- should be deployment ag-nostic.
- Handles access control on the client side – e.g. by providing relevant certificates.

Classic Diagnostic Adapter

- Translates SOVD service calls to UDS commands.
- Enables backward compatibility with legacy ECUs that only support UDS.
- Configured via ODX files describing ECU-specific UDS expectations.

UDS2SOVD Proxy

- Exposes selected SOVD functionality via UDS for backward-compatible testers.
- Acts as a local translation layer between UDS clients and SOVD stack.
- Configured using a ODX to define what is exposed.


Out of scope components
-----------------------

The following components are out of scope for this feature request but are included for context.
Each is briefly described to illustrate its role within the overall system architecture and
to highlight any resulting requirements or constraints imposed by the diagnostic system design.

Configuration Manager

- Provides configuration data to the SOVD Server (e.g., ECU layout, variant, parameters).
- Enables parametrization of applications.

Authentication Manager

- Manages authentication and authorization for incoming SOVD requests.
- Ensures only valid users or clients can access services.

Crypto

- Provides cryptographic services – e.g. securely store and retrieve diagnostic certifi-cates.
- Used by Authentication Manager.

Persistency

- Provides persistent data storage.

Flash Service App

- Specialized extension of the Service App to handle ECU flashing.
- Provides routines for software update/bootloader access via diagnostics.

Rest of Vehicle UDS

- Represents legacy ECUs in the vehicle that only speak UDS.
- Interact via the Classic Diagnostic Adapter (SOVD2UDS).

Rest of Vehicle SOVD

- Other ECUs in the vehicle that already support SOVD natively.
- Can communicate directly with the SOVD Gateway.

UDS Tester

- Traditional diagnostics tester that uses UDS protocol.
- Communicates with the UDS2SOVD Proxy for limited diagnostics access.


Requirements
------------

The following section includes unordered and incomplete feature requirements.

.. feat_req:: SOVD Standard
   :id: feat_req__diagnostics__sovd_std
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__dtc_read_sovd
   :status: valid

   The SOVD implementation shall conform to the SOVD standard as defined in ISO/DIS 17978 (or the latest available draft or final publication).

.. feat_req:: OEM Diagnostic Plug In
   :id: feat_req__diagnostics__oem_plugin
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__dtc_read_sovd
   :status: valid

   The diagnostic system shall provide a plug-in mechanism to include OEM-specific features.

.. feat_req:: Diagnostic system internal communication
   :id: feat_req__diagnostics__internal_com
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__dtc_read_sovd
   :status: valid

   All internal communication between diagnostic components that do not use UDS or SOVD protocols shall be implemented using the S-CORE::COM middleware.


Backwards Compatibility
=======================

UDS2SOVD Proxy and Classic Diagnostic Adapter (SOVD2UDS) ensure compatibility with legacy UDS systems.
ODX as a standardized exchange format further ensure compatibility with proprietary diagnos-tic data models.


Security Impact
===============

[How could a malicious user take advantage of this new/modified feature?]

   .. note::
      If there are security concerns in relation to the CR, those concerns should be explicitly written out to make sure reviewers of the CR are aware of them.

Which security requirements are affected or has to be changed?
Could the new/modified feature enable new threat scenarios?
Could the new/modified feature enable new attack paths?
Could the new/modified feature impact functional safety?
If applicable, which additional security measures must be implemented to mitigate the risk?

    .. note::
     Use Trust Boundary, Defense in Depth Analysis and/or Security Software Critically Analysis,
     Vulnerability Analysis.
     [Methods will be defined later in Process area Security Analysis]


Safety Impact
=============

At this point in time no safety impact is foreseen. The expected ASIL level is QM.
Configuration Management could have a safety impact but is handled in another feature request and out of scope of this document.


License Impact
==============

There are no license restrictions preventing the implementation of an open-source SOVD stack at this time.
While SOVD is currently in the ISO standardization process (ISO/DIS 17978), the relevant parts—especially Part 3,
which defines the API—are already publicly available for purchase as Draft Interna-tional Standards (DIS).
These drafts are considered stable and are typically subject only to minor edito-rial changes before final publication.
As such, referencing the current DIS versions is sufficient for im-plementation purposes, and does not pose any legal or license-related risk.
Once the final ISO standard is published, the delta to the current drafts is expected to be minimal and can be easily addressed.

The license impact regarding publication of XML schemata to handle/convert ODX files as per ISO 22901 needs to be evaluated.


How to Teach This
=================

[How to teach users, new and experienced, how to apply the CR to their work.]

   .. note::
      For a CR that adds new functionality or changes behavior, it is helpful to include a section on how to teach users, new and experienced, how to apply the CR to their work.


Rejected Ideas
==============

An UDS first based diagnostic system was considered but rejected.
The current market trend clearly indicates the move towards SOVD.
Additionally, there a multiple well established proprietary UDS stacks and tools available.
Because no FOSS SOVD stack exists currently, it presents an opportunity for S-CORE to provide value and increase adoption.


Open Issues
===========

-	Interfacing concept with Autosar Adaptive Diagnostic Stack for mixed-stacks and/or a transition-al phase
-	Investigate synergies between Configuration Manager and central diagnostic configuration file in Diagnostic Fault Manager
-	Evaluate publication of XML schemata to handle/convert ODX files as per ISO 22901


Footnotes
=========

[A collection of footnotes cited in the CR, and a place to list non-inline hyperlink targets.]
