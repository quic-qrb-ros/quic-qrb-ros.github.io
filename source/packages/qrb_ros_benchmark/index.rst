=================
QRB ROS Benchmark
=================

Overview
--------

`QRB ROS Benchmark <https://github.com/quic-qrb-ros/qrb_ros_benchmark>`__ is a ros package
that extends the functionality of open source ``ros2_benchmark`` package.

QRB ROS Benchmark supports testing the performance of ROS nodes are accelerated by `dmabuf_transport <https://github.com/quic-qrb-ros/qrb_ros_transport>`__ and
`qrb_ros_transport <https://github.com/quic-qrb-ros/dmabuf_transport>`__ function.
dmabuf_transport and qrb_ros_transport provides type adaption and intra process communication to optimize message formats and dramatically accelerate
communication between participating nodes.

Build
-----

Currently, we only support use QCLINUX to build

1. Setup environments follow this document 's `Set up the cross-compile environment <https://docs.qualcomm.com/bundle/publicresource/topics/80-65220-2/develop-your-first-application_6.html>`__.

2. Create ``ros_ws`` directory in ``<qirp_decompressed_workspace>/qirp-sdk/``

3. Clone this repository under ``<qirp_decompressed_workspace>/qirp-sdk/ros_ws``
    
.. code:: bash

    git clone https://github.com/quic-qrb-ros/lib_mem_dmabuf.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_imu.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_transport.git
    git clone https://github.com/quic-qrb-ros/dmabuf_transport.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_tensor_list_msgs.git
    git clone https://github.com/NVIDIA-ISAAC-ROS/ros2_benchmark.git
    git clone https://github.com/quic-qrb-ros/qrb_ros_benchmark.git

4. Add dependencies in ``ros2_benhcmark/ros2_benchmark/CMakeLists.txt`` file

.. code:: bash

    find_package(rosbag2_compression REQUIRED)

5. Modify line 58 of the ``/qirp-sdk/toolchain/install_dir/sysroots/armv8-2a-qcom-linux/usr/share/rosbag2_compression_zstd/cmake/export_rosbag2_compression_zstdExport.cmake`` file to:

.. code:: bash

    INTERFACE_LINK_LIBRARIES "rcpputils::rcpputils;rosbag2_compression::rosbag2_compression;${_IMPORT_PREFIX}/lib/libzstd.so"

6. Build this project

