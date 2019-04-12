#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     timezone
   Description :
   Author :       Administrator
   date：          2019/4/12 15:08
-------------------------------------------------
   Change Activity:
                   15:08:
-------------------------------------------------
"""
__author__ = 'Administrator'
from datetime import datetime,timezone,timedelta
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)