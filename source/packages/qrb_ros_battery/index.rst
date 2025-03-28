===============
QRB ROS BATTERY
===============

Overview
--------

``qrb_ros_battery`` is a package to publish the battery state data from system node.

``qrb_battery_client``, which is a dynamic library, is based on dbus framework for helping developers to
connect with server to get the battery data.

Battery data can help developers assess the current battery status and determine 
if it needs to be recharged at a charging station in a timely manner.

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
                git clone https://github.com/quic-qrb-ros/qrb_ros_battery.git

      3. Build packages

         .. code:: bash

            colcon build

      4. Run

        .. code:: bash

            cd ${QRB_ROS_WS}/src

            source install/local_setup.sh
            ros2 run qrb_ros_battery battery_node

   .. tab:: QIRP SDK

      5. Setup QCLINUX SDK environments: Reference :doc:`Getting Started - Environment Setup </getting_started/environment_setup>`

      6. Create workspace in QCLINUX SDK environment and clone source code

         .. code:: bash

                mkdir -p <qirp_decompressed_workspace>/qirp-sdk/ros_ws
                cd <qirp_decompressed_workspace>/qirp-sdk/ros_ws

                git clone https://github.com/quic-qrb-ros/qrb_ros_battery.git

      7. Build source code with QCLINUX SDK

         .. code:: bash

                export AMENT_PREFIX_PATH="${OECORE_NATIVE_SYSROOT}/usr:${OECORE_TARGET_SYSROOT}/usr"
                export PYTHONPATH=${OECORE_NATIVE_SYSROOT}/usr/lib/python3.12/site-packages/:${OECORE_TARGET_SYSROOT}/usr/lib/python3.12/site-packages/

                colcon build --continue-on-error --cmake-args \
                  -DCMAKE_TOOLCHAIN_FILE=${OE_CMAKE_TOOLCHAIN_FILE} \
                  -DPYTHON_EXECUTABLE=${OECORE_NATIVE_SYSROOT}/usr/bin/python3 \
                  -DPython3_NumPy_INCLUDE_DIR=${OECORE_NATIVE_SYSROOT}/usr/lib/python3.12/site-packages/numpy/core/include \
                  -DCMAKE_MAKE_PROGRAM=/usr/bin/make \
                  -DBUILD_TESTING=OFF

      8. Install ROS package to device

         .. code:: bash

                cd <qirp_decompressed_workspace>/qirp-sdk/ros_ws/install/qrb_ros_battery
                tar -czvf qrb_ros_battery.tar.gz include lib share
                scp qrb_ros_battery.tar.gz root@[ip-addr]:/home/
                cd <qirp_decompressed_workspace>/qirp-sdk/ros_ws/install/qrb_battery_client
                tar -czvf qrb_battery_client.tar.gz include lib share
                scp qrb_battery_client.tar.gz root@[ip-addr]:/home/
                ssh root@[ip-addr]
                (ssh) mount -o remount rw /
                (ssh) tar --no-overwrite-dir --no-same-owner -zxf /home/qrb_ros_battery.tar.gz -C /usr/
                (ssh) tar --no-overwrite-dir --no-same-owner -zxf /home/qrb_battery_client.tar.gz -C /usr/

      9. Run

        .. code:: bash

            (ssh) export HOME=/home
            (ssh) setenforce 0
            (ssh) source /usr/bin/ros_setup.sh && source /usr/share/qirp-setup.sh
            (ssh) ros2 run qrb_ros_battery battery_node


Packages
--------

.. toctree::
   :maxdepth: 2
   
    qrb_ros_battery  <./qrb_ros_battery>

    qrb_battery_client <./battery_client>

Supported platforms
-------------------

.. include:: ../common/supported_platforms.rst

Updates
-------

.. list-table::
    :header-rows: 1

    * - Date
      - Changes
    * - 2025-3-11
      - Initial release
