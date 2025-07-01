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

:term:`Launch Manager`
======================

Launching Processes
-------------------

.. feat_req:: Support for launching processes
    :id: feat_req__lifecycle__launch_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching :term:`processes`.

.. feat_req:: Process dependency handling
    :id: feat_req__lifecycle__process_ordering
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for ordering the launching of
    :term:`processes` based on the dependencies.


.. feat_req:: Launching processes in parallel
    :id: feat_req__lifecycle__parallel_launch_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching :term:`processes`
    in parallel.

.. feat_req:: Conditional waitfor launching
    :id: feat_req__lifecycle__waitfor_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for waitfor conditions to be
    satisfied to launch :term:`processes`.

.. feat_req:: Control interface support
    :id: feat_req__lifecycle__custom_cond_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support to wait for configurable custom
    conditions, which can be signaled from applications via :term:`Control Interface`.


.. feat_req:: Forward process information
    :id: feat_req__lifecycle__process_input_output
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support to pass the output of one or
    multiple :term:`processes` as input arguments to another process.

.. feat_req:: Conditionally launch of processes
    :id: feat_req__lifecycle__cond_process_start
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support to conditionally start a process
    or process group based on the return value of a single or multiple :term:`processes`
    executed before.

.. feat_req:: Support for essential processes
    :id: feat_req__lifecycle__essential_processes
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall allow to mark :term:`processes` as "essential"
    for the startup.


.. feat_req:: Stop further processing on failing essential process
    :id: feat_req__lifecycle__essential_process_fail
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    In case a process that is marked as "essential" for the startup fails to start,
    the :term:`Launch Manager` shall stop the further processing of its config and
    stop the startup sequence.

.. feat_req:: Error reaction on essential process failure
    :id: feat_req__lifecycle__error_reaction_config
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall support to configure the error reaction in case
    an "essential" process failed to start. Possible error reactions are:

    * System halt

    * System reset

    * Execution of a specifically marked process


.. feat_req:: Handling process args
    :id: feat_req__lifecycle__process_launch_args
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching a process with a
    given set of arguments.

.. feat_req:: Launching process in debug mode
    :id: feat_req__lifecycle__debug_support
    :reqtype: Functional
    :security: NO
    :safety: QM
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching process with a
    given set of debug arguments in debug mode.

.. feat_req:: Launching process in HELD state
    :id: feat_req__lifecycle__support_held_state
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching a process in a
    HELD state.


.. feat_req:: Process user, group IDs support
    :id: feat_req__lifecycle__uid_gid_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching a process with a
    given :term:`UID`/:term:`GID` (user name/Group Identifier).

.. feat_req:: Conditional launch total wait time
    :id: feat_req__lifecycle__total_wait_time_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for per condition configurable
    total wait time for launch conditions to be satisfied.

.. feat_req:: Conditional launch polling interval
    :id: feat_req__lifecycle__polling_interval
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for per condition configurable
    :term:`Polling Interval` for launch conditions to be checked.


.. feat_req:: Process priority support
    :id: feat_req__lifecycle__launch_priority_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching a process with a
    given priority.


.. feat_req:: CWD support
    :id: feat_req__lifecycle__cwd_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching a process with a
    given :term:`Working Directory`.

.. feat_req:: Launching terminal
    :id: feat_req__lifecycle__terminal_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching a terminal or a
    session leader.

.. feat_req:: Standard handle redirection
    :id: feat_req__lifecycle__std_handle_redir
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for stdin, stdout, stderr
    redirection.

.. feat_req:: Builtin commands
    :id: feat_req__lifecycle__builtin_command_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for builtin commands.


.. feat_req:: Non-root support
    :id: feat_req__lifecycle__secpol_non_root
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__dependability__safety_features
    :status: invalid

    The :term:`Launch Manager` shall provide support to be started with security
    policy as non-root.

.. feat_req:: Configurable amount of retries
    :id: feat_req__lifecycle__retries_configurable
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall support a configurable amount of retries in
    case error occurs during startup of a component (e.g. file not available) occurs.


.. feat_req:: Procmgr ability support
    :id: feat_req__lifecycle__procmgr_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching :term:`processes`
    with configured :term:`procmgr` abilities.

.. feat_req:: File descriptor inheritance support
    :id: feat_req__lifecycle__fd_inheritance
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching a process with
    given :term:`File Descriptor` inheritance restrictions.


.. feat_req:: Security policy support
    :id: feat_req__lifecycle__support_secpol_type
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__dependability__safety_features
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching a process with a
    given security policy.

