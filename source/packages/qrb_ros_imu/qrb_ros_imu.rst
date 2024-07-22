==============
|package_name|
==============

Quickstart
----------

This quickstart shows how to run the imu ros node on the device.

.. code:: bash

   (ssh) ros2 run qrb_ros_imu imu_node

API
----

Overview
^^^^^^^^

This API shows the topic and parameter detail.

Available Components
^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :header-rows: 1

    * - Component
      - Topics Published
      - Parameters

    * - ``ImuNode``
      - ``imu``: publish the imu data
      - ``debug``: show the imu driver to ROS Node 's latency.

.. |package_name| replace:: ``qrb_ros_imu``