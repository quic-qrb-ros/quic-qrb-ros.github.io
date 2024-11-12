==============
|package_name|
==============

Quickstart
----------

This quickstart shows how to run the Manipulator ros node on the device.

.. code:: bash

   (ssh) ros2 launch qrb_ros_manipulator  manipulator_controller.launch.py

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

    * - ``qrb_ros_manipulator node``
      - ``manipulator``: provides services to control robot ARM.
      - ``testnode``: Send base command to control robot ARM.

.. |package_name| replace:: ``qrb_ros_manipulator``