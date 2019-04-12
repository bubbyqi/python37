#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     defaultdict
   Description :
   Author :       Administrator
   date：          2019/4/12 16:11
-------------------------------------------------
   Change Activity:
                   16:11:
-------------------------------------------------
"""
__author__ = 'Administrator'
from collections import defaultdict
dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])