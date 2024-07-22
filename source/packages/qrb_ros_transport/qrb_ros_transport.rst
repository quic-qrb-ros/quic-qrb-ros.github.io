==============
|package_name|
==============

Quickstart
----------

1. Add dependencies in your package.xml

   .. code:: xml

      <depend>qrb_ros_transport</depend>

2. Use ament_cmake_auto to find dependencies in your CMakeLists.txt

   .. code:: cmake

      find_package(ament_cmake_auto REQUIRED)
      ament_auto_find_build_dependencies()

3. Using adapted types in your ROS node

   .. code:: cpp

      #include "qrb_ros_transport/type/image.hpp"

      // create message
      auto msg = std::make_unique<qrb_ros::transport::type::Image>();
      msg->header = std_msgs::msg::Header();
      msg->width = width;
      msg->height = height;
      msg->encoding = "nv12";

      // alloc dmabuf for message
      auto dmabuf = lib_mem_dmabuf::DmaBuffer::alloc(size, "/dev/dma_heap/system");
      // ... set data to dmabuf
      msg->dmabuf = dmabuf;

      // publish message
      pub->publish(std::move(msg));

Supported Types
---------------

The following table lists current supported types:

.. list-table::
    :header-rows: 1

    * - QRB ROS Transport Type
      - ROS Interface

    * - `qrb_ros::transport::type::Image <https://github.com/quic-qrb-ros/qrb_ros_transport/tree/main//include/qrb_ros_transport/type/image.hpp>`__
      - `sensor_msgs::msg::Image <https://github.com/ros2/common_interfaces/blob/rolling/sensor_msgs/msg/Image.msg>`__
    * - `qrb_ros::transport::type::Imu <https://github.com/quic-qrb-ros/qrb_ros_transport/tree/main//include/qrb_ros_transport/type/imu.hpp>`__
      - `sensor_msgs::msg::Imu <https://github.com/ros2/common_interfaces/blob/rolling/sensor_msgs/msg/Imu.msg>`__

.. |package_name| replace:: ``qrb_ros_transport``
