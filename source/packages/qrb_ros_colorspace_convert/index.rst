===========================
QRB ROS Color Space Convert
===========================

Overview
--------

Qualcomm's smart devices, such as the RB3 Gen2, use NV12 as the default image color space conversion format. 
Generally, the more common color space format is RGB888. To embrace open source and facilitate developers in 
converting between these two formats, we have developed the ``qrb_ros_colorspace_convert``. 
The feature as follows:

- Provide ROS node include

    - API to convert nv12 to rgb8
  
    - API to convert rgb8 to nv12
- Support dmabuf fd as input / output

- Input & output image receive &send with QRB ROS transport

- Hardware accelerates with GPU by OpenGL ES



Build
------

Currently, we only support use QCLINUX to build

1. Setup environments follow this document 's `Set up the cross-compile environment <https://docs.qualcomm.com/bundle/publicresource/topics/80-65220-2/develop-your-first-application_6.html>`__.

2. Create ``ros_ws`` directory in ``<qirp_decompressed_workspace>/qirp-sdk/``

3. Clone this repository under ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws``
    
.. code:: bash

    git clone https://github.com/quic-qrb-ros/lib_mem_dmabuf.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_transport.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_colorspace_convert.git

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
    tar czvf qrb_ros_colorspace_convert.tar.gz lib share
    scp qrb_ros_colorspace_convert.tar.gz root@[ip-addr]:/opt/
    ssh root@[ip-addr]
    (ssh) tar -zxf /opt/qrb_ros_colorspace_convert.tar.gz -C /opt/qcom/qirp-sdk/usr/

Run
---

This package supports running it directly from the command or by dynamically adding it to the ros2 component container.


1. Source this file to set up the environment on your device:

.. code:: bash

    ssh root@[ip-addr]
    (ssh) export HOME=/opt
    (ssh) source /opt/qcom/qirp-sdk/qirp-setup.sh
    (ssh) export ROS_DOMAIN_ID=xx
    (ssh) source /usr/bin/ros_setup.bash

2. Use this command to run this package

.. code:: bash

    (ssh) ros2 launch qrb_ros_colorspace_convert colorspace_convert.launch.py


Packages
--------

1. ROS Topic

=========== ================================ =================
Topic name  Message type                     Description
=========== ================================ =================
image_raw   qrb_ros::transport::type::Image  The input image
image       qrb_ros::transport::type::Image  The output image
=========== ================================ =================

2. ROS2 parameters

================= ======= ============= =========================
Parameter name    Type    Default value Description
================= ======= ============= =========================
conversion_type   string  nv12_to_rgb8  The conversion type
latency_fps_test  bool    True          test the fps & latency
================= ======= ============= =========================



Supported Platforms
-------------------

.. include:: ../common/supported_platforms.rst

Updates
-------

+---------------+----------------------------------+
| Date          | Changes                          |
+---------------+----------------------------------+
| 2024-7-9      | Initial release                  |
+---------------+----------------------------------+
