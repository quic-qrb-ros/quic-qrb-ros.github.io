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

QuickStart
----------

.. tabs::

   .. tab:: QRB ROS Docker

      1. Setup Docker on device: `Docker Setup <../../getting_started/docker_setup.html>`__.

      2. Download source code

         .. code:: bash

                cd ${QRB_ROS_WS}/src
                git clone https://github.com/quic-qrb-ros/lib_mem_dmabuf.git
                git clone https://github.com/quic-qrb-ros/qrb_ros_imu.git
                git clone https://github.com/quic-qrb-ros/qrb_ros_transport.git

      3. Build packages

         .. code:: bash

            colcon build

      4. Run

        .. code:: bash

            cd ${QRB_ROS_WS}/src

            source install/local_setup.sh
            ros2 run qrb_ros_imu imu_node

   .. tab:: QIRP SDK

      1. Setup QCLINUX SDK environments: Reference :doc:`Getting Started - Environment Setup </getting_started/environment_setup>`

      2. Create workspace in QCLINUX SDK environment and clone source code

         .. code:: bash

                mkdir -p <qirp_decompressed_workspace>/qirp-sdk/ros_ws
                cd <qirp_decompressed_workspace>/qirp-sdk/ros_ws

                git clone https://github.com/quic-qrb-ros/lib_mem_dmabuf.git
                git clone https://github.com/quic-qrb-ros/qrb_ros_imu.git
                git clone https://github.com/quic-qrb-ros/qrb_ros_transport.git

      3. Build source code with QCLINUX SDK

         .. code:: bash

                export AMENT_PREFIX_PATH="${OECORE_NATIVE_SYSROOT}/usr:${OECORE_TARGET_SYSROOT}/usr"
                export PYTHONPATH=${OECORE_NATIVE_SYSROOT}/usr/lib/python3.12/site-packages/:${OECORE_TARGET_SYSROOT}/usr/lib/python3.12/site-packages/

                colcon build --continue-on-error --cmake-args \
                  -DCMAKE_TOOLCHAIN_FILE=${OE_CMAKE_TOOLCHAIN_FILE} \
                  -DPYTHON_EXECUTABLE=${OECORE_NATIVE_SYSROOT}/usr/bin/python3 \
                  -DPython3_NumPy_INCLUDE_DIR=${OECORE_NATIVE_SYSROOT}/usr/lib/python3.12/site-packages/numpy/core/include \
                  -DCMAKE_MAKE_PROGRAM=/usr/bin/make \
                  -DBUILD_TESTING=OFF

      4. Install ROS package to device

         .. code:: bash

                cd <qirp_decompressed_workspace>/qirp-sdk/ros_ws/install/qrb_ros_imu
                tar -czvf qrb_ros_imu.tar.gz include lib share
                ssh root@[ip-addr]
                (ssh) mount -o remount rw /usr
                scp qrb_ros_imu.tar.gz root@[ip-addr]:/home/
                ssh ssh root@[ip-addr]
                (ssh) tar --no-overwrite-dir --no-same-owner -zxf /home/qrb_ros_imu.tar.gz -C /usr/

      5. Run

        .. code:: bash

            (ssh) export HOME=/home
            (ssh) setenforce 0
            (ssh) source /usr/bin/ros_setup.sh && source /usr/share/qirp-setup.sh
            (ssh) ros2 run qrb_ros_imu imu_node


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
   
      
