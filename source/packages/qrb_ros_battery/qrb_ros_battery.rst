==============
|package_name|
==============

Quickstart
----------

This quickstart shows how to run the battery ros node on the device.

.. code:: bash

   (ssh) ros2 run qrb_ros_battery battery_node

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

    * - ``battery_stats_publisher``
      - ``battery_stats``: publish the battery data.

.. |package_name| replace:: ``qrb_ros_battery``