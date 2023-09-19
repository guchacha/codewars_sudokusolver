import numpy as np


def sudoku(puzzle):

    grid = np.array(puzzle)
    print(f"Puzzle to solve:\n{grid}")
    zeros = np.count_nonzero(grid == 0)
    print(f"Number of unknowns: {zeros}\n")

    round_counter = 1
    while zeros > 0:
        print(f"--Round {round_counter}--")

        for box_row in [0, 3, 6]:
            for box_col in [0, 3, 6]:
                for value in [1, 2, 3, 4, 5, 6, 7, 8, 9]:

                    box = np.copy(grid[box_row:box_row + 3, box_col:box_col + 3])
                    if value not in box:
                        for square_row in [box_row, box_row + 1, box_row + 2]:
                            if value in grid[square_row, 0:9]:
                                box[square_row - box_row, :] = [10, 10, 10]
                        for square_col in [box_col, box_col + 1, box_col + 2]:
                            if value in grid[0:9, square_col]:
                                box[:, square_col - box_col] = [10, 10, 10]

                        if np.count_nonzero(box == 0) == 1:
                            zero_pos = np.argwhere(box == 0)
                            grid[zero_pos[0][0] + box_row, zero_pos[0][1] + box_col] = value
                            print(f"Value: {value} on the position: {zero_pos[0]}")

        zeros = np.count_nonzero(grid == 0)
        print(f"Remaining number of unknowns: {zeros}\n")
        round_counter = round_counter + 1

    print(f"Puzzle solved!:\n{grid}")
    return grid.tolist()
