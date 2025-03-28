======================
``qrb_battery_client``
======================

API
---

.. list-table::
    :header-rows: 1

    * - Function Name
      - Comment

    * - bool InitConnection()
      - Create connection with battery service

    * - void CloseConnection()
      - Destroy connection with battery service

    * - bool GetBatteryStats(std::unique_ptr<std::string> & msg)
      - Get battery data.
        ``msg``: battery data 's string, each row of data is separated by a colon.
