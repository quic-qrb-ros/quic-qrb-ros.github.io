==============
|package_name|
==============

qrb_ros_robot_base_keyboard is Keyboard command line tools to control Robot base with ROS 2 messages.

Run
---

1. Source this file to set up the environment on your device:

.. code:: bash

    ssh root@[ip-addr]
    (ssh) export HOME=/opt
    (ssh) source /opt/qcom/qirp-sdk/qirp-setup.sh
    (ssh) export ROS_DOMAIN_ID=xx
    (ssh) source /usr/bin/ros_setup.bash

2. Use this command to run robot base manager

.. code:: bash

    (ssh) ros2 run qrb_ros_robot_base_keyboard robot_base

Use keyboard to control
-----------------------

.. code:: bash

    ---------------------------------------------------------------
    Moving around:      Control mode:        Charger command:
    u    i    o       1   2   3   ?       8   9   0
    j    k    l      Motion mode:         Emergency command:
    m    ,    .       4   5   6   7       [   ]
    ---------------------------------------------------------------

    k : stop

    q/z : increase/decrease max speeds by 10%
    w/x : increase/decrease only linear speed by 10%
    e/c : increase/decrease only angular speed by 10%

    1 : application control
    2 : charger control
    3 : remote controller
    ? : query current mode

    4 : speed mode (for test only)
    5 : driver error (for test only)
    6 : motion emergency enable (for test only)
    7 : motion emergency disable (for test only)

    8 : start charging
    9 : stop charging
    0 : get battery state

    [ : emergency enable
    ] : emergency disable

    CTRL-C to quit

.. |package_name| replace:: ``qrb_ros_robot_base``