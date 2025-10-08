#!/usr/bin/python3

"""(1) (i) Create a list spanning 1 to 50 using list comprehension method. Call this list a.
(ii) Slicing with positive step:
(a) a[1:5]
(b) a[3:20:2]
(c) a[::2]
(d) a[::]
(e) a[10::2]
(f) a[1:1:1]
(g) a[:0:]
(h) a[-7::1]. Is the output a non-empty list? Why did this work?
(i) a[-6:]
(j) a[-10:-4]
(iii) Slicing with negative step:
(a) a[::-1]
(b) a[::-3]
(c) a[:1:-2]
(d) a[-1:-1:-1]
(e) a[:-5:-1]
(f) a[:0:-1]
(g) a[:-1:-1]
(h) a[0:-5:-1]
(i) a[-1:5:-1]
(j) a[2:2:-1]
(k) a[2:1:-1]
(l) a[0:-5]
(iv) Modification of lists using list slicing:
(a) Create a list of even numbers from a using list slicing technique.
(b) Create a new list from a by choosing the first 10 numbers, then the even
numbers from 35-50."""

#1) i)
a = [i for i in range(1, 51)]
print(a)

#ii) slicing with positive step:
#a)
print(a[::2])
#b)
print(a[3:20:2])
#c)
print(a[::2])
#d)
print(a[::])
#e)
print(a[10::2])
#f)
print(a[1:1:1])
#g)
print(a[:0:])
#h) Is the output a non-empty list? Why did this work?
print(a[-7::1])
#i)
print(a[-6:])
#f)
print(a[-10:-4])

#iii)slicing with negative step:
#a)
print(a[::-1])
#b)
print(a[::-3])
#c)
print(a[:1:-2])
#d)
print(a[-1:-1:-1])
#e)
print(a[:-5:-1])
#f)
print(a[:0:-1])
#g)
print(a[:-1:-1])
#h)
print(a[0:-5:-1])
#i)
print(a[-1:5:-1])
#j)
print(a[2:2:-1])
#k)
print(a[2:1:-1])
#l)
print(a[0:-5])

#(iv) Modification of lists using list slicing:
#(a) Create a list of even numbers from a using list slicing technique.
even=a[1::2]
print(even)

#(b) Create a new list from a by choosing the first 10 numbers, then the even numbers from 35-50
even_num=a[:10]+[i for i in a if 35 <= i <= 50 and i%2==0]
print(even_num)
