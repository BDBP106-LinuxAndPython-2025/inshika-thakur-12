#!/use/bin/python

#Write a program to check if an input string is palindrome

A=input("Enter a word: ")
B=(A[::-1])
print(f'{B}')
if A==B:
  print("The word that you entered is a plaindrome")
else:
  print("The word that you entered is not a palindrome")
