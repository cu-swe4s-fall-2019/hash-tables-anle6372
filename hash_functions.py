"""Library of hash functions
Parameters
----------
key : string that is to be converted into a integer within the range(N)
N : integer that represents the size of the hash table


Returns
-------
r : the hash position of string key in table of length N
"""


def h_ascii(key, N):
    # test to ensure input exists
    if key is None:
        return None
    if N is None:
        return None
    # test to ensure input is correct type
    if not type(key) == str:
        raise TypeError('key must be type string')
    if not type(N) == int:
        raise TypeError('Hash table N must be type int')
    # test to ensure list is positive int
    if N < 1:
        return None
    # create hash output
    sum_ = 0
    for i in range(len(key)):
        sum_ += ord(key[i])
    r = sum_ % N
    return r

def h_rolling(key, N):
    # test to ensure input exists
    if key is None:
        return None
    if N is None:
        return None
    # test to ensure input is correct type
    if not type(key) == str:
        raise TypeError('key must be type string')
    if not type(N) == int:
        raise TypeError('Hast table N must be type int')
    # test to ensure list is positive int
    if N < 1:
        return None
    # defining necessary parameters p, a prime number roughly equal 
    # to the number of characters in the input alphabet 
    # m should be a large number, by convention m=2^64 is chosen
    p = 53
    m = 2 ** 64
    sum_ = 0
    for i in range(len(key)):
        sum_ += ord(key[i]) * p ** i
    sum_ = sum_ % m
    return sum_ % N

def h_ascii_sq(key, N):
    # test to ensure input exists
    if key is None:
        return None
    if N is None:
        return None
    # test to ensure input is correct type
    if not type(key) == str:
        raise TypeError('key must be type string')
    if not type(N) == int:
        raise TypeError('Hash table N must be type int')
    # test to ensure list is positive int
    if N < 1:
        return None
    # create hash output
    sum_sq = 0
    for i in range(len(key)):
        sum_sq += ord(key[i]) ** 2
    r = sum_sq % N
    return r