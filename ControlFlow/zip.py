#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     zip
   Description :
   Author :       Administrator
   date：          2019/4/17 10:37
-------------------------------------------------
   Change Activity:
                   10:37:
-------------------------------------------------
"""
__author__ = 'Administrator'
questions=['name','question','favorite color']
answers=['lancelot','the holy grail','blue']
for q,a in zip(questions,answers):
    print('what is your {0}? it is {1}.'.format(q,a))