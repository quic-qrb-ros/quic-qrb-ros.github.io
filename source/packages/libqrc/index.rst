===========
LIBQRC
===========

Overview
--------

Qualcomm robot Platforms need to communicate with motor control board to get odometry and sensors data and send speed
commands to motor control board to control robot move.
``libqrc`` realized the software protocol between qualcomm robot Platforms and motor control board.

In motor control side, Sensors data like imu, ultrasound, and odometry would transport to robot platform with qrc
protocol. In robot platform side, qrc protocol can transport speed command, emergency stop command and other control
commands from robot platform to motor control board.

At present, the qrc protocol define below messages format:
    - motion control message.
    - client control message.
    - emergency message.
    - configuration message.
    - imu message.
    - charger control message.
    - time sync message.
    - misc message.

This package provides reset function to control motor control board restart function based gpio.

In order to seperate platform influence, libqrc realized user-driver function to config uart and gpio
which related platform and provide API to qrc protocol.

This package support multi threads transport, ACK and SYNC mode functions.

This package leverages tiny frame protocol.

Build
-----

Currently, we only support use QCLINUX to build

1. Setup environments follow this document 's `Set up the cross-compile environment <https://docs.qualcomm.com/bundle/publicresource/topics/80-65220-2/develop-your-first-application_6.html>`__.

2. Create ``ros_ws`` directory in ``<qirp_decompressed_workspace>/qirp-sdk/``

3. Clone this repository under ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws``
    
.. code:: bash

    git clone https://github.com/quic-qrb-ros/libqrc.git

4. Build this project

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
    
    cd ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws/install``
    tar czvf libqrc.tar.gz lib share
    scp libqrc.tar.gz root@[ip-addr]:/opt/
    ssh root@[ip-addr]
    (ssh) tar -zxf /opt/qrb_ros_imu.tar.gz -C /opt/qcom/qirp-sdk/usr/

Run
---

This package just provides qrc protocol library, no execution file.

Packages
--------

.. toctree::
   :maxdepth: 2
   
    libqrc  <./libqrc>


Supported Platforms
-------------------

.. include:: ../common/supported_platforms.rst

Updates
-------

.. list-table::
    :header-rows: 1

    * - Date
      - Changes

    * - 2024-8-13
      - Update source code.

