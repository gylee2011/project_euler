#! /usr/bin/env python

primes = [2]

def is_prime(num):
	for item in primes:
		if num % item == 0:
			return False
	primes.append(num)
	return True

i = 3
while(len(primes) != 10001):
	is_prime(i)
	i = i + 2

print primes[len(primes)-1]

