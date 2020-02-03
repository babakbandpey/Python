#!/usr/bin/python3
import sys

a=6
b=2000
c=100
d=400

maks = -sys.maxsize - 1

if(a > maks):
	maks = a
if(b > maks):
	maks = b
if(c > maks):
	maks = c
if(d > maks):
	maks = d

print("Largest value is :" + str(maks))

if((a > b or a == b) and a > c and a > d):
	print("Largest value is :" + str(a))
if(b > a and b > c and b > d):
	print("Largest value is :" + str(b))
if(c > a and c > b and c > d):
	print("Largest value is :" + str(c))
if(d > a and d > b and d > c):
	print("Largest value is :" + str(d))
