=================
qrb_audio_manager
=================

Overview
--------

It creates stream based on client requests (PlaybackStream for playback, RecordThread for record),
provides operations on the stream, and maintains its lifecycle.

API
---
AudioManager

.. list-table::
    :header-rows: 1

    * - Function Name
      - Comment

    * - uint32_t create_playback_stream(std::string source, std::string coding_format, uint8_t volume, std::string play_mode, int8_t repeat)
      - Create playback stream, initialize stream configurations, then open it.
        ``source``: playback path (e.g. /tmp/clips.wav or build-in sound name).
        ``coding_format``: audio coding format (e.g. wav).
        ``volume``: playback volume [1~100].
        ``play_mode``: playback mode (step-by-step or one-touch).
        ``repeat``: -1:repeat, 0:once.
        ``Return``: stream_handle, indicates playback stream.

    * - uint32_t create_record_stream(uint32_t sample_rate, uint8_t channels, uint8_t sample_format, std::string coding_format, std::string source, bool pub_pcm)
      - Create record stream, initialize stream configurations, then open it.
        ``sample_rate``: sampling rate [Hz].
        ``channels``: number of channels.
        ``sample_format``: audio format (e.g. s16le).
        ``coding_format``: audio coding format (e.g. wav).
        ``source``: record path (e.g. /tmp/rec.wav).
        ``pub_pcm``: whether publish the recording data data on topic (/qrb_audiodata) (true:yes, false:no).
        ``Return``: stream_handle, indicates playback stream.

    * - bool start_stream(uint32_t stream_handle)
      - Start stream.
        ``stream_handle``: indicates stream.
        ``Return``: true is success, false is failed.

    * - bool stop_stream(uint32_t stream_handle)
      - Stop stream.
        ``stream_handle``: indicates stream.
        ``Return``: true is success, false is failed.

    * - bool release_stream(uint32_t stream_handle)
      - Close stream.
        ``stream_handle``: indicates stream.
        ``Return``: true is success, false is failed.

    * - bool mute_stream(uint32_t stream_handle)
      - Mute playback stream.
        ``stream_handle``: indicates stream.
        ``Return``: true is success, false is failed.

    * - const std::map<std::string, std::string> & get_buildin_sounds()
      - Get build-in sounds name.
        ``Return``: name of sounds. Key is sound name, value is the local path of sound.

    * - void clean()
      - Delete all streams.

Stream

.. list-table::
    :header-rows: 1

    * - Function Name
      - Comment

    * - bool open()
      - Open stream.
        ``Return``: true is success, false is failed.

    * - bool start()
      - Start stream.
        ``Return``: true is success, false is failed.

    * - bool stop()
      - Stop stream.
        ``Return``: true is success, false is failed.

    * - bool close()
      - Close stream.
        ``Return``: true is success, false is failed.

    * - const StreamConfigs & get_stream_configs()
      - Get stream's configs.
        ``Return``: stream's configs.

    * - bool get_domain_async_mode(uint8_t domain_id)
      - Domain is a ROS package that implements a particular clint request. For playback/record, the ROS package is qrb_ros_audio_common.
        async_mode indicate whether qrb_ros_manager needs to wait until result of calling domina.
        ``domain_id``: domain id, it's predefined. For playback/record, it's DOMAIN_ID_AUDIO_COMMON
        ``Return``: true is asynchronous mode (qrb_ros_manager don't need wait), false is synchronous mode.

    * - uint32_t get_domain_handle(uint8_t domain_id)
      - Domain handle is stream created in domain.
        ``domain_id``: domain id, it's predefined.
        ``Return``: domain handle.

    * - void set_domain_handle(uint8_t domain_id, uint32_t handle)
      - Set domain's handle.
        ``domain_id``: domain id, it's predefined.
        ``handle``: stream created in domain.

    * - static void register_callback(int domain_id, std::function<bool(const void * const, StreamCommand, uint32_t &)> cb, bool use_async)
      - A ROS package call it to register itself as a domain.
        ``cb``: callback function in ROS package.
        ``use_async``: whether qrb_ros_manager needs to wait until result of calling a ROS package.

    * - std::function<bool(const void * const, StreamCommand, uint32_t &)> get_domain_cb(uint8_t domain_id)
      - Get a domain's callback function.
        ``domain_id``: domain id, it's predefined.
        ``Return``: a domain's callback function.

PlaybackStream

.. list-table::
    :header-rows: 1

    * - Function Name
      - Comment

    * - bool set_mute(bool mute)
      - Set mute for playback stream.
        ``mute``: true is mute, false is unmute.
        ``Return``: true is success, false is failed.
