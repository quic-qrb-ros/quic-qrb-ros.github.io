========================
``qrb_audio_common_lib``
========================

Overview
---------

qrb_audio_common_lib is a library used by qrb_ros_audio_common. It is implemented based on PulseAudio’s API for playback and capture.

Data Struct
-----------

1. audio_stream_info

.. list-table::
    :header-rows: 1

    * - Member types
      - Member name
      - description

    * - uint8_t
      - format
      - PCM format, 8bit, 16bit, 24bit, 32bit

    * - uint32_t
      - rate
      - samplerate for  stream 8000, 16000, 32000, 44100, 48000...

    * - uint8_t
      - channels
      - channels for stream, 1, 2...

    * - stream_type
      - type
      - stream type, StreamPlayback or StreamCapture

    * - string
      - file_path
      - file_path to open/store

    * - uint8_t
      - volume
      - volume for stream, from 1 to 100

    * - bool
      - need_timestamp
      - need notify timestamp for stream

    * - bool
      - pcm_mode
      - Whether publish pcm data on topic or manual write playback data.

    * - int32_t
      - repeat
      - repeat count, 0 for no repeat, -1 for unlimited.

API
---

.. list-table::
    :header-rows: 1

    * - Function Name
      - Comment

    * - uint32_t audio_stream_open(const audio_stream_info & stream_info,stream_event_callback_func event_callback);
      - open a stream, and configure stream with stream_info, open succeed will return stream handle.
        ``stream_info``: stream info for configure stream.
        ``event_callback``: callback for stream to notify stream events.

    * - int audio_stream_start(uint32_t stream_handle)
      - start a stream, succeed return 0, failed return error code.
        ``stream_handle``: stream handle for operate stream.

    * - int audio_stream_mute(uint32_t stream_handle,  bool mute)
      - mute a stream, succeed return 0, failed return error code.
        ``stream_handle``: stream handle for operate stream.
        ``mute``: true for mute, false for unmute.

    * - int audio_stream_stop(uint32_t stream_handle)
      - stop a stream, succeed return 0, failed return error code.
        ``stream_handle``: stream handle for operate stream.

    * - int audio_stream_close(uint32_t stream_handle)
      - close a stream, succeed return 0, failed return error code.
        ``stream_handle``: stream handle for operate stream.

    * - int audio_stream_write(uint32_t stream_handle, size_t length, void * buf)
      - write data to stream, succeed return bytes written, failed return error code.
        ``stream_handle``: stream handle for operate stream.
        ``length``: length for data.
        ``buf``: point to data start.
