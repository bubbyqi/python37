#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sort
   Description :
   Author :       Administrator
   date：          2019/4/17 10:45
-------------------------------------------------
   Change Activity:
                   10:45:
-------------------------------------------------
"""
__author__ = 'Administrator'
basket=['apple','orange','apple','pear','orange','banana']
for i in sorted(set(basket)):
    print(i)