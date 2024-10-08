===========
QRB ROS IMU
===========

Overview
--------

Qualcomm Sensor See Framework provides IMU data that obtained from the IMU driver via DSP side.
``qrb_ros_imu`` uses this framework to get the latest IMU data with high performance.

With the Qualcomm Sensor See Framework, data can achieve zero copy performance when coming out of the driver.
``qrb_sensor_client``, which is a dynamic library, is based on this framework for helping developers to utilize this feature.
This will greatly reduce the latency between the ROS node and the driver.
This time consumption measurement is around 0.4ms, which is several tens of times 
better than the performance where copying occurred before.

IMU data is widely used in robot localization, such as: SLAM(Simultaneous localization and mapping).
These localization applications have more precise performance after integrating IMU data to predict position.

This package leverages type adaption and intra process communication to optimize message formats and dramatically 
accelerate the communication between participating nodes.

Build
-----

Currently, we only support use QCLINUX to build

1. Set up environment following the `Set up the cross-compile environment <https://docs.qualcomm.com/bundle/publicresource/topics/80-65220-2/develop-your-first-application_6.html>`_ of the *QIRP User Guide*.

2. Create ``ros_ws`` directory in ``<qirp_decompressed_workspace>/qirp-sdk/``.

3. Clone this repository under ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws``
    
.. code:: bash

    git clone https://github.com/quic-qrb-ros/lib_mem_dmabuf.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_transport.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_imu.git

4. Build this project.

.. code:: bash
    
    export AMENT_PREFIX_PATH="${OECORE_TARGET_SYSROOT}/usr;${OECORE_NATIVE_SYSROOT}/usr"
    export PYTHONPATH=${PYTHONPATH}:${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages

    colcon build --merge-install --cmake-args \
      -DPython3_ROOT_DIR=${OECORE_TARGET_SYSROOT}/usr \
      -DPython3_NumPy_INCLUDE_DIR=${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages/numpy/core/include \
      -DPYTHON_SOABI=cpython-310-aarch64-linux-gnu -DCMAKE_STAGING_PREFIX=$(pwd)/install \
      -DCMAKE_PREFIX_PATH=$(pwd)/install/share \
      -DBUILD_TESTING=OFF

5. Push to the device and install.

.. code:: bash
    
    cd ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws/install``
    tar czvf qrb_ros_imu.tar.gz lib share
    scp qrb_ros_imu.tar.gz root@[ip-addr]:/opt/
    ssh root@[ip-addr]
    (ssh) tar -zxf /opt/qrb_ros_imu.tar.gz -C /opt/qcom/qirp-sdk/usr/

Run
---

This package supports running it directly from the command or by dynamically adding it to the ros2 component container.

Run with command
~~~~~~~~~~~~~~~~

1. Source this file to set up the environment on your device:

.. code:: bash

    ssh root@[ip-addr]
    (ssh) export HOME=/opt
    (ssh) source /opt/qcom/qirp-sdk/qirp-setup.sh
    (ssh) export ROS_DOMAIN_ID=xx
    (ssh) source /usr/bin/ros_setup.bash

2. Use this command to run this package

.. code:: bash

    (ssh) ros2 run qrb_ros_imu imu_node

Dynamically add it to the ros2 component container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    ComposableNode(
        package='qrb_ros_imu',
        plugin='qrb_ros::imu::ImuComponent',
        name='imu'
    )


Packages
--------

.. toctree::
   :maxdepth: 2
   
    qrb_ros_imu  <./qrb_ros_imu>

    qrb_sensor_client <./sensor_client>

    sensor_service <./sensor_service>

Supported platforms
-------------------

.. include:: ../common/supported_platforms.rst

Updates
-------

.. list-table::
    :header-rows: 1

    * - Date
      - Changes
    * - 2024-7-16
      - Added build in QCLINUX SDK
    * - 2024-2-5
      - Initial release
   
      
