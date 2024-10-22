==============
|package_name|
==============

`QRB ROS System Monitor <https://github.com/quic-qrb-ros/qrb_ros_system_monitor>`__ is a ROS package to publish system informations.

API
---

.. list-table::
    :header-rows: 1

    * - Interface
      - Component

    * - /cpu
      - qrb_ros_system_monitor::CpuMonitor

    * - /memory
      - qrb_ros_system_monitor::MemoryMonitor

    * - /disk
      - qrb_ros_system_monitor::DiskMonitor

    * - /swap
      - qrb_ros_system_monitor::SwapMonitor

    * - /temperature
      - qrb_ros_system_monitor::TemperatureMonitor

    * - /battery
      - qrb_ros_system_monitor::BatteryMonitor

    * - /system_info_server
      - qrb_ros_system_monitor::SystemInfoServer


Parameters
----------

.. list-table::
    :header-rows: 1

    * - Parameter
      - Type
      - Default Value
      - Description

    * - interval
      - int
      - 5
      - Sampling interval time (seconds)

.. |package_name| replace:: ``qrb_ros_system_monitor``
