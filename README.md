# Hash tables

## hast_functions.py

    1. Created testing file test_hash_functions.py
        - Created tests for None input
        - Created tests for null input
        - Created tests for incorrect type input
        - Created looped test for accurate functionality


    2. Added h_ascii(key, N) method
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