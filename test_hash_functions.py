"""Unittesting framework for hash_functions.py
Parameters
----------
None
Returns
-------
None
"""

import unittest
import hash_functions
import string
import random as rdm

# Testing none input
class TestNone(unittest.TestCase):

    def test_ascii_both_none(self):
        self.assertEqual(hash_functions.h_ascii(None, None), None)

    def test_ascii_N_none(self):
        self.assertEqual(hash_functions.h_ascii('hello', None), None)

    def test_ascii_key_none(self):
        self.assertEqual(hash_functions.h_ascii(None, 5), None)

    def test_rolling_both_none(self):
        self.assertEqual(hash_functions.h_rolling(None, None), None)

    def test_rolling_N_none(self):
        self.assertEqual(hash_functions.h_rolling('hello', None), None)

    def test_rolling_key_none(self):
        self.assertEqual(hash_functions.h_rolling(None, 5), None)

    def test_ascii_sq_both_none(self):
        self.assertEqual(hash_functions.h_ascii_sq(None, None), None)

    def test_ascii_sq_N_none(self):
        self.assertEqual(hash_functions.h_ascii_sq('hello', None), None)

    def test_ascii_sq_key_none(self):
        self.assertEqual(hash_functions.h_ascii_sq(None, 5), None)

# Testing null input
class TestNullColumn(unittest.TestCase):

    def test_ascii_null(self):
        self.assertRaises(TypeError, lambda: hash_functions.h_ascii())

    def test_rolling_null(self):
        self.assertRaises(TypeError, lambda: hash_functions.h_rolling())

    def test_ascii_sq_null(self):
        self.assertRaises(TypeError, lambda: hash_functions.h_ascii_sq())

# Testing incorrect input types
class TestIncorrectInput(unittest.TestCase):

    def test_ascii_key_non_string(self):
        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii(int(4), 8))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii(float(4), 8))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii([5, 6], 8))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii(True, 8))

    def test_ascii_length_non_int(self):
        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii('string', float(420.69)))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii('string', 'string'))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii('string', True))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii('string', [9, 10]))

    def test_rolling_key_non_string(self):
        self.assertRaises(TypeError,
                          lambda: hash_functions.h_rolling(int(4), 8))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_rolling(float(4), 8))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_rolling([5, 6], 8))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_rolling(True, 8))

    def test_rolling_length_non_int(self):
        self.assertRaises(TypeError,
                          lambda: hash_functions.h_rolling('string', float(420.69)))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_rolling('string', 'string'))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_rolling('string', True))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_rolling('string', [9, 10]))

    def test_ascii_sq_key_non_string(self):
        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii_sq(int(4), 8))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii_sq(float(4), 8))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii_sq([5, 6], 8))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii_sq(True, 8))

    def test_ascii_sq_length_non_int(self):
        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii_sq('string', float(420.69)))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii_sq('string', 'string'))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii_sq('string', True))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii_sq('string', [9, 10]))

# Testing bad table length input
class TestBadTableLength(unittest.TestCase):

    def test_ascii_zero_table(self):
        self.assertEqual(hash_functions.h_ascii('string', 0), None)

    def test_ascii_neg_table(self):
        self.assertEqual(hash_functions.h_ascii('string', -42), None)

    def test_rolling_zero_table(self):
        self.assertEqual(hash_functions.h_rolling('string', 0), None)

    def test_rolling_neg_table(self):
        self.assertEqual(hash_functions.h_rolling('string', -42), None)

    def test_ascii_sq_zero_table(self):
        self.assertEqual(hash_functions.h_ascii_sq('string', 0), None)

    def test_ascii_sq_neg_table(self):
        self.assertEqual(hash_functions.h_ascii_sq('string', -42), None)

# Testing variable cases
class TestVariable(unittest.TestCase):

    def test_ascii(self):
        letters = string.ascii_lowercase + string.ascii_uppercase
        for i in range(100):
            sum_ = 0
            test_length = rdm.randint(1, 100)
            test_key = ''
            for j in range(rdm.randint(1, 100)):
                letter = rdm.choice(letters)
                test_key += letter
            for k in range(len(test_key)):
                sum_ += ord(test_key[k])
            r = sum_ % test_length
            self.assertEqual(hash_functions.h_ascii(test_key, test_length), r)

    def test_rolling(self):
        letters = string.ascii_lowercase + string.ascii_uppercase
        for i in range(100):
            sum_ = 0
            p = 53
            m = 2 ** 64
            test_length = rdm.randint(1, 100)
            test_key = ''
            for j in range(rdm.randint(1, 100)):
                letter = rdm.choice(letters)
                test_key += letter
            for k in range(len(test_key)):
                sum_ = 0
                for i in range(len(test_key)):
                    sum_ += ord(test_key[i]) * p ** i
                sum_ = sum_ % m
                r = sum_ % test_length
            self.assertEqual(hash_functions.h_rolling(test_key, test_length), r)

    def test_ascii_sq(self):
        letters = string.ascii_lowercase + string.ascii_uppercase
        for i in range(100):
            sum_sq = 0
            test_length = rdm.randint(1, 100)
            test_key = ''
            for j in range(rdm.randint(1, 100)):
                letter = rdm.choice(letters)
                test_key += letter
            for k in range(len(test_key)):
                sum_sq += ord(test_key[k]) ** 2
            r = sum_sq % test_length
            self.assertEqual(hash_functions.h_ascii_sq(test_key, test_length), r)

if __name__ == '__main__':
    unittest.main()