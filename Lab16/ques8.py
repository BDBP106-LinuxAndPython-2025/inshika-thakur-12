#!/usr/bin/python3

#Write a script to count the number of occurrences of a word, W, in a sentence, S.

S=input("Enter the sentence: ")
W=input("Enter the word: ")
V=S.split()
count=0
for i in V:
    if i==W:
        count=count+1
print(count)