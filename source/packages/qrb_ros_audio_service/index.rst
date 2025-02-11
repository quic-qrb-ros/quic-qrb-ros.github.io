=====================
QRB ROS Audio Service
=====================


Overview
--------

The ROS package provides essential audio capabilities, it is the entry
point for ROS to provide audio capabilities.

It supports both step-by-step and one-touch playback, allowing playback
from built-in sounds. Additionally, it offers recording functionality,
with the option to save to a local file or a topic.

Playback and record capabilities depend on
`qrb_ros_audio_common <https://github.com/quic-qrb-ros/qrb_ros_audio_common>`__.

Build
-----

Use QIRP SDK to build.

1. Build and install QIRP SDK with the steps in
   `qirp-sdk-workflows <https://docs.qualcomm.com/bundle/publicresource/topics/80-65220-2/introduction_1.html?vproduct=1601111740013072&versionId=1befb000-28cc-4b51-8b35-81601178edee&facet=Qualcomm%20Intelligent%20Robotics%20(QIRP)%20Product%20SDK#qirp-sdk-workflows>`__
   or `Quick start (using the prebuild
   package). <https://docs.qualcomm.com/bundle/publicresource/topics/80-65220-2/quick-start_3.html?vproduct=1601111740013072&versionId=1befb000-28cc-4b51-8b35-81601178edee&facet=Qualcomm%20Intelligent%20Robotics%20(QIRP)%20Product%20SDK>`__

2. Set up environments with the steps in `Set up the cross-compile
   environment. <https://docs.qualcomm.com/bundle/publicresource/topics/80-65220-2/develop-your-first-application_6.html?vproduct=1601111740013072&versionId=1befb000-28cc-4b51-8b35-81601178edee&facet=Qualcomm%20Intelligent%20Robotics%20(QIRP)%20Product%20SDK>`__

3. Create the ``ros_ws`` directory in
   ``<qirp_decompressed_workspace>/qirp-sdk/``.

4. Put ``qrb_audio_manager``, ``qrb_ros_audio_service``,
   ``qrb_ros_audio_service_msgs`` and ``qrb_ros_audio_common_msgs``
   packages under ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws``.

   .. code:: bash

      # qrb_audio_manager and qrb_ros_audio_service in qrb_ros_audio_service:
      git clone https://github.qualcomm.com/QUIC-QRB-ROS/qrb_ros_audio_service.git

      # qrb_ros_audio_service_msgs and qrb_ros_audio_common_msgs in qrb_ros_interfaces
      git clone https://github.qualcomm.com/QUIC-QRB-ROS/qrb_ros_interfaces.git

