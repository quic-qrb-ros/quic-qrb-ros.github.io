===============
Getting started
===============

The QRB ROS suite provides ROS interfaces for developers to access
Qualcomm robotics platform capabilities, including camera, sensors and so on.

QRB ROS uses standard ROS interfaces on input and output topics, making
it extremely easy to use as a drop-in replacement for widely-used, CPU-based ROS
implementations familiar to robotics developers.

Platform setup
-------------------
This information provides instructions on how to download and use the robotics prebuilt package, allowing you to quickly set up the software and hardware environment to get an out-of-the-box experience.

.. toctree::
   :maxdepth: 1

    QIRP SDK setup <./environment_setup.rst>

.. toctree::
   :maxdepth: 1

    Docker setup <./docker_setup.rst>

Tutorial
-------------------
This tutorial teaches you how to run the first QRB ROS application. It is intended for users who want to quickly run the camera on the board and use Rviz on an Ubuntu PC on the same LAN to see the real-time output of the camera.

.. toctree::
   :maxdepth: 1

    First example <./first_example.rst>


.. warning::

   QRB ROS packages have **ONLY** been tested against ROS 2 Humble. Other ROS 2
   versions are **NOT YET** supported.
