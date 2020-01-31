import math

num = 600851475143
# technically needs to be num/2 or new methods to get absolute answer
max_prime = math.sqrt(num)
primes = [2]

for i in range(3, int(max_prime)+1, 2):
	is_prime = True
	for j in primes:
		if (j > math.sqrt(i)):
			break
		if (i % j == 0):
			is_prime = False
			break
	if (is_prime):
		primes.append(i)

for i in range(len(primes)-1, -1, -1):
	if (num % primes[i] == 0):
		print(primes[i])
		break

#6857