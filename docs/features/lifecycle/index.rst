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

.. _chm_feature_templates:


Lifecycle
---------

.. note:: Document header

.. document:: Lifecycle
   :id: doc__lifecycle
   :status: draft
   :safety: ASIL_B
   :tags: feature_request


Feature flag
------------

To activate this feature, use the following feature flag:

``experimental_lifecycle``


Abstract
--------

The lifecycle feature provides a set of functionalities to manage the lifecycle of
components in the S-SCORE platform. The goal is to ensure that components can be
started, stopped, and monitored effectively, providing a robust framework for managing the state of the system.

For every ecu handling of startup, shutdown, and monitoring of components is crucial to
ensure the system operates correctly and efficiently. Additionally we need do provide the
means to set the system in different operating modes, such as normal operation, engineering/debug mode,
flash mode etc.


Rationale
---------

Main task of the lifecycle system is to start and stop processes depending on the overall state the
user wants to achieve
and the functional dependencies between the processes.

We call a state of the system an `operating mode`, which is defined via the processes running on the
system at a certain point in time.

Examples for operating modes are `startup`, `running`, `shutdown` etc.

Via the configuration we define a certain operting mode and add all the components, which are needed to
realize this operating mode as dependencies.

A :term:`Lifecycle Component` is a configuration unit, which describes the `executable`, which shall be executed
and the :term:`Sandbox` the platform has to provide to run this executable.
E.g. the :term:`Sandbox` shall describe

- environment variables, which shall be set via the lifecycle system
- secpol policies on QNX, which shall be applied to the process
- cgroup configurations on linux, which shall be applied to the process
- user and group ids under which the process shall be started.
- ...

A second task of the lifecycle system is to supervise the aliveness of the processes, which are started
and to initiate appropriate actions in case of a failure, which might result in many cases in
a change of the operting mode.

Key aspects of the Lifecycle Management are as follows:

1. Performance: Fast changes of operating modes
2. Support of a mixed-criticality safe system via process isolation
3. Support of safe system design via enhanced monitoring capabilities

Specification
-------------

.. feat_arc_sta:: Feature architecture
   :id: feat_arc_sta__lifecycle__overview
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :fulfils:
   :includes: logic_arc_int__lifecycle__controlif, logic_arc_int__lifecycle__health_monitor_if, logic_arc_int__lifecycle__alive_if

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}

.. mod_view_sta:: Lifecycle
   :id: mod_view_sta__lifecycle__1
   :includes: comp_arc_sta__lifecycle__launch_manager, comp_arc_sta__lifecycle__healthmonitor

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}


The overall functionality of the feature can be split into 2 subfeatures, which are closely coupled to each other.

* Lifecycle Management: This subfeature is responsible for the management of the lifecycle of a lifecycle component.
  including starting and stopping processes, managing their dependencies, and handling different operating modes.

* Health Monitoring, which provides platform functionality to monitor the certain health conditions of applications
  * Alive Monitoring
  * Deadline Monitoring
  * Logical Programflow Monitoring



Architecture
------------

The concept is based on 2 major components:

* :term:`Launch Manager`: Responsible for starting and stopping components based on the defined operating modes
  and alive supervision of the started components

* :term:`Health Monitor`: Provides process local monitoring fucntionalities
  such as deadline monitoring and logical program flow monitoring.

.. toctree::
   :maxdepth: 1
   :glob:

   ./architecture/application_health_monitor
   ./architecture/control_interface
   ./architecture/external_monitoring
   ./architecture/configuration_parameters
   ./architecture/launch_manager



Terms and Definitions
---------------------

.. glossary::

    Launch Manager
      Component to start and stop processes on a POSIX like operating system.

    Health Monitor
      Provides process local monitoring fucntionalities such as deadline monitoring and logical program flow monitoring.

    Control Interface
      Interface to control the lifecycle of the system, e.g. to start and stop processes.

    Alive Interface
      Interface to monitor the aliveness of a process

    Sandbox
      A sandbox is a set of configurations, which are applied to a process when it is started.
      It can include environment variables, secpol policies, cgroup configurations, user and group ids etc.

    Health Monitor Interface
      Interface to monitor the health of a process, e.g. to check if a process is alive or if it is running as expected.

    Alive Monitoring
      Checks if an application reports an alive state in a certain period.

    Deadline Monitoring
      Monitor to detect if a state was reached within a specified time related to another event.

    Logical Programflow Monitoring
      Monitor to detect if certain states where reached in a defined sequence and time intervall.

    Operating mode
      a operating mode defines a set of components, which are in status runing and are supervised by the software platform.
      If the health management system detects abnormal situation it can change the :term:`Operating Mode`.

    Lifecycle Component
      Node of the dependency tree.







Requirements
------------

.. toctree::
   :maxdepth: 1
   :glob:

   requirements/*

Backwards Compatibility
-----------------------

New feature

Security Impact
---------------

TBD

Safety Impact
-------------

TBD


License Impact
--------------

TBD


How to Teach This
-----------------



Rejected Ideas
--------------


Open Issues
-----------


Footnotes
---------

[A collection of footnotes cited in the CR, and a place to list non-inline hyperlink targets.]
