========================
``qrb_ros_audio_common``
========================

Overview
---------

qrb_ros_audio_common is a ros2 package to provice two action for playback and capture.
Load qrb_audio_common_lib lib for pulseaudio stream control.

Load node
---------

start two node with launch file

    .. code:: bash

        (ssh) ros2 launch qrb_ros_audio_common component.launch.py

start two node with singal command

    .. code:: bash

        (ssh) ros2 run qrb_ros_audio_common audio_common_node_exec --ros-args -p Stream_type:="playback" -p action_name:="ros_audio_playback" -p topic_name:="ros_audio_data"
        (ssh) ros2 run qrb_ros_audio_common audio_common_node_exec --ros-args -p Stream_type:="capture" -p action_name:="ros_audio_capture" -p topic_name:="ros_audio_data"

After start two node, will start to action server, ros_audio_playback and ros_audio_capture.
Send goal to action server can open/start/mute/stop/close stream.

Client usesage
--------------

Open command, playback/capture from/to local file:

    .. code:: bash

        (ssh) ros2 action send_goal <action_name> qrb_ros_audio_common_msgs/action/AudioCommon "{
                audio_info: {
                    channels: 2,
                    sample_rate: 48000,
                    sample_format: 16
                  },
                  command: 'open',
                  volume: 100,
                  file_path: '/tmp/xxx.wav',
                  repeat: 1
                }"

<action_name> is passed by parameter action_name.
For playback from file audio_info is no need to pass. will overwrite by audio info read from file.
For Capture audio_info need pass.


Open command, playback/capture from/to topic:

    .. code:: bash

        (ssh) ros2 action send_goal <action_name> qrb_ros_audio_common_msgs/action/AudioCommon "{
                audio_info: {
                    channels: 2,
                    sample_rate: 48000,
                    sample_format: 16
                  },
                    command: 'open',
                    volume: 100,
                    topic_name: "pcm_topic",
                    pub_pcm: true,
              }"

for pcm topic, pub_pcm need set to true, and no need pass file_path.
Both playback and capture need pass audio_info.

If open command succeed, will return stream handle.


stop/mute/stop/close command:
    .. code:: bash

        (ssh) ros2 action send_goal <action_name> qrb_ros_audio_common_msgs/action/AudioCommon "{
                  command: "start",
                  stream_handle: <stream_handle>,
              }"
              ros2 action send_goal <action_name> qrb_ros_audio_common_msgs/action/AudioCommon "{
                  command: "mute",
                  mute: "true",
                  stream_handle: <stream_handle>,
              }"

              ros2 action send_goal <action_name> qrb_ros_audio_common_msgs/action/AudioCommon "{
                  command: "stop",
                  stream_handle: <stream_handle>,
              }"

              ros2 action send_goal <action_name> qrb_ros_audio_common_msgs/action/AudioCommon "{
                  command: "close",
                  stream_handle: <stream_handle>,
              }"

<stream_handle> is  return from open command.
