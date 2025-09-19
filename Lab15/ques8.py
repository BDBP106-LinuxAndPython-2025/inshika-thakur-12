#!/usr/bin/python

#Write a program to tell which quadrant at a given point lies in the first, second, third or fourth quadrant

x=int(input("Enter x coordinate: "))
y=int(input("Enter y coordinate: "))

if x==0 and y==0:
    print("You are on origin")
elif x>0 and y>0:
    print("You are in the first quadrant")
elif x<0 and y>0:
    print("You are in the second quadrant")
elif x<0 and y<0:
    print("You are in the third quadrant")
elif x>0 and y<0:
    print("You are in the fourth quadrant")
elif x==0 and y!=0:
    print("You are on y axis")
else:
    print("You are on x axis")
