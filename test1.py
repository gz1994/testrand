#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time
DARTS = 1000*1000
hits = 0.0
start = time.perf_counter()
for i in range(1,DARTS+1):
    x,y = random.random(),random.random()
    dist = pow(x ** 2 + y **2,0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4*(hits/DARTS)
print("圆周率为：{}".format(pi))
print("运行时间：{:.5f}s".format(time.perf_counter()-start))