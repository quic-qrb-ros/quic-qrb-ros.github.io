==============
|package_name|
==============

dmabuf_transport is a package for zero-copy transport ROS message with
Linux dma-buf file descriptor.

Overview
--------

`Dmabuf Transport <https://github.com/quic-qrb-ros/dmabuf_transport>`__
provides a way to share data between different hardware accelerators and
different ROS nodes with zero-copy.

It is built on ROS 2 `Type
Adaption <https://ros.org/reps/rep-2007.html>`__. It allows us to define
methods for serializing directly to the user requested type, and/or
using that type in intra-process communication without ever converting
it.

QuickStart
----------

1. Add dependency in package.xml

   .. code:: xml

      <depend>dmabuf_transport</depend>

2. Add dependency in CMakeLists.txt

   .. code:: cmake

      find_package(dmabuf_transport REQUIRED)

      ament_target_dependencies(${PROJECT_NAME}
        # ...
        dmabuf_transport
      )

3. Zero-copy transport dmabuf_transport types

   .. code:: cpp

      #include "dmabuf_transport/type/image.hpp"
      // create message
      auto msg = std::make_unique<dmabuf_transport::type::Image>();
      msg->header = std_msgs::msg::Header();
      // save message data to dmabuf
      auto dmabuf = lib_mem_dmabuf::DmaBuffer::alloc(1024, "/dev/dma_heap/system");
      // ... set data
      msg->dmabuf = dmabuf;

      // publish message
      pub_->publish(std::move(msg));

-  Check `test <https://github.com/quic-qrb-ros/dmabuf_transport/tree/main/test>`__ directory to find more details.


Supported Types
---------------

The following table lists current supported types:

.. list-table::
    :header-rows: 1

    * - Dmabuf Transport Type
      - ROS Interface

    * - `dmabuf_transport::type::Image <https://github.com/quic-qrb-ros/dmabuf_transport/tree/main/include/dmabuf_transport/type/image.hpp>`__
      - `sensor_msgs::msg::Image <https://github.com/ros2/common_interfaces/blob/rolling/sensor_msgs/msg/Image.msg>`__
    * - `dmabuf_transport::type::PointCloud2 <https://github.com/quic-qrb-ros/dmabuf_transport/tree/main/include/dmabuf_transport/type/point_cloud2.hpp>`__
      - `sensor_msgs::msg::PointCloud2 <https://github.com/ros2/common_interfaces/blob/rolling/sensor_msgs/msg/PointCloud2.msg>`__


.. |package_name| replace:: ``dmabuf_transport``
