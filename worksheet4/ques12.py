"""Q12.)Write a python script that lists out each line of a file prefixed with its
line number."""

f=open('test.txt', 'r')
l=f.readlines()
f.close()

for i in range(len(l)):
    print(f"{i+1}: {l[i].strip()}")
