==================
``sensor_service``
==================

Overview
---------

sensor service is a system service, which will using fastrpc to get the sensor data 's fd in dsp side
and create a local socket to send this fd to client side.

.. Note:: When we want to change the sensor 's frame rate, we need modify the configuration file in ``/etc/sensors_info.conf`` and restart sensor service.

restart sensor service cmd

    .. code:: bash

        (ssh) systemctl restart sensor-service

Parameter List
--------------

.. list-table::
    :header-rows: 1

    * - Parameter Name
      - Comment

    * - sensor_type
      - Currently, we only support IMU sensor in sensor service, which need write the gyro & accel sensor type.
        ``Note``: If different sensors are configured with the same hardware, the frequency of hardware sampling will be the final set.

    * - frame_rate
      - Because sensors support specific frame rates on different platforms, if a frame rate that does not match the specific frequency is set, it will automatically adapt to a frame rate one level higher than this
