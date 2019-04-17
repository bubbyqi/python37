#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     iterator
   Description :
   Author :       Administrator
   date：          2019/4/15 14:34
-------------------------------------------------
   Change Activity:
                   14:34:
-------------------------------------------------
"""
__author__ = 'Administrator'
from collections import   Iterable,Iterator
a=[1,2,3]
b=iter(a)
print(isinstance(a,Iterator))
print(isinstance(a,Iterable))
print(isinstance(b,Iterator))
print(isinstance(b,Iterable))
c=list(b)
print(c)
d=list(b)
print(b)