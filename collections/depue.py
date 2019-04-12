#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     depue
   Description :
   Author :       Administrator
   date：          2019/4/12 16:08
-------------------------------------------------
   Change Activity:
                   16:08:
-------------------------------------------------
"""
__author__ = 'Administrator'
from collections import  deque
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)