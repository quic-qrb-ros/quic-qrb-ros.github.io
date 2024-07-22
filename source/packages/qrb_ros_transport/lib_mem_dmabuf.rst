==============
|package_name|
==============

Overview
--------

lib_mem_dmabuf is a library for access and interact with Linux DMA
buffer.

Feature highlights
~~~~~~~~~~~~~~~~~~

-  Alloc and destroy DMA buffer
-  Return file descriptor (fd) associated with DMA buffer
-  DMA buffer synchronization operation
-  Auto release DMA buffer and fd when leave code scope
-  Register DMA buffer release callback

Quickstart
----------

1. Add dependencies in your package.xml

   .. code:: xml

      <depend>lib_mem_dmabuf</depend>

2. Use ament_cmake_auto to find dependencies in your CMakeLists.txt

   .. code:: cmake

      find_package(ament_cmake_auto REQUIRED)
      ament_auto_find_build_dependencies()

3. Using lib_mem_dmabuf to alloc DMA buffer

   .. code:: cpp

      #include "lib_mem_dmabuf/dmabuf.hpp"

      // alloc dmabuf with size and DMA heap name
      auto buf = lib_mem_dmabuf::DmaBuffer::alloc(size, "/dev/dma_heap/system");

      // get fd of buffer
      std::cout << "fd: " << buf->fd() << std::endl;

      // get CPU accessable address
      if (buf->map()) {
        std::cout << "CPU address: " << buf->addr() << std::endl;
        // read / write buffer
        // ...
      }

      // buf will auto release when leave scope

API
---

.. list-table::
    :header-rows: 1
    :widths: 3 1 1 1

    * - Function
      - Parameters
      - Return Value
      - Description

    * - DmaBuffer::DmaBuffer(int fd, std::size_t size)
      - fd: dmabuf fd, size: dmabuf size
      -
      - Constructor for DmaBuffer class

    * - static std::shared_ptr<DmaBuffer> alloc(std::size_t size, const std::string& heap_name)
      - size: buffer size (bytes), heap_name: dmabuf heap name
      - Allocated buffer pointer
      - Alloc dmabuf with size and heap name

    * - bool DmaBuffer::release()
      -
      -
      - Release dmabuf

    * - bool DmaBuffer::map()
      -
      -
      - Description

    * - bool DmaBuffer::unmap()
      -
      -
      - Description

    * - bool DmaBuffer::sync_start()
      -
      -
      - Description

    * - bool DmaBuffer::sync_end()
      -
      -
      - Description

    * - bool DmaBuffer::set_auto_release(bool auto_release)
      - auto_release: whether to auto release fd when Dmabuf object destroy
      -
      - Set auto release dmabuf fd when destroy

    * - void DmaBuffer::set_destroy_callback( std::function<void(std::shared_ptr<DmaBuffer>)> cb);
      - cb: callback function when dmabuf destroy
      -
      - Set destroys callback function

    * - bool DmaBuffer::set_data(void* data, std::size_t size, std::size_t offset = 0)
      - data: data be saved, size: data size, offset: offset to dmabuf address
      -
      - Set data into dmabuf

    * - int DmaBuffer::fd() const
      -
      - Dmabuf file descriptor
      - Get dmabuf fd

    * - int DmaBuffer::size() const
      -
      - Dmabuf size
      - Get dmabuf size

    * - void* DmaBuffer::addr()
      -
      - Dmabuf CPU mapped address
      - Get dmabuf CPU memory mapped address

.. |package_name| replace:: ``lib_mem_dmabuf``
