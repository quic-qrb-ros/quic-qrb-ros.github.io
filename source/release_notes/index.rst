=============
Release Notes
=============

.. list-table::
   :header-rows: 1

   * - Version
     - Release Date
   * - Pre-alpha
     - 2024-07-01

QRB ROS Pre-alpha July, 30, 2024
---------------------------------

This inaugural release of QRB ROS offers enhanced Qualcomm hardware acceleration for robots, introducing new features such as:

What's New
~~~~~~~~~~

Updates including:

- Introduction of the new repository `qrb_ros_imu`, enabling low-latency access to the IMU sensor mounted on the Sensor DSP.
- Launch of the new repository `qrb_ros_transport`, featuring a hardware-accelerated transport mechanism based on dmabuf.
- Release of the new repository `qrb_ros_camera`, facilitating easy access to the Qualcomm CameraX system via ROS, with hardware acceleration support.
- Debut of the new repository `qrb_ros_colorspace_convert`, designed to convert YUV to RGB using Qualcomm GPU, with hardware acceleration support.


Limitations
~~~~~~~~~~~

This release has the following known limitations, with workarounds available in the troubleshooting section:

- qrb_ros_imu includes Imu type adapter, it will be move to qrb_ros_transport
