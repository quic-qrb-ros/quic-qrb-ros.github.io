======================
QRB ROS System Monitor
======================

Overview
--------

`QRB ROS System Monitor <https://github.com/quic-qrb-ros/qrb_ros_system_monitor>`__ is a ROS package to publish system informations.

Main features:

-  ``/cpu``: Topic for CPU usage informations
-  ``/memory``: Topic for memory usage informations
-  ``/disk``: Topic for disk usage informations
-  ``/swap``: Topic for swap partition informations
-  ``/temperature``: Topic for CPU temperature
-  ``/battery``: Topic for device battery level
-  ``/system_info_server``: Service for providing system informations.


System Requirements
-------------------

-  Linux, now only support Linux systems

Quickstart
----------

Currently, we only support build with QCLINUX SDK.

1. Setup QCLINUX SDK: :doc:`Environment setup </getting_started/environment_setup>`

2. Create ``ros_ws`` directory in
   ``<qirp_decompressed_workspace>/qirp-sdk/``

   .. code:: bash

      mkdir -p <qirp_decompressed_workspace>/qirp-sdk/ros_ws

3. Clone this repository and dependencies under
   ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws``

   .. code:: bash

      git clone https://github.com/quic-qrb-ros/qrb_ros_system_monitor.git

4. Build projects

   .. code:: bash

      export AMENT_PREFIX_PATH="${OECORE_TARGET_SYSROOT}/usr;${OECORE_NATIVE_SYSROOT}/usr"
      export PYTHONPATH=${PYTHONPATH}:${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages
      
      colcon build --merge-install --cmake-args \
         -DPython3_ROOT_DIR=${OECORE_TARGET_SYSROOT}/usr \
         -DPython3_NumPy_INCLUDE_DIR=${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages/numpy/core/include \
         -DPYTHON_SOABI=cpython-310-aarch64-linux-gnu -DCMAKE_STAGING_PREFIX=$(pwd)/install \
         -DCMAKE_PREFIX_PATH=$(pwd)/install/share \
         -DBUILD_TESTING=OFF

5. Run

   .. code:: bash

      cd <qirp_decompressed_workspace>/qirp-sdk/ros_ws/install
      tar czvf qrb_ros_system_monitor.tar.gz lib share
      scp qrb_ros_system_monitor.tar.gz root@[ip-addr]:/opt/
      ssh ssh root@[ip-addr]
      (ssh) tar -zxf /opt/qrb_ros_system_monitor.tar.gz -C /opt/qcom/qirp-sdk/usr/

Packages
--------

.. toctree::
   :maxdepth: 2

    qrb_ros_system_monitor <./qrb_ros_system_monitor>
    qrb_ros_system_monitor_interfaces <./qrb_ros_system_monitor_interfaces>

Supported Platforms
-------------------

.. include:: ../common/supported_platforms.rst

Updates
-------------

+------------+--------------------------+
| Date       | Changes                  |
+------------+--------------------------+
| 2024-10-19 | Initial release          |
+------------+--------------------------+
