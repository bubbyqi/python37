#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     to_timestamp
   Description :
   Author :       Administrator
   date：          2019/4/12 15:15
-------------------------------------------------
   Change Activity:
                   15:15:
-------------------------------------------------
"""
__author__ = 'Administrator'
from datetime import datetime,timedelta,timezone
def to_timestamp(dt_str,tz_str):
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    tz_hour=int(tz_str[3:].split(':')[0])
    tz_utc=timezone(timedelta(hours=tz_hour))
    return dt.replace(tzinfo=tz_utc).timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

