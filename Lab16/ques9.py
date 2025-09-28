#!/usr/bin/python

#Write a script to check if two strings are anagrams of each other . Eg. listen and
#silent are anagrams, gram and arm are not anagrams.
W1=input("Enter the first word: ")
W2=input("Enter the second word: ")
if (sorted(W1)==sorted(W2)):
    print("is an anagram")
else:
    print("is not an anagram")