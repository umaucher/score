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

Glossary
========

.. glossary::

    Launch Manager
      Component to start and stop processes on a POSIX like operating system.

    Health Monitor
      Provides process local monitoring functionalities such as deadline monitoring
      and logical program flow monitoring.

    Control Interface
      Interface to control the lifecycle of the system, e.g. to start and stop processes.

    Alive Interface
      Interface to monitor the aliveness of a process.

    Sandbox
      A sandbox is a set of configurations, which are applied to a process when it
      is started. It can include environment variables, secpol policies, cgroup
      configurations, user and group IDs etc.

    Health Monitor Interface
      Interface to monitor the health of a process, e.g. to check if a process is
      alive or if it is running as expected.

    Alive Monitoring
      Checks if an application reports an alive state in a certain period.

    Deadline Monitoring
      Monitor to detect if a state was reached within a specified time related to
      another event.

    Logical Programflow Monitoring
      Monitor to detect if certain states were reached in a defined sequence and
      time interval.

    Operating Mode
      An operating mode defines a set of components, which are in status running
      and are supervised by the software platform. If the health management system
      detects abnormal situation it can change the :term:`Operating Mode`.

    Lifecycle Component
      Node of the dependency tree.

    Processes
      Executable programs running on the system that are managed by the Launch Manager.

    UID
      User Identifier - a unique number assigned to each user on a Unix-like operating system.

    GID
      Group Identifier - a unique number assigned to each group on a Unix-like operating system.

    Polling Interval
      The time interval between successive checks of a condition or status.

    Working Directory
      The current directory from which a process is executed, also known as CWD (Current Working Directory).

    File Descriptor
      A handle used by a process to access files or other input/output resources.

    Procmgr
      Process Manager - a QNX system component that manages process creation and execution.

    ASLR
      Address Space Layout Randomization - a security technique that randomizes the memory layout of processes.

    Recovery Action
      Actions taken by the Launch Manager when a process fails or terminates abnormally.

    Liveliness
      The state indicating that a process is active and responding as expected.

    Watchdog
      A monitoring mechanism that detects system failures and can trigger recovery actions.

    Interval
      A period of time between events or measurements.

    QNX
      A real-time operating system commonly used in embedded systems.

    QOS
      QNX Operating System.

    DSS
      Device Safe State - a safe operational state that a system can enter during failures.

    DAG
      Directed Acyclic Graph - a data structure used to represent dependencies between processes.

    SWC
      Software Components - modular software units that can be independently managed.
