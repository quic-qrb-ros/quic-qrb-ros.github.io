=================
QRB ROS Transport
=================

Overview
--------

`QRB ROS
Transport <https://github.com/quic-qrb-ros/qrb_ros_transport>`__ is
designed for hardware-acceleration friendly transporting of messages on
Qualcomm robotics platforms. It uses type adaption to make message data
zero-copy between different ROS nodes, and different hardwares. It
includes adapted types for Qualcomm robotics platforms.

`Type Adaptation Feature (REP
2007) <https://ros.org/reps/rep-2007.html>`__ has enabled on ROS 2
Humble. This interface will allow us to define methods for serializing
directly to the user requested type, and/or using that type in
intra-process communication without ever converting it.

qrb_ros_transport is based on
`lib_mem_dmabuf <https://github.com/quic-qrb-ros/lib_mem_dmabuf>`__, it
is open sourced and apply to all platforms based on Linux.

dmabuf_transport is a zero-copy transport implementation for all platforms
based on Linux, it only depends on Linux standard DMA buffer APIs.

System Requirements
-------------------

-  Linux kernel version 5.12 and later, for kernel dma-buf support.
-  ROS 2 Humble and later, for type adaption support.

Quickstart
----------

Currently, we only support build with QCLINUX SDK.

1. Setup QCLINUX SDK environments follow this document: `Set up the
   cross-compile
   environment <https://docs.qualcomm.com/bundle/publicresource/topics/80-65220-2/develop-your-first-application_6.html?product=1601111740013072&facet=Qualcomm%20Intelligent%20Robotics%20(QIRP)%20Product%20SDK&state=releasecandidate>`__

2. Create ``ros_ws`` directory in
   ``<qirp_decompressed_workspace>/qirp-sdk/``

   .. code:: bash

      mkdir -p <qirp_decompressed_workspace>/qirp-sdk/ros_ws

3. Clone this repository and dependencies under
   ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws``

   .. code:: bash

      cd <qirp_decompressed_workspace>/qirp-sdk/ros_ws
      git clone https://github.com/quic-qrb-ros/lib_mem_dmabuf.git
      git clone https://github.com/quic-qrb-ros/qrb_ros_imu.git
      git clone https://github.com/quic-qrb-ros/qrb_ros_transport.git

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

Packages
--------

.. toctree::
   :maxdepth: 2

    qrb_ros_transport <./qrb_ros_transport>
    lib_mem_dmabuf <./lib_mem_dmabuf>
    dmabuf_transport <./dmabuf_transport>

Supported Platforms
-------------------

.. include:: ../common/supported_platforms.rst
Resources
---------

-  `ROS 2 Type Adaption <https://ros.org/reps/rep-2007.html>`__: ROS 2
   new feature to implement zero copy transport.
-  `Linux dma-buf <https://docs.kernel.org/driver-api/dma-buf.html>`__:
   Linux kernel subsystem for sharing buffers for hardware (DMA) access
   across multiple device drivers and subsystems, and for synchronizing
   asynchronous hardware access
-  `lib_mem_dmabuf <https://github.com/quic-qrb-ros/lib_mem_dmabuf>`__:
   Library for access and interact with Linux DMA heaps.

Updates
-------------

+-----------+--------------------------+
| Date      | Changes                  |
+-----------+--------------------------+
| 2024-7-12 | Add Imu type support     |
+-----------+--------------------------+
| 2024-3-28 | Initial release          |
+-----------+--------------------------+
