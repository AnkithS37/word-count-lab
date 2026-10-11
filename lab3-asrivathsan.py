"""
Program Name: Word Count
Author: Ankith Srivathsan
Purpose: Display a menu of 4 text files, let the user pick one,
and print an alphabetical report of how often each word appears
in it. 
Starter Code: None used. Written from the assignment instructions.
Date: October 11, 2026
"""

import pathlib
import string

class WordAnalyzer:
    def __init__(self, filepath):
        self.__filepath = pathlib.Path(filepath)
        self.__frequencies = {}


analyzer = WordAnalyzer("Tarzan.txt")
print(analyzer._WordAnalyzer__filepath)