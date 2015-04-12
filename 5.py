'''
smallest positive number that is evenly divisible by all of the
numbers from 1 to 20

source : http://www.s-anand.net/euler.html

The elegance of this solution just stopped any other answer
from forming in my head.
'''


def gcd(a, b):
    return b and gcd(b, a % b) or a


def lcm(a, b):
    return a * b / gcd(a, b)

n = 1
for i in xrange(1, 21):
    n = lcm(n, i)

print n
