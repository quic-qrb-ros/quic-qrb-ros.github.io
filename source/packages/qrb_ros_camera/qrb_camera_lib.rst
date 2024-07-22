=====================
``qrb_camera_lib``
=====================

Data Struct
-----------

+------------------------+-------------------+------------------+
| Struct Name            | Member types      | Member name      |
+------------------------+-------------------+------------------+
| CameraRos2CamConfig    | uint32_t          | pipeline_id      |
+                        +-------------------+------------------+
|                        | int32_t           | camera_id        |
+                        +-------------------+------------------+
|                        | uint32_t          | width            |
+                        +-------------------+------------------+
|                        | uint32_t          | height           |
+                        +-------------------+------------------+
|                        | uint32_t          | stride           |
+                        +-------------------+------------------+
|                        | uint32_t          | slice            |
+                        +-------------------+------------------+
|                        | std::string       | format           |
+                        +-------------------+------------------+
|                        | uint8_t           | fps              |
+                        +-------------------+------------------+
|                        | int32_t           | publish_freq     |
+                        +-------------------+------------------+
|                        | uint8_t           | latency_type     |
+------------------------+-------------------+------------------+
| CameraRos2Frame        | uint8_t*          | data             |
+                        +-------------------+------------------+
|                        |CameraRos2FrameInfo| info             |
+------------------------+-------------------+------------------+
| CameraRos2FrameInfo    | uint32_t          | pipeline_id      |
+                        +-------------------+------------------+
|                        | int32_t           | camera_id        |
+                        +-------------------+------------------+
|                        | uint32_t          | frame_id         |
+                        +-------------------+------------------+
|                        | uint64_t          | size             |
+                        +-------------------+------------------+
|                        | uint32_t          | width            |
+                        +-------------------+------------------+
|                        | uint32_t          | height           |
+                        +-------------------+------------------+
|                        | uint32_t          | stride           |
+                        +-------------------+------------------+
|                        | uint32_t          | slice            |
+                        +-------------------+------------------+
|                        | std::string       | format           |
+                        +-------------------+------------------+
|                        | int64_t           | timestamp        |
+                        +-------------------+------------------+
|                        | int64_t           | latency          |
+                        +-------------------+------------------+
|                        | uint8_t           | latency_type     |
+                        +-------------------+------------------+
|                        | int32_t           | fd               |
+------------------------+-------------------+------------------+
| CameraRos2Config       |CameraRos2CamConfig| m_cam_cfg        |
+------------------------+-------------------+------------------+


API
----

.. list-table::
    :header-rows: 1

    * - Function
      - Description

    * - QmmfRos2Pipeline * QmmfRos2Pipeline::create_instance(CameraRos2Config * cfg)
      - Create camera pipeline, start camera,start preview

    * - void QmmfRos2Pipeline::register_publish( CameraRos2MsgPublishFrameFunc publish)
      - bind camera node image publish callback
