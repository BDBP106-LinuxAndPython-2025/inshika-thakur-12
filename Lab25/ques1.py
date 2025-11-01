#!/usr/bin/python3

"""(1) SQLite exercise:"""

"""(i) Write a program to create an SQLite database in the file IBABEmployee.db that
contains a table called Employee with fields ID, name, research area, designation
and gender."""

import sqlite3

conn=sqlite3.connect('IBABemployee.db')
curs=conn.cursor()
curs.execute('''CREATE TABLE IF NOT EXISTS Employee 
(emp_ID INTEGER,
emp_name TEXT,
emp_researchArea TEXT,
emp_designation TEXT,
emp_gender TEXT)''')



print(f'--------------------------------------------------------------------')

"""(ii)Write a program that allows the user to add multiple records into the above
database file. After every record, the user should be asked whether he/she wants
to add another record. Do this for all the faculty in IBAB."""

# database=[]
# while True:
#     emp_ID=int(input('Enter employee ID: '))
#     emp_name=input('Enter employee name: ')
#     emp_researchArea=input('Enter employee research area: ')
#     emp_designation=input('Enter employee designation: ')
#     emp_gender=input('Enter employee gender: ')
#     question=input('Do you want to add another record? (y/n): ')
#     database.append((emp_ID, emp_name, emp_researchArea, emp_designation, emp_gender))
#     if question=='n':
#         break
# curs.executemany("""INSERT INTO Employee VALUES(?,?,?,?,?)""",database)
# conn.commit()

print(f'-----------------------------------------------------------------------------')

"""(iii) Write a program that allows the user to edit an entry present in the above 
database. The program should ask for the ID of the employee and should take in the 
new details of the employee."""

# conn.row_factory=sqlite3.Row
#
#
# emp_id_to_edit=int(input('Enter the Employee ID thay you want to edit: '))
# curs.execute('SELECT * FROM Employee WHERE emp_ID=?', (emp_id_to_edit,))
# record=curs.fetchone()
#
# if record:
#     print(f"Current details of employee {record}:")
#     print("Enter new details of the employee: ")
#     newName=input(f'Employee name [{record[1]}]: ') or record[1]
#     newResearchArea=input(f'Employee research area [{record[2]}]: ') or record[2]
#     newDesignation=input(f'Employee designation [{record[3]}]: ') or record[3]
#     newGender=input(f'Employee gender [{record[4]}]: ') or record[4]
#
#     curs.execute("""UPDATE Employee
#                     SET emp_name=?, emp_researchArea=?, emp_designation=?, emp_gender=?
#                     WHERE emp_ID=?""",
#                     (newName, newResearchArea, newDesignation, newGender, emp_id_to_edit))
#     conn.commit()
#     print("Employee record updated successfully.")
# else:
#     print(f"No employee found with ID {emp_id_to_edit}.")

print(f'-----------------------------------------------------------------------')

"""(iv) Write a program that allows the user to delete 1 or more records from the above
database. The input is a single line containing the ID of the employees to be
deleted, separated by spaces."""

# emp_id_to_delete=input('Enter employee ID to delete: ')
# emp_id_to_dlt_list= emp_id_to_delete.split()
#
# delete_count=0
# for emp_id in emp_id_to_dlt_list:
#     curs.execute('DELETE FROM Employee WHERE emp_id=?',(emp_id,))
#     delete_count+=curs.rowcount
#
# print("Final recordes in database: ")
# curs.execute('SELECT * FROM Employee')
# rows=curs.fetchall()
# print(rows)

"""(v) Write a program that displays all the records present in the above database in a
formatted manner."""

curs.execute('SELECT * FROM Employee')
row=curs.fetchall()
if row:
    print(f'{'ID':<4}{'NAME':<20}{'ResearchArea':<20}{'Designation':<20}{'Gender':<5}')
    for i in row:
        emp_ID , emp_name, emp_researchArea, emp_designation, emp_gender=i
        print(f'{emp_ID:<4}{emp_name:<20}{emp_researchArea:<20}{emp_designation:<20}{emp_gender:<5}')
else:
    print('No records found.')