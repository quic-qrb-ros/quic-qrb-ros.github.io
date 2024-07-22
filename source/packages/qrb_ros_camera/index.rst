==============
QRB ROS Camera
==============

Overview
--------

Qualcomm Camera-Server provides camera data that obtained from the camera sensor.
``qrb_ros_camera`` this camera-server to get the latest camera data. With camera 
ros2 node, data can achieve zero copy performance when coming out of the camera-server. 
This will greatly reduce the latency between ROS nodes.

Camera data is widely used in robot localization, such as: SLAM(Simultaneous localization and mapping).
These localization applications have more precise performance after integrating Camera data to predict position.

This package leverages type adaption and intra process communication to optimize message formats and dramatically 
accelerate communication between participating nodes.

Build
-----

Currently, we only support use QCLINUX to build

1. Setup environments follow this document 's `Set up the cross-compile environment <https://docs.qualcomm.com/bundle/publicresource/topics/80-65220-2/develop-your-first-application_6.html>`__.

2. Create ``ros_ws`` directory in ``<qirp_decompressed_workspace>/qirp-sdk/``

3. Clone this repository under ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws``
    
.. code:: bash

    git clone https://github.com/quic-qrb-ros/lib_mem_dmabuf.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_transport.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_camera.git

4. Build this project

.. code:: bash
    
    export AMENT_PREFIX_PATH="${OECORE_TARGET_SYSROOT}/usr;${OECORE_NATIVE_SYSROOT}/usr"
    export PYTHONPATH=${PYTHONPATH}:${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages

    colcon build --merge-install --cmake-args \
    -DPython3_ROOT_DIR=${OECORE_TARGET_SYSROOT}/usr \
    -DPython3_NumPy_INCLUDE_DIR=${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages/numpy/core/include \
    -DSYSROOT_LIBDIR=${OECORE_TARGET_SYSROOT}/usr/lib \
    -DSYSROOT_INCDIR=${OECORE_TARGET_SYSROOT}/usr/include \
    -DPYTHON_SOABI=cpython-310-aarch64-linux-gnu -DCMAKE_STAGING_PREFIX=$(pwd)/install \
    -DCMAKE_PREFIX_PATH=$(pwd)/install/share \
    -DBUILD_TESTING=OFF

5. Push to the device & Install

.. code:: bash
    
    cd ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws/install``
    tar czvf qrb_ros_camera.tar.gz lib share
    scp qrb_ros_camera.tar.gz root@[ip-addr]:/opt/
    ssh root@[ip-addr]
    (ssh) tar -zxf /opt/qrb_ros_camera.tar.gz -C /opt/qcom/qirp-sdk/usr/

Run
---

This package supports running it directly from the command or by dynamically adding it to the ros2 component container.

a. Run with command

1. Source this file to set up the environment on your device:

.. code:: bash

    ssh root@[ip-addr]
    (ssh) export HOME=/opt
    (ssh) source /opt/qcom/qirp-sdk/qirp-setup.sh
    (ssh) export ROS_DOMAIN_ID=xx
    (ssh) source /usr/bin/ros_setup.bash

2. Use this command to run this package

.. code:: bash

    (ssh) ros2 launch qrb_ros_camera qrb_ros_camera_launch.py

b. Dynamically add it to the ros2 component container

.. code:: python

    ComposableNode(
        package='qrb_ros_camera',
        plugin='qrb_ros::camera::CameraComponent',
        name='camera'
    )


Packages
--------

.. toctree::
   :maxdepth: 2
   
    qrb_ros_camera  <./qrb_ros_camera>
    qrb_camera_lib  <./qrb_camera_lib>

Supported Platforms
-------------------

.. include:: ../common/supported_platforms.rst

Updates
-------

+-----------+--------------------------+
| Date      | Changes                  |
+-----------+--------------------------+
| 2024-7-16 | Add Build in QCLINUX SDK |
+-----------+--------------------------+
| 2024-2-5  | Initial release          |
+-----------+--------------------------+
