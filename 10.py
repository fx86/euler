'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

from primes import isprime


def sumofprimes(n):
    primes = []
    for i in xrange(n):
        if isprime(i):
            primes.append(i)

    return sum(primes)
