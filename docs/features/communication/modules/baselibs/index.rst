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

Baselibs Module
###############

.. mod_view_sta:: Baselibs
   :id: mod_view_sta__baselibs__baselibs
   :includes: comp_arc_sta__baselibs__json, comp_arc_sta__baselibs__message_passing, comp_arc_sta__baselibs__memory_shared

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

Components
==========

.. toctree::
   :titlesonly:

   json_component_architecture
   memory_shared_component_architecture
   message_passing_component_architecture
