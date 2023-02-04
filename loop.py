# Print your name 3 times
s="Pankaj Yadav"
x=''
for i in s:
	x=x+i
print(3*x)
# Print numbers from 10 to 15
for i in range(10,16):
	print(i)
# Find sum of numbers from 1 to 10
# Check your answer

x=0
for i in range(1,11):
	x=x+i
print(x)
# Print the first 11 cube numbers

for i in range(1,12):
	x=i**3
	print(x)
# enter the first odd number

from math import *
def find_composite(a,b):
    copy1=[]
    #copy2=[]
    for i in range(a,b+1):
        for j in range(2,int(sqrt(i))+1):
            if i%j==0:
                copy1.append(i)
                #[copy2.append(x) for x in copy1 if x not in copy2]
    print(list(set(copy1)))
from math import *   
find_composite(7,49)
n=int(input("Enter the number:"))
for i in range(2,int(sqrt(n))+1):
	if n%i==0:
		print("it is prime number")
	else:
		print('not')







