.. feat_req:: Supplementary group support
    :id: feat_req__lifecycle__supplementary_groups
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching a process with a
    given set of supplementary groups.

.. feat_req:: Scheduling support
    :id: feat_req__lifecycle__scheduling_policy
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching a process with
    certain scheduling policy.

.. feat_req:: CPU runmask support
    :id: feat_req__lifecycle__runmask_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching a process with a
    given runmask.


.. feat_req:: ASLR support
    :id: feat_req__lifecycle__aslr_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__dependability__safety_features
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching process with
    :term:`ASLR` (Address Space Layout Randomization).

.. feat_req:: Resource limit support
    :id: feat_req__lifecycle__process_rlimit_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching a process with a
    given set of system resource limits (rlimit).


.. feat_req:: Process detach from parent support
    :id: feat_req__lifecycle__detach_parent_process
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching a process to
    detach from parent.

.. feat_req:: Critical process support
    :id: feat_req__lifecycle__critical_processes
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for launching a process as a
    critical process.

.. feat_req:: Process adoption
    :id: feat_req__lifecycle__running_processes
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall adopt already running :term:`processes`.

.. feat_req:: Dropping process responsibility
    :id: feat_req__lifecycle__drop_supervsion
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support to dropping all surveillance
    and failure reaction activities of :term:`processes`.


.. feat_req:: Multiple instance of executable
    :id: feat_req__lifecycle__multi_start_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall permit an executable to be launched more than once.


.. feat_req:: Pre-start validation
    :id: feat_req__lifecycle__validate_conditions
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall be able to validate the pre-start conditions of the executable using the conditions.


.. feat_req:: post-start validation
    :id: feat_req__lifecycle__validation_conditions
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall be able to validate the start of the executable using the conditions.


.. feat_req:: Managing an externally started process
    :id: feat_req__lifecycle__process_ownership
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall be able to own an externally started process.


.. feat_req:: Invalid dependency
    :id: feat_req__lifecycle__consistent_dependencies
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall reject an inconsistent definition of set of executables dependencies.


.. feat_req:: Dangling dependency
    :id: feat_req__lifecycle__stop_process_dependents
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall be able to stop a process when all it's dependents are stopped if specified in the set of executables.


.. feat_req:: Coordination stop dependency
    :id: feat_req__lifecycle__stop_order_spec
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall permit the stop order of non-dependent processes to be specified.


Groups
......

.. feat_req:: Named group
    :id: feat_req__lifecycle__named_group_executables
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall permit to represent a set of executables as a
    named group.

.. feat_req:: Launching group
    :id: feat_req__lifecycle__start_named_group_exe
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall be able to start a named group of executables.

.. feat_req:: Stopping group
    :id: feat_req__lifecycle__stop_group_executables
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall be able to stop a named group of executables.


.. feat_req:: Start group launch
    :id: feat_req__lifecycle__launcher_start_group
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall be able to start a named group when the launcher
    is started.

.. feat_req:: Process state
    :id: feat_req__lifecycle__process_state_comm
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall have a means for the launched :term:`processes`
    to communicate a state, which represents the launched processes' internal state,
    to the launcher.


Terminating Processes
---------------------

.. feat_req:: Stop timeout
    :id: feat_req__lifecycle__configurable_timeout
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for configurable timeout
    :term:`Interval` to wait for the process to be stopped.

.. feat_req:: Terminating process
    :id: feat_req__lifecycle__process_termination
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for terminating :term:`processes`.

.. feat_req:: Handling process dependency in termination
    :id: feat_req__lifecycle__terminationn_dependency
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall terminate the :term:`processes` based on the
    dependency order.


.. feat_req:: Configurable delay between SIGTERM and SIGKILL
    :id: feat_req__lifecycle__time_to_wait_config
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The time to wait, before SIGKILL is sent shall be configurable. In case "0" is
    stated, the SIGKILL shall be sent immediately.

.. feat_req:: Normal shutdown
    :id: feat_req__lifecycle__launch_manager_shutdown
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall support normal shutdown by terminating all
    process in the dependency order.


.. feat_req:: Slow shutdown
    :id: feat_req__lifecycle__slow_shutdown_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall support slow shutdown by terminating the
    :term:`processes` in the dependency order.

.. feat_req:: Fast shutdown
    :id: feat_req__lifecycle__fast_shutdown_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall support fast shutdown by terminating itself
    without affecting the started :term:`processes`.

