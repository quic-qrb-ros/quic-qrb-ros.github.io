====================
QRB ROS Image Resize
====================

Overview
--------

Qualcomm's smart devices, use NV12 as the default image color space format. To embrace open source and facilitate developers in NV12 image to downscaling, we have developed the image resize ROS node that support EVA acceleration. The feature as follows:

- Provide ROS node include
  
  - API to downscale nv12 image.

- limitation

  - Supprots input nv12 image and outputs downsized nv12 image.

  - Supports a maximum input image size of 3840 x 2160.(0 < input_width ≤ 3840 and 0 < input_height ≤ 2160)

  - Supports a maximum downscale ratio of 1/8.(1/8 input_width ≤ output_width ≤ input_width and 1/8 input_height ≤ output_height ≤ input_height)

  - Supports a minimum output image size of 64 x 64.(64 ≤ output_width ≤ input_width and 64 ≤ output_height ≤ input_height)

  - Supports interpolation methods are 0: EVA_SCALEDOWN_BILINEAR and 1: EVA_SCALEDOWN_BICUBIC.

  - Since OpenCV does not support nv12 images to resize, and must convert NV12 to RGB format, which will result in color loss.

- Support dmabuf fd as input / output.

- Input / output image receive/send with QRB ROS transport.

- Hardware accelerates with EVA.

Note: 
  If your platform device does not support EVA hardware, that will use the resize function provided by OpenCV. 
  Since OpenCV does not support nv12 images to resize, and must convert NV12 to RGB format, which will result in color loss.
  (example: RB3 Gen2 was not support EVA hard ware, it just use OpenCV to resize, which will result in color loss. Not recommended.)

Build
------

Currently, we only support NV12 color space format downscale that based on Qualcomm platform that support EVA acceleration.

1. Setup environments follow this document 's `Set up the cross-compile environment <https://docs.qualcomm.com/bundle/publicresource/topics/80-65220-2/develop-your-first-application_6.html>`__.

2. Create ``ros_ws`` directory in ``<qirp_decompressed_workspace>/qirp-sdk/``

3. Clone this repository under ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws``
    
.. code:: bash

    git clone https://github.com/quic-qrb-ros/lib_mem_dmabuf.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_transport.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_image_resize.git

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
    -DBUILD_TESTING=OFF --continue-on-error

5. Push to the device & Install

.. code:: bash
    
    cd ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws/install``
    tar czvf qrb_ros_image_resize.tar.gz lib share
    scp qrb_ros_image_resize.tar.gz root@[ip-addr]:/opt/
    ssh root@[ip-addr]
    (ssh) tar -zxf /opt/qrb_ros_image_resize.tar.gz -C /opt/qcom/qirp-sdk/usr/

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

    (ssh) ros2 launch qrb_ros_image_resize qti_image_resize.launch.py


Packages
--------

1. ROS Topic

============= ================================ =================
Topic name    Message type                     Description
============= ================================ =================
image_raw     qrb_ros::transport::type::Image  The input image
image_resize  qrb_ros::transport::type::Image  The output image
============= ================================ =================

2. ROS2 parameters

================= ======= ============= ===========================================
Parameter name    Type    Default value Description
================= ======= ============= ===========================================
use_scale         string  nv12_to_rgb8  Enable use the scale_height and scale_width
height            int     -1			Size of height
width             int     -1            Size of width
scale_height      double  1             Downscale of height
scale_width       double  1             Downscale of width
interpolation     int     0             The interpolation type
calculate_enable  bool    False         Test the fps & latency
================= ======= ============= ===========================================



Supported Platforms
-------------------


Updates
-------

+---------------+----------------------------------+
| Date          | Changes                          |
+---------------+----------------------------------+
| 2024-8-14     | Initial release                  |
+---------------+----------------------------------+
