"""Library of classes that create hash tables with variable hash functions and resolution strategies
Parameters
----------
hash_function : the hash constructor function to be used
N : integer that represents the size of the hash table

Functions
----------
add(self, key, value):
    parameters:
        key: the key to be added
        value: the corresponding value to be added
    returns:
        Boolean: True indicates successful addition, false indicates unsuccessful addition

find(self, key):
    parameters:
        key: the key corresponding to the value at the hashed position
    returns: value corresponding to the given key

Returns
-------
Hash Table: A class object that is the data structure utilizing the hash function and desired size
"""

import hash_functions

class LinearProbe:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N
        self.T = [None for i in range(N)]
        if not callable(self.hash_function) is True:
            raise TypeError('hash function must be callable')
        if not type(self.N) is int:
            raise TypeError('table size must be an integer')

    def add(self, key, value):
        if key is None:
            return None
        test_slot = self.hash_function(key, self.N)
        for i in range(self.N):
            if self.T[test_slot] is None:
                self.T[test_slot] = (key, value)
                return True
            if test_slot == self.N - 1:
                test_slot = 0
                continue
            test_slot += 1
        return False

    def search(self, key):
        if key is None:
            return None
        test_slot = self.hash_function(key, self.N)
        for i in range(self.N):
            if self.T[test_slot] is None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
            if test_slot == self.N - 1:
                test_slot = 0
                continue
            test_slot += 1
        return None

class ChainedHash:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N
        self.T = [[] for i in range(N)]
        if not callable(self.hash_function) is True:
            raise TypeError('hash function must be callable')
        if not type(self.N) is int:
            raise TypeError('table size must be an integer')


    def add(self, key, value):
        if key is None:
            return None
        start_slot = self.hash_function(key, self.N)
        self.T[start_slot].append((key, value))
        return True

    def search(self, key):
        if key is None:
            return None
        start_slot = self.hash_function(key, self.N)
        for k, v in self.T[start_slot]:
            if key == k:
                return v
        return None


class QuadraticProbe:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N
        self.T = [None for i in range(N)]
        if not callable(self.hash_function) is True:
            raise TypeError('hash function must be callable')
        if not type(self.N) is int:
            raise TypeError('table size must be an integer')

    def add(self, key, value):
        if key is None:
            return None
        start_slot = self.hash_function(key, self.N)
        for i in range(self.N):
            test_slot = (start_slot + (i ** 2)) % self.N
            if self.T[test_slot] is None:
                self.T[test_slot] = (key, value)
                return True
        return False

    def search(self, key):
        if key is None:
            return None
        start_slot = self.hash_function(key, self.N)
        for i in range(self.N):
            test_slot = (start_slot + (i ** 2)) % self.N
            if self.T[test_slot] is None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        return None
