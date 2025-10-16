#!/usr/bin/python3

"""(b) Next, in a new program, read in the matrix of strings in the above file as a 2D array
of list of lists. The number of rows and columns are not known in advance. Make
sure your code can figure out how many rows and columns are there in this input.
Name this list as grid and print this 2D list. Name this program as ”Q3 b.py”. In
this same program, print a list that contains lists of columns of the above matrix.
For example, the first column will be grouped into a list [A,E,I] and so on. Next,
print a list that prints the diagonal elements read in one direction. For example,
some of the elements in this list will be [‘A’],[‘B’,‘E’],[’C’,‘F’,‘I’] and so on."""

with open('stringmatrix.dat', 'r') as file:
    grid=[line.strip().split() for line in file]

print("Grid:")
for row in grid:
    print(row)

numRow = len(grid)
numCols = len(grid[0]) if numRow > 0 else 0

print(f'\nRows:{numRow}, Cols:{numCols}')

columns=[]
for i in range(numCols):
    col=[]
    for j in range(numRow):
        col.append(grid[j][i])
    columns.append(col)

print('\nColumns:')
for column in columns:
    print(column)

D=[]
for a in range(numRow+numCols-1):
    diagonal=[]
    for b in range(numRow):
        c=a-b
        if 0<=c<numCols:
            diagonal.append(grid[b][c])
        D.append(diagonal)

print('\nDiagonals:')
for diagonal in D:
    print(diagonal)