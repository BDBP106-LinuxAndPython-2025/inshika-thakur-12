#!/usr/bin/python3

"""(2) Lists and do loops
(i) Using a simple do loop structure or list comprehension, find the sum of elements in the
above list a.
(ii) Define another list b (using list comprehension again!) containing prime numbers from 1 to 50.
(iii) Using a do loop structure, collect all the common numbers in a and b into a new list c."""

a = [i for i in range(1, 51)]

#i)
#using the do loop:
Sum=0
for number in a:
    Sum=Sum+number
print(Sum)

#using the list comprehension method:
Sum=sum([i for i in range(1,51)])
print(Sum)

#ii)list b with prime numbers 1-50
b=[i for i in range(2,51) if all(i%y!=0 for y in range(2, int(i**0.5)+1))]
print(b)

#iii)all common numbers in  a and b
cmn_num=[ i for i in a if i in b ]
print(cmn_num)

