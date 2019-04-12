#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     timedelta
   Description :
   Author :       Administrator
   date：          2019/4/12 15:02
-------------------------------------------------
   Change Activity:
                   15:02:
-------------------------------------------------
"""
__author__ = 'Administrator'
from datetime import datetime,timedelta
now=datetime.now()
print(now)
t=now+timedelta(hours=10)
print(t)
s=now-timedelta(days=1)
print(s)
j=now+timedelta(days=1,hours=1,minutes=30)
print (j)