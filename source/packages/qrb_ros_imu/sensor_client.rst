=====================
``qrb_sensor_client``
=====================

Data Struct
-----------

1. sensors_event_t

.. list-table::
    :header-rows: 1

    * - Member types
      - Member name

    * - int64_t
      - timestamp

    * - sensors_vec_t
      - acceleration

    * - sensors_vec_t
      - gyro

2. sensors_vec_t

.. list-table::
    :header-rows: 1

    * - Member types
      - Member name

    * - float
      - x

    * - float
      - y

    * - float
      - z


API
---

.. list-table::
    :header-rows: 1

    * - Function Name
      - Comment

    * - bool CreateConnection()
      - Create connection with sensor service

    * - void DisconnectServer()
      - Destroy connection with sensor service

    * - bool GetImuData(sensors_event_t** accel_ptr, sensors_event_t** gyro_ptr, int32_t* sample_count)
      - Get Imu data.
        ``accel_ptr``: accel data 's ptr.
        ``gyro_ptr``: gyro data 's ptr.
        ``sample_count``: return available sample 's count.
