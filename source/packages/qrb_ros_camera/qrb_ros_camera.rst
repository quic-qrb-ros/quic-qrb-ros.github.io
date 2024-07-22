==============
|package_name|
==============

Quickstart
----------

This quickstart shows how to run the camera ros node on the device.

.. code:: bash

   (ssh) ros2 launch qrb_ros_camera qrb_ros_camera_launch.py

qrb_ros_camera_launch.py is in /opt/qcom/qirp-sdk/usr/share/qrb_ros_camera/launch, you can change image parameters in this.
API
----

Overview
^^^^^^^^

This API shows the topic and parameter detail.

Available Components
^^^^^^^^^^^^^^^^^^^^

======================== ==================================================== 
Component                Topics Published                                     
======================== ==================================================== 
``CameraNode``              ``image``: publish the image data           
``CameraNode``              ``camera_info``: publish the camera info data                
======================== ==================================================== 

======================== ==================================================== 
Component                Parameters                                     
======================== ==================================================== 
``CameraNode``              ``camera_info_path``: the url of camera yaml file(yaml file is in /opt/qcom/qirp-sdk/usr/share/qrb_ros_camera/config)          
``CameraNode``              ``fps``: the frame rate of image   
``CameraNode``              ``width``: the width of image   
``CameraNode``              ``height``: the height of image  
``CameraNode``              ``cameraId``: the ID to identify which camera to use 
``CameraNode``              ``format``: default format is nv12, and currently only support nv12                  
======================== ==================================================== 

.. |package_name| replace:: ``qrb_ros_camera``