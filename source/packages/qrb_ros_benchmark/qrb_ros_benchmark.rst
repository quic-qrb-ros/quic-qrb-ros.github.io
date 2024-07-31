==============
|package_name|
==============

Supported Types
---------------

The following table lists current supported types:

.. list-table::
    :header-rows: 1

    * - Msg Type
      - Description

    * - `qrb_ros::transport::type::Image <https://github.com/quic-qrb-ros/qrb_ros_transport>`__
      - `Zero copy with qrb_ros_transport`
    * - `qrb_ros::transport::type::Imu <https://github.com/quic-qrb-ros/qrb_ros_transport>`__
      - `Zero copy with qrb_ros_transport`
    * - `dmabuf_transport::type::Image <https://github.com/quic-qrb-ros/dmabuf_transport>`__
      - `Zero copy with dmabuf_transport`
    * - `dmabuf_transport::type::PointCloud2 <https://github.com/quic-qrb-ros/dmabuf_transport>`__
      - `Zero copy with dmabuf_transport`
    * - `sensor_msgs::msg::Image <https://github.com/ros2/common_interfaces/blob/rolling/sensor_msgs/msg/Imu.msg>`__
      - `Support intra-process communication`
    * - `sensor_msgs::msg::CompressedImage <https://github.com/ros2/common_interfaces/blob/rolling/sensor_msgs/msg/CompressedImage.msg>`__
      - `Support intra-process communication`
    * - `qrb_ros_tensor_list_msgs::msg::TensorList <https://github.com/quic-qrb-ros/qrb_ros_tensor_list_msgs/blob/main/msg/TensorList.msg>`__
      - `Support intra-process communication`

.. |package_name| replace:: ``qrb_ros_benchnark``