.. code:: bash
    
    export AMENT_PREFIX_PATH="${OECORE_TARGET_SYSROOT}/usr;${OECORE_NATIVE_SYSROOT}/usr"
    export PYTHONPATH=${PYTHONPATH}:${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages

    colcon build --merge-install --cmake-args \
      -DPython3_ROOT_DIR=${OECORE_TARGET_SYSROOT}/usr \
      -DPython3_NumPy_INCLUDE_DIR=${OECORE_TARGET_SYSROOT}/usr/lib/python3.10/site-packages/numpy/core/include \
      -DPYTHON_SOABI=cpython-310-aarch64-linux-gnu -DCMAKE_STAGING_PREFIX=$(pwd)/install \
      -DCMAKE_PREFIX_PATH=$(pwd)/install/share \
      -DBUILD_TESTING=OFF

7. Push to the device & Install

.. code:: bash
    
    cd <qirp_decompressed_workspace>/qirp-sdk/ros_ws/install
    tar czvf qrb_ros_benchmark.tar.gz lib share
    scp qrb_ros_benchmark.tar.gz root@[ip-addr]:/opt/
    ssh root@[ip-addr]
    (ssh) tar -zxf /opt/qrb_ros_benchmark.tar.gz -C /opt/qcom/qirp-sdk/usr/

Run
---

QRB ROS Benchmark supports running it directly from the command with test script, taking the `qrb_ros_imu <https://github.com/quic-qrb-ros/qrb_ros_imu>`__ becnhamk test as an example.

1. Source this file to set up the environment on your device:

.. code:: bash

    ssh root@[ip-addr]
    (ssh) export HOME=/opt
    (ssh) source /opt/qcom/qirp-sdk/qirp-setup.sh
    (ssh) export ROS_DOMAIN_ID=xx
    (ssh) source /usr/bin/ros_setup.bash

2. Use this command to run this package with test script `qrb_ros_imu_benchmark.py <https://github.com/quic-qrb-ros/qrb_ros_benchmark/scripts/qrb_ros_imu_benchmark.py>`__ file.

.. code:: bash

    (ssh) launch_test qrb_ros_imu_benchmark.py

3. After the benchmark test is completed, the performance measurement results will be displayed on the terminal.
And will generate a json file containing the test results and metadata (such as system information, benchmark configuration). the result json file path: /tmp/xxx.json.

The benchmark test result example: `qrb_ros_imu_qcm6490.json <https://github.com/quic-qrb-ros/qrb_ros_benchmark/results/qrb_ros_imu_qcm6490.json>`__.

.. code:: bash

    "qrb_ros_imu": {
      "BasicPerformanceMetrics.RECEIVED_DURATION": 5019.522623697917,
      "BasicPerformanceMetrics.MEAN_PLAYBACK_FRAME_RATE": 202.39100914116554,
      "BasicPerformanceMetrics.MEAN_FRAME_RATE": 202.4096863814278,
      "BasicPerformanceMetrics.NUM_MISSED_FRAMES": 0.0,
      "BasicPerformanceMetrics.NUM_FRAMES_SENT": 1016.0,
      "BasicPerformanceMetrics.FIRST_SENT_RECEIVED_LATENCY": 1.6370442708333333,
      "BasicPerformanceMetrics.LAST_SENT_RECEIVED_LATENCY": 1.3841145833333333,
      "BasicPerformanceMetrics.FIRST_INPUT_LATENCY": 1.6370753333333334,
      "BasicPerformanceMetrics.LAST_INPUT_LATENCY": 1.3841233333333334,
      "BasicPerformanceMetrics.MAX_LATENCY": 5.016393,
      "BasicPerformanceMetrics.MIN_LATENCY": 0.644319,
      "BasicPerformanceMetrics.MEAN_LATENCY": 1.8897658450305777,
      "BasicPerformanceMetrics.MAX_JITTER": 5.287109375,
      "BasicPerformanceMetrics.MIN_JITTER": 0.0,
      "BasicPerformanceMetrics.MEAN_JITTER": 1.1905905217578896,
      "BasicPerformanceMetrics.STD_DEV_JITTER": 1.0327541582660051
    },

    "ResourceMetrics.BASELINE_OVERALL_CPU_UTILIZATION": 12.5,
    "ResourceMetrics.MAX_OVERALL_CPU_UTILIZATION": 25.0,
    "ResourceMetrics.MIN_OVERALL_CPU_UTILIZATION": 0.0,
    "ResourceMetrics.MEAN_OVERALL_CPU_UTILIZATION": 3.3015959588417196,
    "ResourceMetrics.STDDEV_OVERALL_CPU_UTILIZATION": 4.361769437087449,


4. How to customize a test scripts, the test script example: `qrb_ros_imu_benchmark.py <https://github.com/quic-qrb-ros/qrb_ros_benchmark/scripts/qrb_ros_imu_benchmark.py>`__.

Config ``qrb_ros::imu::ImuComponent`` and ``qrb_ros::benchmark::QrbMonitorNode`` plugins.
set msg type on QrbMonitorNode plugin by ``monitor_data_format``, and remappings topic name to create pipeline:

.. code:: bash

    qrb_ros_imu_node = ComposableNode(
        name='QrbRosIMU',
        namespace=TestQrbRosImuNode.generate_namespace(),
        package='qrb_ros_imu',
        plugin='qrb_ros::imu::ImuComponent',
        remappings=[('imu', '/imu_raw')]
    )

    qrb_ros_monitor_node = ComposableNode(
        name='QrbMonitorNode',
        namespace=TestQrbRosImuNode.generate_namespace(),
        package='qrb_ros_benchmark',
        plugin='qrb_ros::benchmark::QrbMonitorNode',
        parameters=[{
            'monitor_index': 1,
            'monitor_data_format': 'qrb_ros/transport/type/Imu',
        }],
        remappings=[('output', '/imu_raw')]
    )


set benchmark test configuration parameters:

.. code:: bash

    config = ROS2BenchmarkConfig(
        benchmark_name='Qrb Ros Imu Live Benchmark',
        benchmark_mode=BenchmarkMode.LIVE,
        benchmark_duration=5,
        test_iterations=5,
        collect_start_timestamps_from_monitors=True,
        monitor_info_list=[
            MonitorPerformanceCalculatorsInfo(
                'monitor_node1',
                [BasicPerformanceCalculator({
                    'report_prefix': 'qrb_ros_imu',
                    'message_key_match': True
                })])
        ]
    )

The following table lists important benchmark configuration parameters:

.. list-table::
    :header-rows: 1

    * - Configuration Parameters
      - Description

    * - benchmark_mode
      - Benchmark mode for how buffered messages should be played. Can be either of "TIMELINE", "LOOPING" or "SWEEPING".
    * - collect_start_timestamps_from_monitors
      - Collect start timestamps from the messages observed by monitors, should be true when Benchmark modeis TIMELINE.
    * - benchmark_duration
      - Duration, in seconds, for how long each benchmark should run.
    * - test_iterations
      - The number of test iterations.
    * - playback_message_buffer_size
      - The number of frames to be buffered, effective in "LOOPING" or "SWEEPING" mode.
    * - publisher_upper_frequency
      - Upper and lower bounds of peak throughput search window, effective in "LOOPING" or "SWEEPING" mode.
    * - publisher_lower_frequency
      - Upper and lower bounds of peak throughput search window, effective in "LOOPING" or "SWEEPING" mode.
    * - assets_root
      - The directory for storing assets, effective in "LOOPING" or "SWEEPING" mode.
    * - input_data_path
      - The path, relative to "assets_root", of the file (usually a rosbag) to beloaded by a data loader node, effective in "LOOPING" or "SWEEPING" mode.


Packages
--------

.. toctree::
   :maxdepth: 2

    qrb_ros_benchmark <./qrb_ros_benchmark>


Supported Platforms
-------------------

This package is designed and tested to be compatible with ROS 2 Humble
running on Qualcomm RB3 gen2.

+-------------------------------------------------+-------------------+
| Hardware                                        | Software          |
+=================================================+===================+
| `Qualcomm RB3                                   | LE.QCROBOTICS.1.0 |
| gen2 <https://www.qualcomm.com/d                |                   |
| eveloper/hardware/rb3-gen-2-development-kit>`__ |                   |
+-------------------------------------------------+-------------------+

Updates
-------

+-----------+--------------------------+
| Date      | Changes                  |
+-----------+--------------------------+
| 2024-7-16 | Initial release          |
+-----------+--------------------------+
