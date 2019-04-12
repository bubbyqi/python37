#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     timestamp
   Description :timestamp与时区毫无关系，全球一样，是个相对值，以0为基准，0表示1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time
   Author :       Administrator
   date：          2019/4/12 14:37
-------------------------------------------------
   Change Activity:
                   14:37:
-------------------------------------------------
"""
__author__ = 'Administrator'
from datetime import datetime
dt= datetime(2019,4,12,14,40)
t=dt.timestamp()
epoch=datetime.fromtimestamp(0)
epoch_utc=datetime.utcfromtimestamp(0)
print(epoch)
print(epoch_utc)
print(t)