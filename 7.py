'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
'''


def isprime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** .5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def findprime(x=10001):
    primelist = []
    i = 1
    while len(primelist) <= x - 1:
        if isprime(i):
            primelist.append(i)
        i += 1
    return primelist

if __name__ == '__main__':
    if findprime(6) == [2, 3, 5, 7, 11, 13]:
        primelist = findprime()
        print primelist[-1]
