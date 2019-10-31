"""Unittesting framework for hash_tables.py
Parameters
----------
None
Returns
-------
None
"""

import unittest
import hash_functions as hf
import hash_tables as ht
import string
import random as rdm


# Testing bad input
class TestBadInput(unittest.TestCase):

    def test_linear_probe_bad_fxn(self):
        self.assertRaises(TypeError, lambda: ht.LinearProbe(5, None))
        self.assertRaises(TypeError, lambda: ht.LinearProbe(5, 'string'))
        self.assertRaises(TypeError, lambda: ht.LinearProbe(5, int(5)))
        self.assertRaises(TypeError, lambda: ht.LinearProbe(5, float(420.69)))

    def test_linear_probe_bad_size(self):
        self.assertRaises(TypeError,
                          lambda: ht.LinearProbe(None, hf.h_ascii))
        self.assertRaises(TypeError,
                          lambda: ht.LinearProbe('string', hf.h_ascii))
        self.assertRaises(TypeError,
                          lambda: ht.LinearProbe(sum, hf.h_ascii))
        self.assertRaises(TypeError,
                          lambda: ht.LinearProbe(float(420.69), hf.h_ascii))

    def test_chained_hash_bad_fxn(self):
        self.assertRaises(TypeError, lambda: ht.ChainedHash(5, None))
        self.assertRaises(TypeError, lambda: ht.ChainedHash(5, 'string'))
        self.assertRaises(TypeError, lambda: ht.ChainedHash(5, int(5)))
        self.assertRaises(TypeError, lambda: ht.ChainedHash(5, float(420.69)))

    def test_chained_hash_bad_size(self):
        self.assertRaises(TypeError, lambda: ht.ChainedHash(None, hf.h_ascii))
        self.assertRaises(TypeError,
                          lambda: ht.ChainedHash('string', hf.h_ascii))
        self.assertRaises(TypeError, lambda: ht.ChainedHash(sum, hf.h_ascii))
        self.assertRaises(TypeError,
                          lambda: ht.ChainedHash(float(420.69), hf.h_ascii))

    def test_quadratic_probe_bad_fxn(self):
        self.assertRaises(TypeError, lambda: ht.QuadraticProbe(5, None))
        self.assertRaises(TypeError, lambda: ht.QuadraticProbe(5, 'string'))
        self.assertRaises(TypeError, lambda: ht.QuadraticProbe(5, int(5)))
        self.assertRaises(TypeError,
                          lambda: ht.QuadraticProbe(5, float(420.69)))

    def test_quadratic_probe_bad_size(self):
        self.assertRaises(TypeError,
                          lambda: ht.QuadraticProbe(None, hf.h_ascii))
        self.assertRaises(TypeError,
                          lambda: ht.QuadraticProbe('string', hf.h_ascii))
        self.assertRaises(TypeError,
                          lambda: ht.QuadraticProbe(sum, hf.h_ascii))
        self.assertRaises(TypeError,
                          lambda: ht.QuadraticProbe(float(420.69), hf.h_ascii))


# Testing None function input
class TestNoneFxnInput(unittest.TestCase):

    def test_linear_probe_add_key_none(self):
        test_table = ht.LinearProbe(5, hf.h_ascii)
        self.assertEqual(None, test_table.add(None, 420))

    def test_linear_probe_search_key_none(self):
        test_table = ht.LinearProbe(5, hf.h_ascii)
        self.assertEqual(None, test_table.search(None))

    def test_chained_hash_add_key_none(self):
        test_table = ht.ChainedHash(5, hf.h_ascii)
        self.assertEqual(None, test_table.add(None, 420))

    def test_chained_hash_search_key_none(self):
        test_table = ht.ChainedHash(5, hf.h_ascii)
        self.assertEqual(None, test_table.search(None))

    def test_chained_hash_add_key_none(self):
        test_table = ht.QuadraticProbe(5, hf.h_ascii)
        self.assertEqual(None, test_table.add(None, 420))

    def test_chained_hash_search_key_none(self):
        test_table = ht.QuadraticProbe(5, hf.h_ascii)
        self.assertEqual(None, test_table.search(None))


