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

    def process_file(self):
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError
            table = str.maketrans("", "", string.punctuation)
            with self.__filepath.open() as file:
                for line in file:
                    for word in line.translate(table).lower().split():
                        self.__frequencies[word] = self.__frequencies.get(word, 0) + 1
            return True
        except FileNotFoundError:
            print("File not found.")
            return False

    def print_report(self):
        for word in sorted(self.__frequencies.keys()):
            print(f"{word:<15} :: {self.__frequencies[word]}")

def main():
    base = pathlib.Path(__file__). parent
    files = {
        "1": base / "princess_mars.txt",
        "2": base / "Tarzan.txt",
        "3": base / "treasure_island.txt",
        "4": base / "monte_cristo.txt",
    }
    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        for key, path in files.items():
            print(f"{key}. {path.name}")
        print("5. Exit")
        break