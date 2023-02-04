#Write a function is_prime(n) that receives a number n as parameter and returns True 
#if n is prime, else returns False.
def is_prime(n):
	'''Return:to check number given by user is prime or not
	
	a number is prime when we divide 2 to squareroot of given number(n) its remainder is not equal to zero.
	otherwise it is not a prime number.

	precondition:number should be int or float



	'''

	
	t=int(n**(0.5))
	isPr = True
	for i in range(2,t+1):

		if n%i==0:
			isPr = False
	return isPr		
print(is_prime(999999937))