.. feat_req:: Launch Manager shutdown
    :id: feat_req__lifecycle__launcher_exit_shutdown
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall exit after performing shutdown operation by
    stopping all the :term:`processes` it owns in the dependency order when requested.

.. feat_req:: Shutdown signal handling
    :id: feat_req__lifecycle__shutdown_signal
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall implement a shutdown by sending a SIGTERM to
    the process. In case the process does not terminate itself, a SIGKILL shall be sent.


:term:`Control Interface`
-------------------------

.. feat_req:: Control commands
    :id: feat_req__lifecycle__control_commands
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for commands to control
    component states.

.. feat_req:: Query commands
    :id: feat_req__lifecycle__query_commands
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for commands to query component
    states.


.. feat_req:: Report "started/running/degraded"
    :id: feat_req__lifecycle__controlif_status
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall be able to report status on components via the
    :term:`Control Interface`.

    Note: status can be "started/running/degraded" - refer to documentation for details

.. feat_req:: Request group launch
    :id: feat_req__lifecycle__request_group_launch
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall be able to start a named group respecting the
    dependencies when requested.

.. feat_req:: Request group stop
    :id: feat_req__lifecycle__request_group_stop
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall be able to stop a named group respecting the
    dependencies when requested.

.. feat_req:: Request group restart
    :id: feat_req__lifecycle__request_group_restart
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall be able to restart a named group respecting
    the dependencies when requested.


Monitoring, Notification and Recovery
-------------------------------------

.. feat_req:: Process crash monitoring
    :id: feat_req__lifecycle__monitor_abnormal_term
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for monitoring abnormal
    termination of :term:`processes`.

.. feat_req:: Process state notification
    :id: feat_req__lifecycle__ext_monitor_notify
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for external monitors to get
    notified on process life status.


.. feat_req:: Recovery action
    :id: feat_req__lifecycle__recovery_action_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall support :term:`Recovery Action` for the
    abnormally terminated :term:`processes`.

.. feat_req:: Restart of named group as recovery action
    :id: feat_req__lifecycle__recover_group
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall support a restart of a named group as recovery
    method in case a single process out of that group terminated abnormally or lost
    its :term:`Liveliness`.

.. feat_req:: Monitoring and recovery: watchdog support
    :id: feat_req__lifecycle__smart_watchdog_config
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall support smart :term:`Watchdog`, configurable
    per process.


.. feat_req:: Monitoring and recovery: recovery wait time
    :id: feat_req__lifecycle__configurable_wait_time
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for configurable wait time
    that shall elapse before repeating :term:`Recovery Action`.

.. feat_req:: Monitoring and recovery: adopted process monitoring
    :id: feat_req__lifecycle__monitoring_processes
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall provide support for monitoring adopted
    :term:`processes`.

.. feat_req:: Process launch monitoring
    :id: feat_req__lifecycle__failure_detect
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall be able to detect and react to failure of the
    process launch.

.. feat_req:: Process liveliness detection
    :id: feat_req__lifecycle__liveliness_detection
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall be able to detect and react to loss of
    :term:`Liveliness` of the :term:`processes` it owns.

.. feat_req:: Process monitoring
    :id: feat_req__lifecycle__process_monitoring
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall monitor the state of the :term:`processes` as
    specified by the set of executables.


.. feat_req:: Recovery
    :id: feat_req__lifecycle__process_failure_react
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall be able to react to a process failure by
    optionally performing one of relaunching the process, stopping the process,
    stopping the process and starting another process, or triggering :term:`QNX`
    :term:`Operating System` (:term:`QOS`) Device Safe State (:term:`DSS`).

.. feat_req:: Multi-instance
    :id: feat_req__lifecycle__multi_instance_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall be able to run in multiple instances with its
    own configurations on a system.

.. feat_req:: Launch manager self health check
    :id: feat_req__lifecycle__lm_self_health_check
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall implement time based cyclical monitoring of itself.

.. feat_req:: Launch manager external watchdog notification
    :id: feat_req__lifecycle__lm_ext_watchdog_notify
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall trigger a notification to an external
    :term:`Watchdog` for each successful self monitoring test execution.

.. feat_req:: Launch manager external watchdog notification - failed test
    :id: feat_req__lifecycle__lm_ext_wdg_failed_test
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall not trigger an external :term:`Watchdog`
    notification if an internal health check failed.

.. feat_req:: Launch manager external monitoring configuration
    :id: feat_req__lifecycle__lm_ext_watchdog_cfg
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The :term:`Launch Manager` shall support configuring the :term:`Interval` of
    the internal health check executions.

