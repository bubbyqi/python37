#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     str_to_datatime
   Description :
   Author :       Administrator
   date：          2019/4/12 14:56
-------------------------------------------------
   Change Activity:
                   14:56:
-------------------------------------------------
"""
__author__ = 'Administrator'
from datetime import datetime
cday=datetime.strptime('2019-4-12 14:57:20','%Y-%m-%d %H:%M:%S')
print(cday)