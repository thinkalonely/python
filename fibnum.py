# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def fibnum(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for n in fibnum(10):
    print(n)
