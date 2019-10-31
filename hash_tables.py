"""Library of classes that create hash tables with variable
 hash functions and resolution strategies.
Note main also contains infrastructure for experimentation

Library:
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
        Boolean: True indicates successful addition,
         false indicates unsuccessful addition

search(self, key):
    parameters:
        key: the key corresponding to the value at the hashed position
    returns: value corresponding to the given key

Returns
-------
Hash Table: A class object that is the data structure
 utilizing the hash function and desired size

Main:
main:
    Parameters
    ----------
    --input_file : file containing list of strings to be
     hashed to integers
    --table size: desired size of the hash table
    --hash_alg: hash function to be used (options:
     'ascii', 'rolling', 'asciisq')
    --res_strat: type of collision resolution strategy to be used
    --num_keys: number of keys to be sampled

    Returns
    -------
    prints hashed values to stdout
"""
import argparse
import hash_functions as hf
import time
import random


def main():

    parser = argparse.ArgumentParser(description='Create scatter plots'
                                                 ' with data from stdin.')

    parser.add_argument('--input_file', type=str,
                        help='size of the hash table', required=True)
    parser.add_argument('--table_size', type=str,
                        help='size of the hash table', required=True)
    parser.add_argument('--hash_alg', type=str,
                        help='type of hash function used', required=True)
    parser.add_argument('--res_strat', type=str,
                        help='type of collision resolution strategy',
                        required=True)
    parser.add_argument('--num_keys', type=str,
                        help='number of keys to be added', required=True)

    args = parser.parse_args()

    N = int(args.table_size)
    hash_alg = args.hash_alg
    collision_strategy = args.res_strat
    data_file_name = args.input_file
    keys_to_add = int(args.num_keys)

    ht = None

    if hash_alg == 'ascii':

        if collision_strategy == 'linear':
            ht = LinearProbe(N, hf.h_ascii)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, hf.h_ascii)
        elif collision_strategy == 'quadratic':
            ht = QuadraticProbe(N, hf.h_ascii)

    elif hash_alg == 'rolling':

        if collision_strategy == 'linear':
            ht = LinearProbe(N, hf.h_rolling)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, hf.h_rolling)
        elif collision_strategy == 'quadratic':
            ht = QuadraticProbe(N, hf.h_rolling)

    elif hash_alg == 'asciisq':

        if collision_strategy == 'linear':
            ht = LinearProbe(N, hf.h_ascii_sq)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, hf.h_ascii_sq)
        elif collision_strategy == 'quadratic':
            ht = QuadraticProbe(N, hf.h_ascii_sq)

    keys_to_search = 100
    V = []

    for l in open(data_file_name):
        reservoir_sampling(l, keys_to_search, V)
        t0 = time.time()
        ht.add(l, l)
        t1 = time.time()
        print('insert', ht.M/ht.N, t1 - t0)
        if ht.M == keys_to_add:
            break

    for v in V:
        t0 = time.time()
        r = ht.search(v)
        t1 = time.time()
        print('search', t1 - t0)


class LinearProbe:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N
        self.T = [None for i in range(N)]
        self.M = 0
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
                self.M += 1
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
        self.M = 0
        self.keys = []
        if not callable(self.hash_function) is True:
            raise TypeError('hash function must be callable')
        if not type(self.N) is int:
            raise TypeError('table size must be an integer')

    def add(self, key, value):
        if key is None:
            return None
        start_slot = self.hash_function(key, self.N)
        self.T[start_slot].append((key, value))
        self.M += 1
        self.keys.append(key)
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
        self.M = 0
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
                self.M += 1
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


def reservoir_sampling(new_val, size, V):
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val


if __name__ == '__main__':
    main()
