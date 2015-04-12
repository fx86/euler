'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def triplets(n):
    for i in xrange(n):
        for j in xrange(i, n):
            k = 1000 - i - j
            if k > 0:
                if k ** 2 == i ** 2 + j ** 2:
                    print i * j * k
triplets(1000)
