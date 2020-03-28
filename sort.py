# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:59:40 2020

@author: MEET MEHTA
"""
#In this program we have used the sort() function
# 

numbers=[1,4,2,3]
num1=[1.1,1.01,1.001]
numbers.sort()
num1.sort()
numbers.sort(reverse=True)

def sort1(val):
    return val[0]
list1=[(1,2),(2,2),(1,3)]
list1.sort(key=sort1)
print(list1)
list1.sort(key=sort1,reverse=True)

    