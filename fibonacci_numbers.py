# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KXy6Z7hlhy8vPIf9UqeMKtl89uc5ZO5K
"""

number=int(input("Enter the number of Fibonacci numbers to generate"))
fibonacci_numbers=[0,1]
for x in range(2,number):
  next=fibonacci_numbers[-1]+fibonacci_numbers[-2]
  fibonacci_numbers.append(next)
print(fibonacci_numbers)