====================
QRB ROS Audio Common
====================

Overview
--------

qrb_ros_audio_common is a package to provide two ros action for playback and capture.

Provide two ROS node for playback and capture.
Two node support set audio parameter(volume, channels, sample_format, rate, repeat) to specify stream format.
Provide interface(ros2 communication) to Transfer audio data between ROS node.
For Playback, can receive PCM data or file path from other ROS node, then playback to Speaker
For Capture, can get PCM data from Mic, then send PCM data to other ROS node or save to file

Build
-----

Currently, we only support use QCLINUX to build

1. Setup environments follow this document 's `Set up the cross-compile environment <https://docs.qualcomm.com/bundle/publicresource/topics/80-65220-2/develop-your-first-application_6.html>`__.

2. Create ``ros_ws`` directory in ``<qirp_decompressed_workspace>/qirp-sdk/``

3. Clone this repository under ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws``

.. code:: bash

    git clone https://github.qualcomm.com/QUIC-QRB-ROS/qrb_ros_audio_common.git

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

    cd `<qirp_decompressed_workspace>/qirp-sdk/ros_ws/install`
    tar czvf qrb_ros_audio.tar.gz lib share
    scp qrb_ros_audio.tar.gz root@[ip-addr]:/opt/
    ssh root@[ip-addr]
    (ssh) tar -zxf /opt/qrb_ros_audio.tar.gz -C /opt/qcom/qirp-sdk/usr/

Run
---

This package supports running it from ros launch file or directly running it from command.

a. Run with launch file

1. Source this file to set up the environment on your device:

.. code:: bash

    ssh root@[ip-addr]
    (ssh) export HOME=/opt
    (ssh) source /opt/qcom/qirp-sdk/qirp-setup.sh
    (ssh) export ROS_DOMAIN_ID=xx
    (ssh) source /usr/bin/ros_setup.bash

2. Use this launch file to run this package

.. code:: bash

    (ssh) ros2 launch qrb_ros_audio_common component.launch.py

b. Run with command

1. Playback Action:

.. code:: bash

    ros2 run qrb_ros_audio_common audio_common_node_exec --ros-args -p Stream_type:="playback" -p action_name:="ros_audio_playback" -p topic_name:="ros_audio_data"


2. Capture Action

.. code:: bash

    ros2 run qrb_ros_audio_common audio_common_node_exec --ros-args -p Stream_type:="capture" -p action_name:="ros_audio_capture" -p topic_name:="ros_audio_data"

After launch with component.launch.py, will start two action ros_audio_playback and ros_audio_capture.

Packages
--------

.. toctree::
   :maxdepth: 2

    qrb_audio_common_lib  <./qrb_audio_common_lib>

    qrb_ros_audio_common <./qrb_ros_audio_common>


Supported Platforms
-------------------

.. include:: ../common/supported_platforms.rst

Updates
-------

.. list-table::
    :header-rows: 1

    * - Date
      - Changes

    * - 2024-8-21
      - Add Build in QCLINUX SDK
