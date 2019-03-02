#!/usr/bin/env python
# -*- coding: utf-8 -*-
def fact(n, *b) :
    s=1
    for i in range(1,n+1):
        s *=i
    for item in b:
        s *=item
    return s,n
a,b=fact(2,2,2)
print(a,b)