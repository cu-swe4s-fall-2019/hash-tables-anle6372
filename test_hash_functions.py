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

    def test_ascaii_both_none(self):
        self.assertEqual(hash_functions.h_ascii(None, None), None)

    def test_ascaii_N_none(self):
        self.assertEqual(hash_functions.h_ascii('hello', None), None)

    def test_ascaii_key_none(self):
        self.assertEqual(hash_functions.h_ascii(None, 5), None)

# Testing null input
class TestNullColumn(unittest.TestCase):

    def test_ascaii_null(self):
        self.assertRaises(TypeError, lambda: hash_functions.h_ascii())

# Testing incorrect input types
class TestIncorrectInput(unittest.TestCase):

    def test_ascaii_key_non_string(self):
        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii(int(4), 8))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii(float(4), 8))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii([5, 6], 8))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii(True, 8))

    def test_ascaii_length_non_int(self):
        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii('string', float(420.69)))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii('string', 'string'))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii('string', True))

        self.assertRaises(TypeError,
                          lambda: hash_functions.h_ascii('string', [9, 10]))

# Testing bad table length input
class TestBadTableLength(unittest.TestCase):

    def test_ascaii_bad_table(self):
        self.assertEqual(hash_functions.h_ascii('string', 0), None)

    def test_ascaii_bad_table(self):
        self.assertEqual(hash_functions.h_ascii('string', -42), None)

# Testing variable cases
class TestVariable(unittest.TestCase):

    def test_ascaii(self):
        letters = string.ascii_lowercase
        for i in range(100):
            sum = 0
            test_length = rdm.randint(1, 100)
            test_key = ''
            for j in range(rdm.randint(1, 100)):
                letter = rdm.choice(letters)
                test_key += letter
            for k in range(len(test_key)):
                sum += ord(test_key[k])
            r = sum % test_length
            self.assertEqual(hash_functions.h_ascii(test_key, test_length), r)


if __name__ == '__main__':
    unittest.main()