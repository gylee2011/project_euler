#! /usr/bin/env python

primes = [2]
s = 2

def is_prime(num):
	for number in primes:
		if num%number == 0:
			return False
	primes.append(num)
	return True

for i in range(3, 2000000, 2):
	if is_prime(i):
		s = s + i
print s

print len(primes)
