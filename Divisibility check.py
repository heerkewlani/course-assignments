# -*- coding: utf-8 -*-
"""Untitled22.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JRwsA16U2gapXEn9rkOWMp8-apEUPLpD
"""

'''
write a python program to find those numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included).
'''

for i in range(1500,2700):
  if i%7==0 and i%5==0:
    print(i)