Logging
-------

.. feat_req:: Logging slog2 and file support
    :id: feat_req__lifecycle__slog2_logging
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__dev_experience__logging_support
    :status: invalid

    The :term:`Launch Manager` shall support slog2 and a logging file as logging
    destinations.

.. feat_req:: Logging state transitions
    :id: feat_req__lifecycle__process_logging_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__dev_experience__logging_support
    :status: invalid

    The :term:`Launch Manager` shall provide support for logging process launches,
    :term:`processes` exit/recovery, internal tasks, and interaction with external monitor.

.. feat_req:: Logging timestamp
    :id: feat_req__lifecycle__log_timestamp
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__dev_experience__logging_support
    :status: invalid

    The :term:`Launch Manager` logs shall contain timestamp information.


.. feat_req:: Logging DAG
    :id: feat_req__lifecycle__dag_logging_controlif
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__dev_experience__logging_support
    :status: invalid

    The :term:`Launch Manager` shall provide the possibility to log the :term:`DAG`
    in a human readable format, triggered via :term:`Control Interface`.


.. feat_req:: Configuration dependency view
    :id: feat_req__lifecycle__dependency_visu
    :reqtype: Functional
    :security: NO
    :safety: QM
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall have the means to log the current dependencies in a format that can be visualized when requested.

Configuration file
------------------

.. feat_req:: Configuration file support
    :id: feat_req__lifecycle__modular_config_support
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__functional_req__file_based
    :status: invalid

    The :term:`Launch Manager` shall provide modular configuration file support to
    configure process attributes.

.. feat_req:: Updating configuration
    :id: feat_req__lifecycle__session_extension
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__functional_req__file_based
    :status: invalid

    The :term:`Launch Manager` shall provide support for extending already running
    session with additional new configuration file.

.. feat_req:: Module support
    :id: feat_req__lifecycle__clustering_modules_supp
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__functional_req__file_based
    :status: invalid

    The :term:`Launch Manager` shall provide support to clustering set of components
    as modules.


.. feat_req:: global process properties
    :id: feat_req__lifecycle__central_default_defines
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall be able to centrally define defaults for specific properties for the set of executables.


.. feat_req:: Lazy check of configured commands
    :id: feat_req__lifecycle__lazy_check
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall check availability of executables in the filesystem only when the executable shall required to be executed.


.. feat_req:: Configuration Dependency view
    :id: feat_req__lifecycle__deps_visualization
    :reqtype: Functional
    :security: NO
    :safety: QM
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall have the means to generate the specified dependencies in a format that can be visualized.


.. feat_req:: Configuration Verification tool
    :id: feat_req__lifecycle__offline_config_valid
    :reqtype: Functional
    :security: NO
    :safety: QM
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall have a means to validate the configuration offline.


Condition Check
---------------

.. feat_req:: Launched Process status
    :id: feat_req__lifecycle__launcher_status_storage
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall provide a way to store the status of the launched process.


.. feat_req:: Condition check based on status
    :id: feat_req__lifecycle__condition_check_method
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall provide a method for condition check based on process state.


.. feat_req:: Configuration of action based on condition evaluation
    :id: feat_req__lifecycle__config_actions_cond
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall provide a way to configure actions based on condition evaluation i.e. to be able to configure SUCCESS and FAILURE case.


.. feat_req:: Condition check based on path
    :id: feat_req__lifecycle__path_condition_check
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall provide a method for condition check for a path.


.. feat_req:: Condition check based on ENV
    :id: feat_req__lifecycle__env_variable_cond_check
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall provide a method for condition check for environment variable.


.. feat_req:: Condition check based on all dependency
    :id: feat_req__lifecycle__dependency_check
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall provide a method to check if all dependency has been executed.


.. feat_req:: Condition check based on at least one dependency
    :id: feat_req__lifecycle__check_dependency_exec
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall provide a method to check if at least one dependency has been executed.


.. feat_req:: Condition check for each SWC its dependencies
    :id: feat_req__lifecycle__define_swc_dependencies
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall provide a way to define for each :term:`SWC` (Software Components), its dependencies.


.. feat_req:: Condition check for each SWC its stop sequence
    :id: feat_req__lifecycle__stop_sequence
    :reqtype: Functional
    :security: NO
    :safety: ASIL_D
    :satisfies: stkh_req__execution_model__processes
    :status: invalid

    The Launch Manager shall provide a way to define the stop sequence for each :term:`SWC` (Software Components).
