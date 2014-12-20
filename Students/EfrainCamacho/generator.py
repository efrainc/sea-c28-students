#!/usr/bin/env python
"Generator Assignment"

"""from generator import generator_solution 

gen = generator_solution()
updated the testing file with the above lines to get this to 
run with the desired return values"""

class generator_solution(object):
    def __init__(self):
        return None

    def intsum(self):
        i = 0
        value = 0
        while True:
            yield value
            i += 1
            value = value + i

    def intsum2(self):
        i = 0
        value = 0
        while True:
            yield value
            i += 1
            value = value + i

    def doubler(self):
        value = 1 
        while True:
            yield value
            value = value * 2

    def fib(self):
        first = 0
        follower = 1
        while True:
            yield follower
            (first, follower) = (follower, first + follower)

    def prime(self):
        prime = 2
        list_of_primes = []
        while True:
            for x in list_of_primes:
                if prime % x == 0:
                    break 
            else:
                list_of_primes.append(prime)
                yield prime 
            prime += 1






           