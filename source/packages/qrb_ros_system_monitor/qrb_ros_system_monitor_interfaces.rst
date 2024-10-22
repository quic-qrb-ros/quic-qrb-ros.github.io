==============
|package_name|
==============

|package_name| defines ROS messages for publishing system informations.

Message Definitions
-------------------

qrb_ros_system_monitor::msg::CpuInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

  float32 usage
  uint64 user
  uint64 nice
  uint64 system
  uint64 idle
  uint64 iowait
  uint64 irq
  uint64 softirq
  uint64 steal
  uint64 guest
  uint64 guest_nice

qrb_ros_system_monitor::msg::MemoryInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

  # memory information
  # provided by `cat /proc/meminfo`
  # unit: kB
  uint64 mem_total
  uint64 mem_free
  uint64 mem_available
  uint64 buffers
  uint64 cached
  uint64 swap_total
  uint64 swap_free

qrb_ros_system_monitor::msg::DiskInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

  FileSystem[] fslist

qrb_ros_system_monitor::msg::FileSystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

  # provided by `df -BM`
  string fs
  string type
  uint32 total    # MB
  uint32 used     # MB
  uint32 avail    # MB
  uint32 use_rate
  string mount

qrb_ros_system_monitor::msg::SwapInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

  SwapItem[] swaplist

qrb_ros_system_monitor::msg::SwapItem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

  string file_name
  string type
  uint64 size
  uint64 used
  uint32 priority

qrb_ros_system_monitor::msg::SystemInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

  ---
  uint32 cpu_count
  uint32 mem_total    # MB
  uint32 swap_total   # MB
  uint64 disk_total   # MB


.. |package_name| replace:: ``qrb_ros_system_monitor_interfaces``