# Testing linear probing functionality
class TestVariableAdditionSearchLP(unittest.TestCase):

    def test_linear_probe_ascii_variable_add_search(self):
        for i in range(100):
            test_length = rdm.randint(1, 100)
            letters = string.ascii_lowercase + string.ascii_uppercase
            test_value = rdm.randint
            test_key = ''
            for j in range(rdm.randint(1, 100)):
                letter = rdm.choice(letters)
                test_key += letter
            test_table = ht.LinearProbe(test_length, hf.h_ascii)
            test_table.add(test_key, test_value)
            self.assertEqual((test_key, test_value),
                             test_table.T[hf.h_ascii(test_key, test_length)])
            self.assertEqual(test_value, test_table.search(test_key))

    def test_linear_probe_rolling_variable_add_search(self):
        for i in range(100):
            test_length = rdm.randint(1, 100)
            letters = string.ascii_lowercase + string.ascii_uppercase
            test_value = rdm.randint
            test_key = ''
            for j in range(rdm.randint(1, 100)):
                letter = rdm.choice(letters)
                test_key += letter
            test_table = ht.LinearProbe(test_length, hf.h_rolling)
            test_table.add(test_key, test_value)
            self.assertEqual((test_key, test_value),
                             test_table.T[hf.h_rolling(test_key, test_length)])
            self.assertEqual(test_value, test_table.search(test_key))

    def test_linear_probe_ascii_collision(self):
        for i in range(100):
            test_length = rdm.randint(2, 1000)
            test_value1 = rdm.randint(1, 1000)
            test_value2 = rdm.randint(1, 1000)
            test_key = 'teststring'
            test_table = ht.LinearProbe(test_length, hf.h_ascii)
            test_table.add(test_key, test_value1)
            test_table.add(test_key, test_value2)
            self.assertEqual(test_value1, test_table.search(test_key))
            if test_table.N - 1 == hf.h_ascii(test_key, test_length):
                self.assertEqual((test_key, test_value2), test_table.T[0])
                continue
            self.assertEqual((test_key, test_value2),
                             test_table.T[hf.h_ascii(
                                 test_key, test_length) + 1])

    def test_linear_probe_rolling_collision(self):
        for i in range(100):
            test_length = rdm.randint(2, 1000)
            test_value1 = rdm.randint(1, 1000)
            test_value2 = rdm.randint(1, 1000)
            test_key = 'teststring'
            test_table = ht.LinearProbe(test_length, hf.h_rolling)
            test_table.add(test_key, test_value1)
            test_table.add(test_key, test_value2)
            self.assertEqual(test_value1, test_table.search(test_key))
            if test_table.N - 1 == hf.h_rolling(test_key, test_length):
                self.assertEqual((test_key, test_value2), test_table.T[0])
                continue
            self.assertEqual((test_key, test_value2),
                             test_table.T[
                                 hf.h_rolling(test_key, test_length) + 1])


# Testing chained hash functionality
class TestVariableAdditionSearchCH(unittest.TestCase):

    def test_chained_hash_ascii_variable_add_search(self):
        for i in range(100):
            test_length = rdm.randint(1, 100)
            letters = string.ascii_lowercase + string.ascii_uppercase
            test_value = rdm.randint
            test_key = ''
            for j in range(rdm.randint(1, 100)):
                letter = rdm.choice(letters)
                test_key += letter
            test_table = ht.ChainedHash(test_length, hf.h_ascii)
            test_table.add(test_key, test_value)
            self.assertEqual((test_key, test_value),
                             test_table.T[
                                 hf.h_ascii(test_key, test_length)][0])
            self.assertEqual(test_value, test_table.search(test_key))

    def test_chained_hash_rolling_variable_add_search(self):
        for i in range(100):
            test_length = rdm.randint(1, 100)
            letters = string.ascii_lowercase + string.ascii_uppercase
            test_value = rdm.randint
            test_key = ''
            for j in range(rdm.randint(1, 100)):
                letter = rdm.choice(letters)
                test_key += letter
            test_table = ht.ChainedHash(test_length, hf.h_rolling)
            test_table.add(test_key, test_value)
            self.assertEqual((test_key, test_value),
                             test_table.T[
                                 hf.h_rolling(test_key, test_length)][0])
            self.assertEqual(test_value, test_table.search(test_key))

    def test_chained_hash_ascii_collision(self):
        for i in range(100):
            test_length = rdm.randint(2, 1000)
            test_value1 = rdm.randint(1, 1000)
            test_value2 = rdm.randint(1, 1000)
            test_key = 'teststring'
            test_table = ht.ChainedHash(test_length, hf.h_ascii)
            test_table.add(test_key, test_value1)
            test_table.add(test_key, test_value2)
            self.assertEqual(test_value1,
                             test_table.search(test_key))
            self.assertEqual((test_key, test_value2),
                             test_table.T[
                                 hf.h_ascii(test_key, test_length)][1])

    def test_chained_hash_rolling_collision(self):
        for i in range(100):
            test_length = rdm.randint(2, 1000)
            test_value1 = rdm.randint(1, 1000)
            test_value2 = rdm.randint(1, 1000)
            test_key = 'teststring'
            test_table = ht.ChainedHash(test_length, hf.h_rolling)
            test_table.add(test_key, test_value1)
            test_table.add(test_key, test_value2)
            self.assertEqual(
                test_value1, test_table.search(test_key))
            self.assertEqual((test_key, test_value2),
                             test_table.T[
                                 hf.h_rolling(test_key, test_length)][1])

    # Ensures correct storage of key values
    def test_chained_hash_rolling_variable_key_store(self):
        letters = string.ascii_lowercase + string.ascii_uppercase
        for i in range(10):
            keys = []
            test_length = rdm.randint(1, 100)
            test_table = ht.ChainedHash(test_length, hf.h_rolling)
            for k in range(50):
                test_value = rdm.randint
                test_key = ''
                for j in range(rdm.randint(1, 100)):
                    letter = rdm.choice(letters)
                    test_key += letter
                keys.append(test_key)
                test_table.add(test_key, test_value)
        self.assertEqual(keys, test_table.keys)
