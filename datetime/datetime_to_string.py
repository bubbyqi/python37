#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     datetime_to_string
   Description :
   Author :       Administrator
   date：          2019/4/12 15:00
-------------------------------------------------
   Change Activity:
                   15:00:
-------------------------------------------------
"""
__author__ = 'Administrator'
from datetime import datetime
now=datetime.now()
print(now.strftime('%a,%b %d %H:%M'))