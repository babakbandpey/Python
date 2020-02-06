#!/usr/bin/python3

import ntplib
from time import ctime
c = ntplib.NTPClient()
response = c.request('pool.ntp.org')
print(ctime(response.tx_time))
