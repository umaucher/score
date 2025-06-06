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


Requirements
############

Diagnostic and Fault Management
===============================


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
