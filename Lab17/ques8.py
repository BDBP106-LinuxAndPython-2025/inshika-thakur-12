#!/usr/bin/python

"""Write a program to interchange the even and odd components of an input list. The list
can contain any type of variables. Output the result for the following example:
[23,32,33,44,’BDBH101’,’hello’,’python’, 15, 1e-10, True,’hit’]"""

L=[23,32,33,44,"BDBH101","hello","python", 15, 1e-10, True, "hit"]
print(f'Oringinal list: {L}')
New=[]
for i in range (0,len(L)-1,2):
    New.append(L[i+1])
    New.append(L[i])
print(f'New list: {New}')