#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     namedtuple
   Description :
   Author :       Administrator
   date：          2019/4/12 16:04
-------------------------------------------------
   Change Activity:
                   16:04:
-------------------------------------------------
"""
__author__ = 'Administrator'
from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x)
print(p.y)