# Testing quadratic probing functionality
class TestVariableAdditionSearchQP(unittest.TestCase):

    def test_quadratic_probe_ascii_variable_add_search(self):
        for i in range(100):
            test_length = rdm.randint(1, 100)
            letters = string.ascii_lowercase + string.ascii_uppercase
            test_value = rdm.randint
            test_key = ''
            for j in range(rdm.randint(1, 100)):
                letter = rdm.choice(letters)
                test_key += letter
            test_table = ht.QuadraticProbe(test_length, hf.h_ascii)
            test_table.add(test_key, test_value)
            self.assertEqual((test_key,
                              test_value),
                             test_table.T[hf.h_ascii(test_key, test_length)])
            self.assertEqual(test_value,
                             test_table.search(test_key))

    def test_quadratic_probe_rolling_variable_add_search(self):
        for i in range(100):
            test_length = rdm.randint(1, 100)
            letters = string.ascii_lowercase + string.ascii_uppercase
            test_value = rdm.randint
            test_key = ''
            for j in range(rdm.randint(1, 100)):
                letter = rdm.choice(letters)
                test_key += letter
            test_table = ht.QuadraticProbe(test_length, hf.h_rolling)
            test_table.add(test_key, test_value)
            self.assertEqual((test_key, test_value),
                             test_table.T[hf.h_rolling(test_key, test_length)])
            self.assertEqual(test_value, test_table.search(test_key))

    def test_quadratic_probe_ascii_collision(self):
        for i in range(100):
            test_length = rdm.randint(100, 1000)
            test_value1 = rdm.randint(1, 1000)
            test_value2 = rdm.randint(1, 1000)
            test_value3 = rdm.randint(1, 1000)
            test_key = 'teststring'
            test_table = ht.QuadraticProbe(test_length, hf.h_ascii)
            test_table.add(test_key, test_value1)
            test_table.add(test_key, test_value2)
            test_table.add(test_key, test_value3)
            self.assertEqual(test_value1, test_table.search(test_key))
            self.assertEqual((test_key, test_value2), test_table.T[(hf.h_ascii(
                test_key, test_length) + 1) % test_length])
            self.assertEqual((test_key, test_value3),
                             test_table.T[(hf.h_ascii(
                                 test_key, test_length) + 4) % test_length])

    def test_quadratic_probe_rolling_collision(self):
        for i in range(100):
            test_length = rdm.randint(100, 1000)
            test_value1 = rdm.randint(1, 1000)
            test_value2 = rdm.randint(1, 1000)
            test_value3 = rdm.randint(1, 1000)
            test_key = 'teststring'
            test_table = ht.QuadraticProbe(test_length, hf.h_rolling)
            test_table.add(test_key, test_value1)
            test_table.add(test_key, test_value2)
            test_table.add(test_key, test_value3)
            self.assertEqual(test_value1, test_table.search(test_key))
            self.assertEqual((
                test_key, test_value2), test_table.T[
                (hf.h_rolling(test_key, test_length) + 1) % test_length])
            self.assertEqual((
                test_key, test_value3), test_table.T[
                (hf.h_rolling(test_key, test_length) + 4) % test_length])


if __name__ == '__main__':
    unittest.main()
