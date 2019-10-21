# Hash tables

## hash_functions.py

    1. Created testing file test_hash_functions.py
        - Created tests for None input
        - Created tests for null input
        - Created tests for incorrect type input
        - Created looped test for accurate functionality


    2. Added h_ascii(key, N) method
        Description: hash function that returns a integer value within range(N) given a string
        Parameters:
            - key : string that is to be converted into a integer within the range(N)
            - N : integer that represents the size of the hash table
        
        Returns:
            - r : the hash position of string key in table of length N
        
        Error Behavior
            - Returns None given None
            - Throws TypeError given null input
            - Throws TypeError given non-list input
            - Returns None for any invalid list lengths
     
    3. Added h_rolling(key, N) method
        Description: hash function that returns a integer value within range(N) given a string
        Parameters:
            - key : string that is to be converted into a integer within the range(N)
                + currently optmized to consist only of upper and lower case letters
            - N : integer that represents the size of the hash table
        
        Returns:
            - r : the hash position of string key in table of length N
        
        Error Behavior
            - Returns None given None
            - Throws TypeError given null input
            - Throws TypeError given non-list input
            - Returns None for any invalid list lengths
     
    4. Added h_ascii_sq(key, N) method
        Description: hash function that returns a integer value within range(N) given a string
        Parameters:
            - key : string that is to be converted into a integer within the range(N)
            - N : integer that represents the size of the hash table
        
        Returns:
            - r : the hash position of string key in table of length N
        
        Error Behavior
            - Returns None given None
            - Throws TypeError given null input
            - Throws TypeError given non-list input
            - Returns None for any invalid list lengths

## hash_tables.py

    1. Created testing file test_hash_tables.py
        - Created tests for incorrect type input
        - Created tests for None class function input
        - Created looped test for accurate functionality


    2. Created class LinearProbe:
        Description: hash table class that stores (key, value), utilizes linear probe collision resolution
        Parameters:
            - self.hash_function: the hash function to be used in the table
            - self.N: the size of the hash table to be created
        
        Returns:
            - self.T: the hash table data object created
        
        Functions:
            - add(self, key, value):
                Parameters:
                    + key: a string that is to be used to place the (key, value) pair
                    + value: the integer value assocaited with the key
                Returns:
                    + True: successful addition to hash table
                    + False: unsuccessful addition to hash table

            - search(self, key):
                 Parameters:
                    + key: a string that is to be used to locate the value in the correct (key, value) pair
                Returns:
                    + value: the value associated with the key stored in the hash table
          
        Error Behavior
            - Throws Syntax Error given null input
            - Throws TypeError given incorrect input
            - Returns None given null function inputs
     

    3. Created class ChainedHash:
        Description: hash table class that stores (key, value), utilizes chained hash collision resolution
        Parameters:
            - self.hash_function: the hash function to be used in the table
            - self.N: the size of the hash table to be created
        
        Returns:
            - self.T: the hash table data object created
        
        Functions:
            - add(self, key, value):
                Parameters:
                    + key: a string that is to be used to place the (key, value) pair
                    + value: the integer value assocaited with the key
                Returns:
                    + True: successful addition to hash table
                    + False: unsuccessful addition to hash table

            - search(self, key):
                 Parameters:
                    + key: a string that is to be used to locate the value in the correct (key, value) pair
                Returns:
                    + value: the value associated with the key stored in the hash table
          
        Error Behavior
            - Throws Syntax Error given null input
            - Throws TypeError given incorrect input
            - Returns None given null function inputs

    4. Created class QuadraticProbe:
        Description: hash table class that stores (key, value), utilizes quadratic probe collision resolution
        Parameters:
            - self.hash_function: the hash function to be used in the table
            - self.N: the size of the hash table to be created
        
        Returns:
            - self.T: the hash table data object created
        
        Functions:
            - add(self, key, value):
                Parameters:
                    + key: a string that is to be used to place the (key, value) pair
                    + value: the integer value assocaited with the key
                Returns:
                    + True: successful addition to hash table
                    + False: unsuccessful addition to hash table

            - search(self, key):
                 Parameters:
                    + key: a string that is to be used to locate the value in the correct (key, value) pair
                Returns:
                    + value: the value associated with the key stored in the hash table
          
        Error Behavior
            - Throws Syntax Error given null input
            - Throws TypeError given incorrect input
            - Returns None given null function inputs