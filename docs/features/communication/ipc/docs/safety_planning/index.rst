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

.. _safety_planning_ipc:

Safety Planning
###############

Inter-process Communication Safety Work Products
================================================

.. list-table:: Feature Inter-process Communication Workproducts
    :header-rows: 1

    * - Workproduct Id
      - Link to process
      - Process status
      - Link to issue
      - Link to WP
      - WP status

    * - :need:`PROCESS_wp__feat_request`
      - :need:`PROCESS_gd_temp__change__feature_request`
      - :ndf:`copy('status', need_id='PROCESS_gd_temp__change__feature_request')`
      - `#69 <https://github.com/eclipse-score/score/issues/69>`_
      - :need:`doc__com_ipc`
      - :ndf:`copy('status', need_id='doc__com_ipc')`

    * - :need:`PROCESS_wp__requirements__feat`
      - :need:`PROCESS_gd_temp__req__feat_req`
      - :ndf:`copy('status', need_id='PROCESS_gd_temp__req__feat_req')`
      - `#69 <https://github.com/eclipse-score/score/issues/69>`_
      - :doc:`../requirements/index`
      - see below

    * - :need:`PROCESS_wp__requirements__feat_aou`
      - :need:`PROCESS_gd_temp__req__aou_req`
      - :ndf:`copy('status', need_id='PROCESS_gd_temp__req__aou_req')`
      - <link to issue>
      - :doc:`../requirements/index`
      - see below

    * - :need:`PROCESS_wp__feature_arch`
      - :need:`PROCESS_gd_temp__arch__feature`
      - :ndf:`copy('status', need_id='PROCESS_gd_temp__arch__feature')`
      - `#388 <https://github.com/eclipse-score/score/issues/388>`_
      - :doc:`../architecture/index`
      - see below

    * - :need:`PROCESS_wp__feature_safety_analysis`
      - <link to process>
      - <automated>
      - <link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`PROCESS_wp__requirements__inspect`
      - :need:`PROCESS_gd_chklst__req__inspection`
      - :ndf:`copy('status', need_id='PROCESS_gd_chklst__req__inspection')`
      - <link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`PROCESS_wp__sw_arch_verification`
      - :need:`PROCESS_gd_chklst__arch__inspection_checklist`
      - :ndf:`copy('status', need_id='PROCESS_gd_chklst__arch__inspection_checklist')`
      - <link to issue>
      - <Link to WP>
      - <automated>

    * - :need:`PROCESS_wp__verification__feat_int_test`
      - :need:`PROCESS_gd_guidl__verification_guide`
      - :ndf:`copy('status', need_id='PROCESS_gd_guidl__verification_guide')`
      - <link to issue>
      - <Link to WP>
      - <automated>

Feature Requirements Status
---------------------------

.. needtable::
   :style: table
   :types: feat_req
   :tags: ipc
   :columns: id;status
   :colwidths: 25,25
   :sort: title

Feature AoU Status
------------------

.. needtable::
   :style: table
   :types: aou_req
   :tags: ipc
   :columns: id;status
   :colwidths: 25,25
   :sort: title

Feature Architecture Status
---------------------------

.. needtable::
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: ipc
   :columns: id;status
   :colwidths: 25,25
   :sort: title
