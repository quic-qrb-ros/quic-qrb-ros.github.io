=====================
qrb_ros_audio_service
=====================

Overview
--------

It is the entry point for ROS to provide audio capabilities.

The communication mode for Playback and Record:

.. image:: ../../resources/qrb_ros_docs/packages/qrb_ros_audio_service/playback_record_communication_mode.png
  :align: center
  :alt: aha? why no image? try reflash your website.

``AudioServer`` is a ROS service server which provide interface for client.
The interface is `qrb_ros_audio_serivce_msgs <https://github.qualcomm.com/QUIC-QRB-ROS/qrb_ros_interfaces/tree/main/qrb_ros_audio_common_msgs>`_.

``AudioCommonClient`` is a ROS action client which invoke qrb_ros_audio_common to implement playback and record function.
The interface is `qrb_ros_audio_common_msgs <https://github.qualcomm.com/QUIC-QRB-ROS/qrb_ros_interfaces/tree/main/qrb_ros_audio_service_msgs>`_.

API
---
AudioServer

.. list-table::
    :header-rows: 1

    * - Function Name
      - Comment

    * - void shutdown_callback()
      - Release resource when got ctrl+c.

AudioCommonClient

.. list-table::
    :header-rows: 1

    * - Function Name
      - Comment

    * - rclcpp_action::ClientGoalHandle<AudioCommonAction>::WrappedResult AudioCommonClient::send_and_wait(rclcpp_action::Client<AudioCommonAction>::SharedPtr client, std::shared_ptr<qrb_ros_audio_common_msgs::action::AudioCommon_Goal_<std::allocator<void>>>
        goal_msg)
      - Send request to qrb_ros_audio_common and wait for response.
        ``client``: response from qrb_ros_audio_common.
        ``goal_msg``: request send to qrb_ros_audio_common.
        ``Return``: response from qrb_ros_audio_common.

    * - static bool stream_cb(const void * const payload, StreamCommand cmd, uint32_t & audio_comm_handle)
      - Callback registers with qrb_audio_manager and is used for communication between qrb_audio_manager and AudioCommonClient.
        ``payload``: request from qrb_audio_manager.
        ``cmd``: command from qrb_audio_manager.
        ``audio_comm_handle``: stream is created in qrb_ros_audio_common.
        ``Return``: true is success, false is failed.