5. Build this project.

   .. code:: bash

      export AMENT_PREFIX_PATH="${OECORE_TARGET_SYSROOT}/usr;${OECORE_NATIVE_SYSROOT}/usr"
      export PYTHONPATH=${PYTHONPATH}:${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages

      colcon build --merge-install --cmake-args \
        -DPython3_ROOT_DIR=${OECORE_TARGET_SYSROOT}/usr \
        -DPython3_NumPy_INCLUDE_DIR=${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages/numpy/core/include \
        -DPYTHON_SOABI=cpython-310-aarch64-linux-gnu -DCMAKE_STAGING_PREFIX=$(pwd)/install \
        -DCMAKE_PREFIX_PATH=$(pwd)/install/share \
        -DBUILD_TESTING=OFF

6. Push to the device and Install.

   .. code:: bash

      cd <qirp_decompressed_workspace>/qirp-sdk/ros_ws/install
      tar czvf qrb_ros_audio.tar.gz lib share
      scp qrb_ros_audio_service.tar.gz root@[ip-addr]:/opt/
      ssh root@[ip-addr]
      (ssh) tar -zxf /opt/qrb_ros_audio_service.tar.gz -C /opt/qcom/qirp-sdk/usr/

Run
---

1. Source this file to set up the environment on your device.

   .. code:: bash

      ssh root@[ip-addr]
      (ssh) export HOME=/opt
      (ssh) source /opt/qcom/qirp-sdk/qirp-setup.sh
      (ssh) export ROS_DOMAIN_ID=xx
      (ssh) source /usr/bin/ros_setup.bash

2. Use this launch file to run this package.

   .. code:: bash

      ros2 launch qrb_ros_audio_service audio_service.launch.py

3. Run ``qrb_ros_audio_common`` on another ssh terminal.

4. Run test cases on a third ssh terminal.

   stream_handle indicate the stream created by Audio Service when command is "create". The value can be found on third ssh terminal
   (if use "ROS Command":
   `stream_handle=***`;
   if use "Python Script":
   `command create success 1 stream_handle ***`).

   .. list-table::
       :header-rows: 1

       * - Test Case
         - Using ROS Command
         - Using Python Script

       * - Get build-in sound names
         - mkdir -p /opt/qcom/qirp-sdk/usr/share/qrb-audio-manager/sounds

           chmod 0755 /opt/qcom/qirp-sdk/usr/share/qrb-audio-manager -R

           adb push clip.wav /opt/qcom/qirp-sdk/usr/share/qrb-audio-manager/sounds

           chmod 0644 /opt/qcom/qirp-sdk/usr/share/qrb-audio-manager/sounds/*

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "get-buildin-sound"
           }"
         - python3 audio_service_test.py --get-buildin-sound

       * - One-touch playback
         - ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "play",
           source: "clip",
           volume: 100,
           }"

           The playback will be stopped and released automatically after end of file. Or stop it before end of file:

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "stop",
           stream_handle: 3520332881,
           }"

           Note: One-touch playback will be released after stopping successful.
         - python3 audio_service_test.py --mode='one-touch' --source='security' --volume=100

           "Ctrl+C" audio_service_test.py.

       * - One-touch playback and repeat
         - ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "play",
           source: "clip",
           volume: 100,
           repeat: -1,
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "stop",
           stream_handle: 3520332881,
           }"
         - python3 audio_service_test.py --mode='one-touch' --source='security' --volume=100 --repeat=-1

           "Ctrl+C" audio_service_test.py.

       * - Step-by-step playback
         - ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           type: "playback",
           command: "create",
           source: "/tmp/music.wav",
           volume: 100,
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "start",
           stream_handle: 2551300426,
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "mute",
           mute: true,
           stream_handle: 2551300426,
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "mute",
           mute: false,
           stream_handle: 2551300426,
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "stop",
           stream_handle: 2551300426,
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "release",
           stream_handle: 2551300426,
           }"
         - python3 audio_service_test.py --type='playback' --source='/tmp/yesterday_48KHz.wav' --volume=100

           python3 audio_service_test.py --set-mute --mute=True --stream_handle=2124364840

           python3 audio_service_test.py --set-mute --mute=False --stream_handle=2124364840

           "Ctrl+C" audio_service_test.py.

       * - Streaming playback
         - Firstly, create and start a streaming playback, it subscribes audio pcm data from topic "loopback":

           step-by-step streaming playback:

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           audio_info: {
           channels: 1,
           sample_rate: 16000,
           sample_format: 16,
           },
           type: "playback",
           command: "create",
           volume: 100,
           topic_name: "loopback",
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "start",
           stream_handle: 1246004764,
           }"

           one-touch streaming playback:

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           audio_info: {
           channels: 1,
           sample_rate: 16000,
           sample_format: 16,
           },
           command: "play",
           volume: 100,
           topic_name: "loopback",
           }"

           Secondly, create and start a step-by-step record, it publishes audio pcm data to topic "loopback":

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           audio_info: {
           channels: 1,
           sample_rate: 16000,
           sample_format: 16,
           },
           type: "record",
           command: "create",
           pub_pcm: true,
           topic_name: "loopback",
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "start",
           stream_handle: 2681124530,
           }"

           Stop and release playback:

           for step-by-step streaming playback:

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "stop",
           stream_handle: 1246004764,
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "release",
           stream_handle: 1246004764,
           }"

           for one-touch streaming playback:

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "stop",
           stream_handle: 1246004764,
           }"

           Stop and release step-by-step record:

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "stop",
           stream_handle: 2681124530,
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "release",
           stream_handle: 2681124530,
           }"

         - step-by-step streaming playback:

           python3 audio_service_test.py --type='playback' --channels=1 --sample_rate=16000 --sample_format=16 --pub_pcm=True --volume=100 --topic_name='loopback'

           one-touch streaming playback:

           python3 audio_service_test.py --mode='one-touch' --channels=1 --sample_rate=16000 --sample_format=16 --pub_pcm=True --volume=100 --topic_name='loopback'

           python3 audio_service_test.py --type='record' --channels=1 --sample_rate=16000 --sample_format=16 --pub_pcm=True --topic_name='loopback'

           "Ctrl+C" playback audio_service_test.py.

           "Ctrl+C" record audio_service_test.py.

       * - Step-by-step record
         - ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           audio_info: {
           channels: 1,
           sample_rate: 16000,
           sample_format: 16,
           },
           type: "record",
           command: "create",
           source: "/tmp/rec.wav",
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "start",
           stream_handle: 1502099078,
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "stop",
           stream_handle: 1502099078,
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "release",
           stream_handle: 1502099078,
           }"
         - python3 audio_service_test.py --type='record' --source='/tmp/rec.wav' --channels=1 --sample_rate=16000 --sample_format=16

           "Ctrl+C" audio_service_test.py.

       * - Publish recording data
         - publish recording data to a topic (default topic name is "qrb_audiodata", but it can be specified using topic_name):

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           audio_info: {
           channels: 1,
           sample_rate: 16000,
           sample_format: 16,
           },
           type: "record",
           command: "create",
           pub_pcm: true,
           }"
            
           or, publish recording data to /qrb_audiodata. meanwhile, save it to file:

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           audio_info: {
           channels: 1,
           sample_rate: 16000,
           sample_format: 16,
           },
           type: "record",
           command: "create",
           pub_pcm: true,
           source: "/tmp/rec.wav",
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{command: "start",
           stream_handle: 806639317,
           }"

           ros2 topic echo /qrb_audiodata
            
           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "stop",
           stream_handle: 806639317,
           }"

           ros2 service call /audio_server qrb_ros_audio_service_msgs/srv/AudioRequest "{
           command: "release",
           stream_handle: 806639317,
           }"
         - publish recording data to a topic (default topic name is "qrb_audiodata", but it can be specified using topic_name):
           python3 audio_service_test.py --type='record' --source='/tmp/rec.wav' --channels=1 --sample_rate=16000 --sample_format=16 --pub_pcm=True

           or, publish recording data to /qrb_audiodata. meanwhile, save it to file:

           python3 audio_service_test.py --type='record' --source='/tmp/rec.wav' --channels=1 --sample_rate=16000 --sample_format=16 --pub_pcm=True

           ros2 topic echo /qrb_audiodata

Packages
--------

.. toctree::
   :maxdepth: 2

    qrb_ros_audio_service <./qrb_ros_audio_service>

    qrb_audio_manager  <./qrb_audio_manager>

Supported Platforms
-------------------

.. include:: ../common/supported_platforms.rst

Updates
-------

.. list-table::
    :header-rows: 1

    * - Date
      - Changes

    * - 2024-09-26
      - Initial release

    * - 2025-01-03
      - Update index.rst
