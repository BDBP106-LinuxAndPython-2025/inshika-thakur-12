#!/usr/bin/python3

#Write a program to subtract two matrices, m1 and m2, using a list of lists.

m1=[
    [4,8],
    [1,5],
]
m2=[
    [4,9],
    [2,7],
]

output=[
    [0,0],
    [0,0],
]

for i in range(0,len(m1)):
    for j in range(0,len(m2)):
        output[i][j]+=m1[i][j]-m2[i][j]
print(output)