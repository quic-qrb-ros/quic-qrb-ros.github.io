===============
Getting Started
===============

The QRB ROS suite provides ROS interfaces for developers to access 
Qualcomm robotics platform capability. Such as Camera, sensors etc.

QRB ROS uses standard ROS interfaces on input and output topics, making
it extremely easy to use as a drop-in replacement for commonly-used, CPU-based ROS
implementations familiar to robotics developers.

Platform Setup
-------------------
This information provides instructions on how to download and use the robotics prebuilt package, allowing you to quickly setup software and hardware environment to get an out-of-the-box experience.

.. toctree::
   :maxdepth: 1
   
    Environment Setup <./environment_setup.rst>

Tutorial
-------------------
This tutorial will teach you how to run the first QRB ROS application. It is intended for users who want to quickly running the camera on the board and being able to use rviz on UbuntuPC on the same LAN to see the real-time output of the camera.

.. toctree::
   :maxdepth: 1
   
    First Example <./first_example.rst>


.. warning::

   QRB ROS packages have **ONLY** been tested against ROS 2 Humble. Other ROS 2
   versions are **NOT YET** supported.
