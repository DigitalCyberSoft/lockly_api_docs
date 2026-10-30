CRC-8
=====

Lockly uses a non-standard CRC-8 (``CrcUtils.java``) over the whole frame
**including** the type byte but **excluding** the CRC byte itself. The lookup
table has only 16 entries — it processes 4 bits at a time. (🔎 from LocklyHA.)

.. sourcecode:: python

   CRC8_LUT = [0, 49, 98, 83, 196, 245, 166, 151,
               185, 136, 219, 234, 125, 76, 31, 46]

   def crc8_lockly(data: bytes) -> int:
       crc = 0
       for byte in data:
           s4  = ((crc << 4) & 0xFF) ^ CRC8_LUT[(crc >> 4) ^ (byte >> 4)]
           crc = ((s4  << 4) & 0xFF) ^ CRC8_LUT[(s4  >> 4) ^ (byte & 0x0F)]
       return crc & 0xFF
