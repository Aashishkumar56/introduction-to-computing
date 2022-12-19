#q1
print("average calculater")
a=int(input("number one : "))
b=int(input("number two : "))
c=int(input("number three : "))
d=(a+b+c)/3
print(d)

#q2
a=float(input("enter your income : "))
b=a-10000
c=int(input("Dependents : "))
d=c*3000
e=b-d
f=(0.2*e)
print(f)

#q3
from math import *
a=float(input("first : "))
b=a/60
c=(a % 60)
d="mins"
e=floor(b)
f="secs"
print(e,d,"and",c,f)

#q4
a=int(input("num1 : "))
b=float(input("num2 : "))
c=input("num3 : ")
d=a+b+int(c)
print(d)

#q5
import math
a=int(input("enter the value from 0-345 : "))
b=print(math.sin(math.radians(a)),math.cos(math.radians(a)))
