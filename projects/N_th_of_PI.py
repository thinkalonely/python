# coding: utf-8
"""
Enter a number and find have the program generate PI up to that many decimal places.
Bailey–Borwein–Plouffe
Pi = SUM k=0 to infinity 16^-k [ 4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6) ]
ref: https://www.math.hmc.edu/funfacts/ffiles/20010.5.shtml
"""
import math
from decimal import *


getcontext().prec = 50
MAX = 10000
pi = Decimal(0)


for k in range(MAX):
    pi += Decimal(math.pow(16, -k)) * (Decimal(4/(8*k+1)) - Decimal(2/(8*k+4)) - Decimal(1/(8*k+5)) - Decimal(1/(8*k+6)))

print('PI >>>>>>>>>>', pi)
