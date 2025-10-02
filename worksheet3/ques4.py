

"""One can use sets or lists or tuples as values in a dictionary. For example, let’s define the
following dictionary studentmarks={"Rahul":{49,58, 35,64}, "Sandeep":{80,92,94,83},"Sita":{44,65,76,54}}
Write a script to check and print the name of the student if the student has scored above
60 in all subjects."""

studentmarks = {"Rahul": {49, 58, 35, 64}, "Sandeep": {80, 92, 94, 83}, "Sita": {44, 65, 76, 54}}
for student,marks in studentmarks.items():
    above_60 = True
    for mark in marks:
        if mark <= 60:
            above_60 = False
            break
    if above_60 == True:
        print(f'Student who has scored above 60 in all subjects:' ,student)

#in line 9: we are iterating through the dictionary and it will return a tuple
#each tuple will contain a key and it's value. The marks of the student is present as a set so
#we need to access each element of the set

#in line 10: we assume that all marks is above 60
#line 11: it accesses the marks in the set one be one.

#line 12, in this if the marks is less than or equal to 60 we will set the above_60 to false
#and if it is above_60 then it will print the student name.