#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     generator
   Description :
   Author :       Administrator
   date：          2019/4/15 15:05
-------------------------------------------------
   Change Activity:
                   15:05:
-------------------------------------------------
"""
__author__ = 'Administrator'
def g():
    print("1 is")
    yield 1
    print("2 is")
    yield 2
    print("3 is")
    yield 3
z=g()
print(z)
print(next(z))
print(next(z))
print(next(z))
print(next(z))