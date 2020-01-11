# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 00:27:52 2020

@author: MEET MEHTA
"""
# In this program we will see if and else loop and compare between 3 numbers
#Before starting the program, 
#tip:python doesnt have brackets but it does have indendation so watchout for the spaces else you will get an error
#If and else loop syntax is as follow
#if condition:
 #   Code and logic
#else:
 #   Code and logic
  #  if you want a nested loop you can use elif like else if in python
#if condition:
 #   Code and logic
#elif condition:
 #   Code and logic
#else:
    #Code and logic

a=int(input("enter 1st Integer:"))
print("a=",a)
b=int(input("enter 2nd Integer:"))
print("b=",b)
c=int(input("enter 3rd Integer:"))
print("c=",c)
if a>b and a>c:
    print("Largest among the three is a")
elif b>a and b>c:
    print("Largest among the three is b")
elif a==c: print("a and c are equal")# short hand if
else:
    print("Largest among the three is c")
print("30") if a>b else print("45")# short hand if else
    
#enter 1st Integer:2
#a= 2
#enter 2nd Integer:3
#b= 3
#enter 3rd Integer:4
#c= 4
#Largest among the three is c
#30