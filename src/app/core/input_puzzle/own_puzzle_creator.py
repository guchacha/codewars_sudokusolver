import numpy as np


def puzzle_creator() -> list:
    """
    Function preparing users puzzle from users inputs.
    :return: 9x9 2d list of integers with sudoku puzzle ready to solve, unknown values as number 0
    """

    # rows entering with input validation
    print("To prepare your own puzzle enter row after row. Unknown value enter as number 0.")
    own_puzzle = []
    for r in range(9):
        while True:
            row = input("Enter 9 numbers without spaces: ")
            if len(row) == 9 and row.isdigit():
                row = [int(x) for x in row]
                own_puzzle.append(row)
                break
            else:
                print("Incorrect input, enter this row again.")
                continue
    print(f"Your puzzle:\n{np.array(own_puzzle)}\n")

    # value correction if needed and puzzle approving
    while True:
        answer = input("To approve and solve your puzzle type letter A\n"
                       "To correct your puzzle type letter C:")
        if answer.lower() == "a":
            print("\nYou approved your puzzle, solve it.\n")
            break
        elif answer.lower() == "c":
            answer_row = int(input("Row number (from 1 to 9) of corrected value:"))
            answer_col = int(input("Column number (from 1 to 9) of corrected value:"))
            answer_val = int(input("Correct value:"))
            own_puzzle[answer_row-1][answer_col-1] = answer_val
            print(f"Your puzzle:\n{np.array(own_puzzle)}")
            continue
        else:
            print("Incorrect input, answer again: A or C.")
            continue

    return own_puzzle
