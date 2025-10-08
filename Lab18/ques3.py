#!/usr/bin/python3

"""List comprehension with strings Use list comprehension technique you learnt
in class to do the following."""

a = [i for i in range(1, 51)]
#i) Using the join method:
#a) Create a string by joining the numbers in the above list a using the comma.
str_join=",".join(str(i) for i in a)
print(f' The string by joining numbers in list using comma is:{str_join}')

#b)Create a string by joining the numbers in the above list a using the period.
join_period=".".join(str(i) for i in a)
print(f' The string by joining numbers using period is {join_period}')

#c)Create a string by joining the numbers in the above list a using the ‘—’.
join_dash="-".join(str(i) for i in a)
print(f' The string by joining numbers using dash is {join_dash}')

#d)Create a new string by first creating a list of squares of the elements in a,
#then listing them alongside the elements of a line by line.In other words,
#we want a data set that looks like:
#1 1
#2 4
#2 9
print('\n'.join([f'{i} {i**2}' for i in a]))

#(ii) Make a list of 10 people you know, and do the following
List= [
    "Rahul Thakur",
    "Pujasvi Jella",
    "Rajeshwari",
    "Suhani Bansal",
    "Aheli Biswas",
    "Himiksha Singh",
    "Tenzin Saldon",
    "Tenzin Kunsel",
    "Tashi Dolma",
    "Renjima Sherin"
]

#a)Convert each element in the list to upper case using list comprehension.
upper_case = [i.upper() for i in List]
print(upper_case)

#b)Swap the first name and surname of each element in the list
swapped_list= [' '.join(i.split()[::-1]) for i in List]
print(swapped_list)

#c)Join the first name and surname in each element as ’First.Last’. Note that
#the first letter of the first name and first letter of the surname should be
#upper case.

new_list = [
    f"{i.split()[0].capitalize()}.{i.split()[-1].capitalize()}" if len(i.split()) >= 2 else i.capitalize()
    for i in List
]

#iii) Find the longest word in this sentence using list comprehension: ”She sells sea
#shells that she collects from the sea floor”.

S="She sells sea shells that she collects from the sea floor"
Words=S.split()

longest_word_len=max(len(i) for i in Words)
longest_word=[i for i in Words if len(i)==longest_word_len]
print(f'The longest word in the given sentence is {longest_word}')

#iv)Create a list of the words that are repeated in the above sentence.
Words = S.lower().split()
Repeated = list({i for i in Words if Words.count(i) > 1})
print(Repeated)
