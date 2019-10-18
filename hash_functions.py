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
        raise TypeError('Hast table N must be type int')
    # test to ensure list is positive int
    if N <= 1:
        return None
    # create hash output
    sum = 0
    for i in range(len(key)):
        sum += ord(key[i])
    r = sum % N
    return r

def h_rolling(key, N):
    return None

