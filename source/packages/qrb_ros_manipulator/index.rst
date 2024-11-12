===================
QRB ROS Manipulator
===================

qrb_ros_manipulator is a package to provide ROS service to control manipulator.

## Overview

QRB ROS manipulator provides different vendor robot ARM SDK to control hardware.

qrb_manipulator_controller, which is a dynamic library, is base on this framework for helping developers to utilize this feature and provide unified API to control robot ARM.
qrb_ros_manipulator, which is a ros package and provide ROS service to control robot ARM and get ARM status. It call qrb_manipulator_controller library to realize robot arm control.
qrb_ros_manipulator_msg provides manipulator ROS messages, it include robot arm status, tcp pose, link pose and claw control.


## Build

Currently, we only support use QCLINUX to build

1. Setup environments follow this document 's [Set up the cross-compile environment.](https://docs.qualcomm.com/bundle/publicresource/topics/80-65220-2/develop-your-first-application_6.html?product=1601111740013072&facet=Qualcomm%20Intelligent%20Robotics%20(QIRP)%20Product%20SDK&state=releasecandidate) part

2. Create `ros_ws` directory in `<qirp_decompressed_workspace>/qirp-sdk/`

3. Clone this repository under `<qirp_decompressed_workspace>/qirp-sdk/ros_ws`

.. code:: bash

    git clone https://github.com/quic-qrb-ros/qrb_ros_manipulator.git
    git clone https://github.com/lebai-robotics/lebai-sdk.git

4. Build this project
    Lebai SDK:

.. code:: bash

    cmake -S. -Bbuild -DBUILD_PYTHON=OFF -DBUILD_DEB=ON -DBUILD_TESTING=OFF
    make install

    Manupulator:

.. code:: bash

    export AMENT_PREFIX_PATH="${OECORE_TARGET_SYSROOT}/usr;${OECORE_NATIVE_SYSROOT}/usr"
    export PYTHONPATH=${PYTHONPATH}:${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages

    colcon build --merge-install --cmake-args \
    -DPython3_ROOT_DIR=${OECORE_TARGET_SYSROOT}/usr \
    -DPython3_NumPy_INCLUDE_DIR=${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages/numpy/core/include \
    -DPYTHON_SOABI=cpython-310-aarch64-linux-gnu -DCMAKE_STAGING_PREFIX=$(pwd)/install \
    -DCMAKE_PREFIX_PATH=$(pwd)/install/share \
    -DBUILD_TESTING=OFF

5. Push to the device & Install

.. code:: bash

    cd `<qirp_decompressed_workspace>/qirp-sdk/ros_ws/install`
    tar czvf qrb_ros_manipulator.tar.gz lib share
    scp qrb_ros_manipulator.tar.gz root@[ip-addr]:/opt/
    ssh root@[ip-addr]
    (ssh) tar -zxf /opt/qrb_ros_manipulator.tar.gz -C /opt/qcom/qirp-sdk/usr/

## Run

This package supports running it directly from the command or by dynamically adding it to the ros2 component container.

a.Run with command

1. Source this file to set up the environment on your device:

.. code:: bash

    ssh root@[ip-addr]
    (ssh) export HOME=/opt
    (ssh) source /opt/qcom/qirp-sdk/qirp-setup.sh
    (ssh) export ROS_DOMAIN_ID=xx
    (ssh) source /usr/bin/ros_setup.bash


2. Use this command to run this package

.. code:: bash

    (ssh)  ros2 launch qrb_ros_manipulator  manipulator_controller.launch.py


Packages
--------

.. toctree::
    :maxdepth: 2

    qrb_ros_manipulator <./qrb_ros_manipulator>

Supported platforms
-------------------

.. include:: ../common/supported_platforms.rst

Updates
-------

.. list-table::
    :header-rows: 1

    * - Date
      - Changes
    * - 2024-11-12
      - Initial release
   
      
