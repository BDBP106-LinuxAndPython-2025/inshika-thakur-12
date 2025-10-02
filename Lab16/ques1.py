# #!/usr/bin/python3
#
# #Write a script to convert the binary number B into decimal.

#METHOD 1 USING INTRINSIC FUNCTION
#B=str(input("Enter a binary number: "))
#D=int(B,2)
#print (f' The decimal number is: {D}')

# #METHOD 2 USING LOOPS
B=str(input("Enter the binary number: "))
n=len(B)
# #Will specify the length of the string
binary=0
# #we initialised the binary as zero
for n in range(0,n):
    a=int(B[-1-n])
# #here we are converting the string into integer as we cannot do the mathematical
# #expression on string. and the B[-1-n] will take up the element from last f the string for converting it to int
    b=a*(2**n)
# #here we are multiplying that integer, with 2 raise to the power n. It is 0 in the first loop and keeps on increasing
    binary=binary+b
print(binary)