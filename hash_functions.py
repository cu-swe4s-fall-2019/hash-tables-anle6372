"""Library of hash functions with function testing in main
main:
    Parameters
    ----------
    --input_file : file containing list of strings to be hashed to integers
    --function: hash function to be used
    (options: 'ascii', 'rolling', 'asciisq')

    Returns
    -------
    prints hashed values to stdout

functions:
    Parameters
    ----------
    key : string that is to be converted into a integer within the range(N)
    N : integer that represents the size of the hash table


    Returns
    -------
    r : the hash position of string key in table of length N
"""
import argparse


def main():

    parser = argparse.ArgumentParser(description='Create scatter plots'
                                                 ' with data from stdin.')

    parser.add_argument('--input_file', type=str,
                        help='Name of the output file', required=True)
    parser.add_argument('--function', type=str,
                        help='Name of the output file', required=True)

    args = parser.parse_args()

    for l in open(args.input_file):
        if args.function == 'ascii':
            print(h_ascii(l, 1000))
        elif args.function == 'rolling':
            print(h_rolling(l, 1000))
        elif args.function == 'asciisq':
            print(h_ascii_sq(l, 1000))


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


if __name__ == '__main__':
    main()
