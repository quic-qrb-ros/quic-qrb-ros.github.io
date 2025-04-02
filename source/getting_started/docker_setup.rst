====================
QRB ROS Docker Setup
====================

This section will introduce the setup of QRB ROS Docker.

Introdution
-----------

QRB ROS Docker is a docker application for `QRB ROS <https://github.com/quic-qrb-ros>`__, which provides a **fast** and **easy** way for developer to experience QRB ROS applications on QCOM Linux Yocto BSP releases.

QRB ROS Docker provides the ROS2 environment based on Ubuntu, here comes the way to run it.

Build QRB ROS Docker
--------------------

.. note:: All following steps are happen on your device

1. clone the qrb_ros_docker

.. code:: bash

  mkdir -p /home/qrb_ros_ws/src && \
  git clone https://github.com/quic-qrb-ros/qrb_ros_docker

2. build the QRB ROS Docker

.. code:: bash

  cd /home/qrb_ros_ws/src/qrb_ros_docker/scripts && \
  bash docker_build.sh

Run QRB ROS Docker Container
----------------------------

.. code:: bash

  cd /home/qrb_ros_ws/src/qrb_ros_docker/scripts && \
  bash docker_run.sh

QRB ROS Packages Supported Situation
------------------------------------

QRB ROS Docker now support **12** QRB ROS Packages, supported list is as below:

.. list-table::
    :header-rows: 1

    * - Packages Name
      - Description

    * - `qrb_ros_benchmark <https://github.com/quic-qrb-ros/qrb_ros_benchmark>`_
      - Qualcomm Robotics platform Benchmark Tools.

    * - `qrb_ros_nn_inference <https://github.com/quic-qrb-ros/qrb_ros_nn_inference>`_
      - Qualcomm Robotics NatureNetwork Inference ROS Node.

    * - `qrb_ros_transport <https://github.com/quic-qrb-ros/qrb_ros_transport>`_
      - Zero Copy ROS Transport for Qualcomm platforms.

    * - `qrb_ros_system_monitor <https://github.com/quic-qrb-ros/qrb_ros_system_monitor>`_
      - QRB ROS System Monitor is a ROS package to access and publish system informations.

    * - `qrb_ros_imu <https://github.com/quic-qrb-ros/qrb_ros_imu>`_
      - Qualcomm Robotics platform IMU sensor ROS node.

    * - `qrb_ros_interfaces <https://github.com/quic-qrb-ros/qrb_ros_interfaces>`_
      - qrb_ros_interfaces is a ros2 package contains the custom qrb ros messages.

    * - `qrb_ros_robot_base <https://github.com/quic-qrb-ros/qrb_ros_robot_base>`_
      - Qualcomm Robotics platform Robot Base ROS Node.

    * - `qrb_ros_audio_service <https://github.qualcomm.com/QUIC-QRB-ROS/qrb_ros_audio_service>`_
      - Qualcomm Robotics Audio Service.

    * - `qrb_ros_manipulator <https://github.com/quic-qrb-ros/qrb_ros_manipulator>`_
      - Qualcomm Robotics manipulator ROS node.

    * - `qrb_ros_yolo_processor <https://github.com/quic-qrb-ros/qrb_ros_yolo_processor>`_
      - qrb_ros_yolo_processor provides ros nodes to execute pre/post-process for Yolo model.

    * - `qrb_ros_amr_service <https://github.com/quic-qrb-ros/qrb_ros_amr_service>`_
      - qrb_ros_amr_service is a package to manage the AMR behavior, such as navigation, mapping, return charging station.

    * - `qrb_ros_color_space_convert <https://github.com/quic-qrb-ros/qrb_ros_color_space_convert>`_
      - Qualcomm Robotics platform Color space conversion ROS node.



