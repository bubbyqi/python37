#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fork
   Description :
   Author :       Administrator
   date：          2019/4/12 14:16
-------------------------------------------------
   Change Activity:
                   14:16:
-------------------------------------------------
"""
__author__ = 'Administrator'
import os
print('Process (%s) start...' % os.getpid())
pid=os.fork()
if pid==0:
    print('i am child process (%s) and my parent is %s.' % (os.getpid(),os.getpid()))

else:
    print ('i (%s) just created a child process (%s).'% (os.getpid(),pid))
