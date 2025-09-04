import cmath
import math
a=3
b=5.5
c=2.5

#without using the cmath:
x=(-b+(b*b-4*a*c)**(1/2))/(2*a)
print(x)
x1=(-b-(b*b-4*a*c)**(1/2))/(2*a)
print(x1)

#output:
#-0.8333333333333334
#-1.0


#using math
x1=(-b+ math.sqrt(b*b-4*a*c))/(2*a)
print(x1)
x2=(-b- math.sqrt(b*b-4*a*c))/(2*a)
print(x2)

#output using math.sqrt
#-0.8333333333333334
#-1.0
#we got output in math.sqrt because the number was not negative for square root)


#cmath is complex math here and normal math cannot take a negative number for squareroot so we were grtting math domain error that is why we used cmath
x1=(-b+ cmath.sqrt(b*b-4*a*c))/(2*a)
print(x1)
x2=(-b- cmath.sqrt(b*b-4*a*c))/(2*a)
print(x2)

#output using cmath.sqrt
#(-0.8333333333333334+0j)
#(-1+0j)

