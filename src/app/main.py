from src.app.core.sudoku_solver import sudoku
from src.app.core.input_puzzle.random_sample_puzzle import random_puzzle
from src.app.core.input_puzzle.own_puzzle_creator import puzzle_creator

if __name__ == "__main__":
    answer = input("===Sudoku solver===\n"
                   "To solve sample puzzle type letter S\n"
                   "To solve your own puzzle type letter O\n"
                   "To exit type anything else: ")
    if answer.lower() == "s":
        print("\nYou chose to solve the sample puzzle.\n")
        sudoku(random_puzzle())
    elif answer.lower() == "o":
        print("\nYou chose to solve you own puzzle.\n")
        sudoku(puzzle_creator())
    else:
        print("Exit")
