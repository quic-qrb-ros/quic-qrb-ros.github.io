==============
|package_name|
==============

qrb_ros_robot_base is a ROS 2 API to control robot base, it calls `qrb_robot_base_manager`.

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

    (ssh) ros2 launch qrb_ros_robot_base robot_base.launch.py

Parameters
----------

Parameters Definition
~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------+---------------------+
| Name                          | Value Description | Default Value       |
+-------------------------------+-------------------+---------------------+
| car_wheel_perimeter           | float (m)         | 0.4115              |
+-------------------------------+-------------------+---------------------+
| car_wheel_space               | float (m)         | 0.3302              |
+-------------------------------+-------------------+---------------------+
| imu_enable                    | bool              | false               |
+-------------------------------+-------------------+---------------------+
| motion_max_speed              | float (m/s)       | 1.0                 |
+-------------------------------+-------------------+---------------------+
| motion_max_angle_speed        | float (rad/s)     | 1.5                 |
+-------------------------------+-------------------+---------------------+
| motion_pid_speed              | float[3]          | [400.0, 200.0, 0.0] |
+-------------------------------+-------------------+---------------------+
| motion_odom_frequency         | 1-50              | 50                  |
+-------------------------------+-------------------+---------------------+
| motion_tf_enable              | bool              | false               |
+-------------------------------+-------------------+---------------------+
| rc_enable                     | bool              | true                |
+-------------------------------+-------------------+---------------------+
| rc_max_speed                  | float (m/s)       | 0.8                 |
+-------------------------------+-------------------+---------------------+
| rc_max_angle_speed            | float (rad/s)     | 2.0                 |
+-------------------------------+-------------------+---------------------+
| scale_speed                   | float             | 1.0                 |
+-------------------------------+-------------------+---------------------+
| scale_speed_odom              | float             | 1.0                 |
+-------------------------------+-------------------+---------------------+
| ultra_enable                  | bool              | true                |
+-------------------------------+-------------------+---------------------+
| ultra_quantity                | uint              | 7                   |
+-------------------------------+-------------------+---------------------+
| oba_bottom_distance           | float (m)         | 0.05                |
+-------------------------------+-------------------+---------------------+
| oba_front_distance            | float (m)         | 0.15                |
+-------------------------------+-------------------+---------------------+
| oba_side_distance             | float (m)         | 0.15                |
+-------------------------------+-------------------+---------------------+
| test_transport_latency_enable | bool              | false               |
+-------------------------------+-------------------+---------------------+
| time_sync_interval_sec        | unsigned int (s)  | 300                 |
+-------------------------------+-------------------+---------------------+
| time_sync_threshold_ms        | unsigned int (ms) | 10                  |
+-------------------------------+-------------------+---------------------+

Attention

- rc_max_speed need <= motion_max_speed
- rc_max_angle_speed need <= motion_max_angle_speed

Robot Models
~~~~~~~~~~~~

Change robot model with environment variable:

.. code:: bash

    export ROBOT_BASE_MODEL=robot_base_mini

Current support robot models:

- Standard Robot base: `robot_base` (default)
- Circle Robot base: `robot_base_mini`

Parameters Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

Change config yaml file

- Standard Robot base: `robot_base.yaml` (default)
- Circle Robot base: `robot_base_mini.yaml`

code path: qrb_ros_robot_base/qrb_ros_robot_base/config/obot_base.yaml

device path: /opt/qcom/qirp-sdk/usr/share/qrb_ros_robot_base/config/robot_base.yaml

.. code:: bash

    /qrb_robot_base_manager:
        ros__parameters:
        ultra_enable: true
        rc_enable: true
        motion_tf_enable: false
        # other parameters


Relaunch ROS node

.. code:: bash

    ros2 launch qrb_ros_robot_base robot_base.launch.py

.. |package_name| replace:: ``qrb_ros_robot_base``