'''
largest palindromic product of two three-digit numbers:
solution:
calculate a single array of possible numbers of 3 digits,
multiply each by others. Make a set and check for palindromes
'''


def answer(digit=2):
    '''
        calculates the product of 'numbers', each of 'digit's
    '''
    number_set = range(10, 10 ** digit)
    prods = []
    [prods.extend(map(lambda x: x * i, number_set))
        for i in number_set]
    return max([i for i in prods if str(i) == str(i)[::-1]])


if __name__ == '__main__':
    if answer() == 9009:
        print answer(digit=3)
