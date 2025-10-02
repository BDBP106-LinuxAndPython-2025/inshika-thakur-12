#!/usr/bin/python

#One can create a set from several different objects – lists, tuples and dictionaries.
#Come up with an example for each object type, and create a set out of that object using the set() function.
#In the case of a dictionary, what does the set contain?.

L=[1,2,3,1,4,5,6,2,3,3,4,1]
T=(1,2,3,1,4,5,6,2,3,3,4,1)
D={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7}

S1=set(L)
S2=set(T)
S3=set(D)

print(S1)
#output:{1, 2, 3, 4, 5, 6}
print(S2)
#output:{1, 2, 3, 4, 5, 6}
print(S3)
#output: {'d', 'g', 'f', 'c', 'b', 'a', 'e'}
#in case of dictionary the set contains only the keys and not the values