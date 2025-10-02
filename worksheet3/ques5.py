

"""Write functions to add and subtract two matrices of m× n. Below these two functions,
create two example matrices that have the same dimensions (rows and columns) and
therefore correctly does the addition and subtraction Also come up with an example
where the addition and subtraction are not defined, and hence the runtime errors show
up."""

A = [
    [632, 4423, 44],
    [53, 23, 442],
    [734, 8244, 924]
]

B = [
    [976, 854, 567],
    [656, 565, 456],
    [3754, 672, 761]
]

#so we have matrix A and B that we are supposed to add and subtract
#But first we know that the number of rows and column should be same in both the matrices.
#We will start with comparing A and B.

if len(A) == len(B) and len(A[0]) == len(B[0]):
#Here len(A)==len(B) will compare the number of rows, as each row is present as a list inside the given matrix which is a list
#And the len(A[0]) is accessing the first element of the list that is the first row. len(A[0])==len(B[0]) will compare that.
    result_add = []
#Then we will create an empty list that will have the result of the addition
    for i in range(len(A)):
        row = []
#The empty list will store the value of current row of the addition result
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result_add.append(row)

    print("Matrix A + Matrix B:")
    for row in result_add:
        print(row)

    result_sub = []
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        result_sub.append(row)

    print("Matrix A - Matrix B:")
    for row in result_sub:
        print(row)

else:
    print("Matrices must have the same dimensions!")

