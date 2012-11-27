#! /usr/bin/env python
def is_palindrome(num):
	num = str(num)
	first_half = num[:len(num)/2]
	last_half = num[-1*(len(num)/2):]
	last_half = last_half[::-1]
	return first_half == last_half


def find_palindrome():
	ret = []
	for i in range(999, 99, -1):
		for j in range(999, 99, -1):
			if is_palindrome(i*j):
				ret.append(i*j)
	return ret

p = find_palindrome()
p.sort()
p.reverse()

print p[0]
