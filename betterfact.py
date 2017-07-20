def factor():

	l = [] #List of factors, starts out empty
	
	n = int(input("Please enter number you need factored: ")) #The number whose factorization we want
	
	i = 2 #The first number we will try dividing by(will not always be a prime)
	
	while n > 1: #The number one doesnt have any factors other then it self
	
		if n%i == 0 : #We check to see if the number is divisible by our current prime(*)
		
			while n%i == 0 : #Our number may be divisible by a certain factor more then once so we will cover all of them this way
			
				n /= i #We will reduce the number by that factor
				
				l.append(i) #We will add that factor to our factor list
				
		else : #If our number isn't divisible by the current factor we will try the next(**) prime(*) and so on
			if i == 2 :
				i += 1
			else :
				i += 2
			
	print (l) #We print our factors
	exit = input("Press enter to exit")
	if exit == "":
		pass
	else :
		factor()
	
factor() #We call out factor function
#(*)We are garunteed that our function won't skip any primes as it is incrementing from smallest to largest numbers and diving 
#our number or reduced number, by its smallest possible factor(excluding 1), which will always be a prime.
