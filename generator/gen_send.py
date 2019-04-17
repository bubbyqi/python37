#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     gen_send
   Description :
   Author :       Administrator
   date：          2019/4/15 15:10
-------------------------------------------------
   Change Activity:
                   15:10:
-------------------------------------------------
"""
__author__ = 'Administrator'
def gen():
    while True:
        s = yield
        print(s)

g=gen()
g.send("bubbyqi")
