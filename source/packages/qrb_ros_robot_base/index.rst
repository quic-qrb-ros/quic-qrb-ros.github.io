=================
QRB ROS Robot Base
=================

Overview
--------
QRB ROS Robot Base control package provide ROS interfaces  to control AMR robot base.
It will init robot base, sync time with MCB, provide ROS interfaces for control robot base, publish robot base state with ROS topics and provide test tools for robot base control. All the data between MCB and RBx side through `QRC protocol <https://github.com/quic-qrb-ros/libqrc>`__.

Quickstart
----------

Currently, we only support build with QCLINUX SDK.

1. Download QCLINUX SDK follow this document: `download-the-prebuilt-robotics-image <https://docs.qualcomm.com/bundle/publicresource/topics/80-65220-2/download-the-prebuilt-robotics-image_3_1.html?product=1601111740013072&facet=Qualcomm%20Intelligent%20Robotics%20(QIRP)%20Product%20SDK&state=releasecandidate>`__

2. Create ``ros_ws`` directory in
   ``<qirp_decompressed_workspace>/qirp-sdk/``

   .. code:: bash

      mkdir -p <qirp_decompressed_workspace>/qirp-sdk/ros_ws

3. Clone this repository and dependencies under
   ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws``

   .. code:: bash

      cd <qirp_decompressed_workspace>/qirp-sdk/ros_ws
      git clone https://github.com/quic-qrb-ros/libqrc.git
      git clone https://github.com/quic-qrb-ros/qrb_ros_robot_base.git
      git clone https://github.com/QUIC-QRB-ROS/qrb_ros_interfaces.git

4. Build projects

   .. code:: bash

      export AMENT_PREFIX_PATH="${OECORE_TARGET_SYSROOT}/usr;${OECORE_NATIVE_SYSROOT}/usr"
      export PYTHONPATH=${PYTHONPATH}:${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages

      colcon build --merge-install --cmake-args \
         -DPython3_ROOT_DIR=${OECORE_TARGET_SYSROOT}/usr \
         -DPython3_NumPy_INCLUDE_DIR=${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages/numpy/core/include \
         -DCMAKE_STAGING_PREFIX=$(pwd)/install \
         -DCMAKE_PREFIX_PATH=$(pwd)/install/share -DBUILD_TESTING=OFF \
         -DPYTHON_SOABI=cpython-310-aarch64-linux-gnu -DQRC_RB3=ON

5. Push to the device and install

   .. code:: bash

      cd <qirp_decompressed_workspace>/qirp-sdk/ros_ws/install
      tar czvf qrb_ros_robot_base.tar.gz include lib share
      scp qrb_ros_robot_base.tar.gz root@[ip-addr]:/opt/
      ssh root@[ip-addr]
      (ssh) tar -zxf /opt/qrb_ros_robot_base.tar.gz -C /opt/qcom/qirp-sdk/usr/

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

3. Use this command to run keyboard test tool in another terminal

.. code:: bash

    (ssh) ros2 run qrb_ros_robot_base_keyboard robot_base

Packages
--------
+-----------------------------+-----------------------------------------------------------------------------------+
| Name                        | Descriptions                                                                      |
+-----------------------------+-----------------------------------------------------------------------------------+
| qrb_robot_base_manager      | The C/C++ library to control robot base. it communicates with MCB using `libqrc`. |
+-----------------------------+-----------------------------------------------------------------------------------+
| qrb_ros_robot_base          | ROS 2 API to control robot base, it calls `qrb_robot_base_manager`.               |
+-----------------------------+-----------------------------------------------------------------------------------+
| qrb_ros_robot_base_msgs     | ROS 2 interfaces definition.                                                      |
+-----------------------------+-----------------------------------------------------------------------------------+
| qrb_ros_robot_base_keyboard | Keyboard command line tools to control Robot base with ROS 2 messages.            |
+-----------------------------+-----------------------------------------------------------------------------------+
| qrb_ros_robot_base_urdf     | Robot base URDF model description and Rviz launch scripts.                        |
+-----------------------------+-----------------------------------------------------------------------------------+

.. toctree::
   :maxdepth: 2

    qrb_ros_robot_base <./qrb_ros_robot_base>
    qrb_ros_robot_base_keyboard <./qrb_ros_robot_base_keyboard>

Supported Platforms
-------------------

.. include:: ../common/supported_platforms.rst

Updates
-------------

+-----------+--------------------------+
| Date      | Changes                  |
+-----------+--------------------------+
| 2024-8-28 | Initial release          |
+-----------+--------------------------+
