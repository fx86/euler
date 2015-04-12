'''
Largest prime factor
'''


def isprime(n):
    ''' checks if a number is prime or not '''
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def largestprimefactor(x):
    '''finds the largest prime factor'''
    factors = []
    for i in xrange(2, int(x ** .5) + 1):
        if i * i < x and isprime(i) and (x % i == 0):
            factors.append(i)
    return factors

largestprimefactor(600851475143)
