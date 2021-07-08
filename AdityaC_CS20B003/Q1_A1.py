# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hDUaHJ2z48fVmjUaD0jxasD_aecPykHR
"""

import numpy as np
import math

n = 100
ycap = np.random.rand(n)
y = np.random.randint(0,2,n)

O = 0;
for i in range(0,n,1):
    O += y[i]*math.log2(ycap[i]) + (1-y[i])*math.log2(1-ycap[i])
    
O /= -n
print(O)