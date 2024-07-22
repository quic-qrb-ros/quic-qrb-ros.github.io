First Example
#############

.. contents:: Table of Contents
   :depth: 2
   :local:

This tutorial will teach you how to run the first QRB ROS application.
It is intended for users who want to quickly running the camera on the board 
and being able to use rviz on UbuntuPC on the same LAN to see the real-time 
output of the camera.

Prerequisites
-------------

- Setup your environment

- Setup QIRP SDK

Running camera
--------------

Download Code
^^^^^^^^^^^^^

You need to create a path to store the code on the Host PC.

Then, you need to use these cmd to clone the code repository in this path.

.. code-block:: bash

    git clone https://github.com/quic-qrb-ros/lib_mem_dmabuf.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_transport.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_camera.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_colorspace_convert.git

Build
^^^^^

You need to set up qirp-sdk environment before build these code.

Then, you can use these cmd to build these code in QIRP SDK.

.. code-block:: bash

    export AMENT_PREFIX_PATH="${OECORE_TARGET_SYSROOT}/usr;${OECORE_NATIVE_SYSROOT}/usr"
    export PYTHONPATH=${PYTHONPATH}:${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages

    colcon build --merge-install --cmake-args \
      -DPython3_ROOT_DIR=${OECORE_TARGET_SYSROOT}/usr \
      -DPython3_NumPy_INCLUDE_DIR=${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages/numpy/core/include \
      -DSYSROOT_LIBDIR=${OECORE_TARGET_SYSROOT}/usr/lib \
      -DSYSROOT_INCDIR=${OECORE_TARGET_SYSROOT}/usr/include \
      -DPYTHON_SOABI=cpython-310-aarch64-linux-gnu -DCMAKE_STAGING_PREFIX=$(pwd)/install \
      -DCMAKE_PREFIX_PATH=$(pwd)/install/share \
      -DBUILD_TESTING=OFF

Push & Install
^^^^^^^^^^^^^^

you can use these cmd to push & install the output on the device.

.. code-block:: bash

    cd install
    tar czvf qrb_ros_example.tar.gz lib share
    scp qrb_ros_example.tar.gz root@[ip-addr]:/opt/
    ssh root@[ip-addr]
    (ssh) tar -zxf /opt/qrb_ros_example.tar.gz -C /opt/qcom/qirp-sdk/usr/

Run
^^^

Firstly, we need to create ``launch.py`` file that looks like:

.. code-block:: python

    import launch
    import os
    from ament_index_python.packages import get_package_share_directory
    from launch_ros.actions import ComposableNodeContainer
    from launch_ros.actions import Node
    from launch_ros.descriptions import ComposableNode

    def generate_launch_description():
        camera_info_config_file_path = os.path.join(
            get_package_share_directory('qrb_ros_camera'),
            'config', 'camera_info_imx577.yaml'
        )
        camera_info_path = camera_info_config_file_path
        print(camera_info_path)
        """Generate launch description with multiple components."""
        container = ComposableNodeContainer(
            name='my_container',
            namespace='',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[
                ComposableNode(
                    package='qrb_ros_camera',
                    plugin='qrb_ros::camera::CameraNode',
                    name='camera_node',
                    remappings=[('/image', '/image_raw')],
                    parameters=[{
                        'camera_info_path': camera_info_path,
                        'fps': 30,
                        'width': 1920,
                        'height': 1080,
                        'cameraId': 0,
                        'publish_latency_type': 1,
                    }]
                ),
                ComposableNode(
                    package='qrb_ros_colorspace_convert',
                    plugin='qrb_ros::colorspace_convert::ColorspaceConvertNode',
                    parameters=[{
                        'conversion_type': "nv12_to_rgb8",
                        'latency_fps_test': False,
                    }],
                    extra_arguments=[{'use_intra_process_comms': True, 'log_level': 'INFO'}],
                )
            ],
            output='screen',
        )

        return launch.LaunchDescription([container,
            Node(
                package='image_transport',
                executable='republish',
                output='screen',
                name='republish_node',
                arguments=[
                    'raw',  # Input
                    'compressed',  # Output
                ], 
                remappings=[
                    ('in', '/image'),
                    ('out/compressed', '/image_compressed'),
                ]
            ),
        ])


Secondly, we need to push this file to device.

.. code-block:: bash

    scp launch.py root@[ip-addr]:/opt/

Thirdly, we will use these cmd to run it on the device.

.. code-block:: bash

    ssh root@[ip-addr]
    (ssh) export XDG_RUNTIME_DIR=/dev/socket/weston/
    (ssh) export WAYLAND_DISPLAY=wayland-1
    (ssh) export HOME=/opt
    (ssh) source /opt/qcom/qirp-sdk/qirp-setup.sh
    (ssh) export ROS_DOMAIN_ID=1
    (ssh) source /usr/bin/ros_setup.bash
    (ssh) ros2 launch /opt/launch.py

Get the realtime image in Ubuntu PC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need to prepare an Ubuntu PC to be on the same LAN as the device.

We need to install ROS2 Desktop on Ubuntu PC follow `Install ROS <https://docs.ros.org/en/rolling/Installation/Ubuntu-Install-Debians.html>`__

Then, we can use these cmd in the first terminal to decompressed the image.

.. code-block:: bash

    source /opt/ros/<ros-version>/setup.sh
    export ROS_DOMAIN_ID=1
    ros2 run image_transport republish compressed raw --ros-args -r in/compressed:=/image_compressed -r out:=/image_repub

Last, we can can obtain real-time images from image_repub topic in rviz2.
