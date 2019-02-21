# Universidad del Valle de Guatemala
# Inteligencia Artificail
#
# Proyecto 1 (Sudoku)
# Jose Martinez 15163

import Sudoku.printing as printing

# Get a sudoku matrix from a string
def get_sudoku_matrix(sudoku_string):
    sudokuMatrix = [[0 for x in range(4)] for y in range(4)]
    for nRow in range(4):
        for nCol in range(4):
            sudokuMatrix[nRow][nCol] = sudoku_string[(nRow * 4) + nCol]
    return sudokuMatrix


# Set a value to a space in a sudoku matrix
def change_space_value(sudoku_matrix, space, value):
    row = space[0]
    col = space[1]

    s2 = sudoku_matrix.copy()
    s21 = sudoku_matrix[row].copy()

    s21[col] = str(value)

    s2[row] = s21

    return s2


# Returns an array with the white spaces of the sudoku matrix [[row, col], [row], [col]]
def find_white_spaces(sudoku_matrix):
    white_spaces = []
    i_row = 0
    for n_row in sudoku_matrix:
        i_col = 0
        for n_col in n_row:
            if n_col == '.':
                white_spaces.append([i_row, i_col])
            i_col +=1
        i_row += 1

    return white_spaces


def end_condition(sudoku_matrix):
    stay_in_condition = True
    if len(find_white_spaces(sudoku_matrix)) == 0:
        stay_in_condition = False
    return stay_in_condition

# Returns the number of free spaces in the space, just constraints from row and col
def find_n_free_spaces_in_space(sudoku_matrix, space):
    row = space[0]
    col = space[1]

    n_constraints_in_row = 0
    n_constraints_in_col = 0

    # find number of constraints in row
    for n_col in range(0,4):
        if sudoku_matrix[row][n_col] == '.':
            n_constraints_in_row += 1

    # find number of constraints in col
    for n_row in range(0,4):
        if sudoku_matrix[n_row][col] == '.':
            n_constraints_in_col += 1

    total_constraints = n_constraints_in_row + n_constraints_in_row

    return total_constraints


# Returns the number of free spaces in the box where the space is
def find_n_free_spaces_in_box(sudoku_matrix, space, numbers_tried, path):
    row = space[0]
    col = space[1]

    n_constraints_in_box = 0

    # find number of constraints in box
    if row < 2:
        if col < 2:
            for n_row in range(0, 2):
                for n_col in range(0, 2):
                    if sudoku_matrix[n_row][n_col] == '.':
                        n_constraints_in_box += 1
        else:
            for n_row in range(0, 2):
                for n_col in range(2, 4):
                    if sudoku_matrix[n_row][n_col] == '.':
                        n_constraints_in_box += 1
    else:
        if col < 2:
            for n_row in range(2, 4):
                for n_col in range(0, 2):
                    if sudoku_matrix[n_row][n_col] == '.':
                        n_constraints_in_box += 1
        else:
            for n_row in range(2, 4):
                for n_col in range(2, 4):
                    if sudoku_matrix[n_row][n_col] == '.':
                        n_constraints_in_box += 1

    return n_constraints_in_box


# Checks if the sudoku is possible with the value of the space
def check_possible_sudoku(sudoku_matrix, space):
    row = space[0]
    col = space[1]
    value = sudoku_matrix[row][col]

    possible_row = True
    possible_col = True
    possible_box = True

    # find number of constraints in row
    for n_col in range(0, 4):
        if sudoku_matrix[row][n_col] == value and col != n_col and possible_row:
            possible_row = False

    # find number of constraints in col
    for n_row in range(0, 4):
        if sudoku_matrix[n_row][col] == value and row != n_row and possible_col:
            possible_col = False

    # find number of constraints in box
    if row < 2:
        if col < 2:
            for n_row in range(0, 2):
                for n_col in range(0, 2):
                    if sudoku_matrix[n_row][n_col] == value and (n_row != row or n_col != col) and possible_box:
                        possible_box = False
        else:
            for n_row in range(0, 2):
                for n_col in range(2, 4):
                    if sudoku_matrix[n_row][n_col] == value and (n_row != row or n_col != col) and possible_box:
                        possible_box = False
    else:
        if col < 2:
            for n_row in range(2, 4):
                for n_col in range(0, 2):
                    if sudoku_matrix[n_row][n_col] == value and (n_row != row or n_col != col) and possible_box:
                        possible_box = False
        else:
            for n_row in range(2, 4):
                for n_col in range(2, 4):
                    if sudoku_matrix[n_row][n_col] == value and (n_row != row or n_col != col) and possible_box:
                        possible_box = False

    return possible_row and possible_col and possible_box

def change_value_path(path, numbers_tried, selected_space):
    last_sudoku = path[-1]
    last_numbers_tired = numbers_tried[-1]

    if len(last_numbers_tired) < 5:
        number_to_try = len(last_numbers_tired) + 1
        possible_sudoku_matrix = change_space_value(last_sudoku, selected_space, number_to_try)

        numbers_tried[len(numbers_tried) - 1].append(1)
        is_possible = check_possible_sudoku(possible_sudoku_matrix, selected_space)
        if is_possible:
            path.append(possible_sudoku_matrix)
            numbers_tried.append([])
        else:
            if len(last_numbers_tired) == 4:
                path.pop()
                numbers_tried.pop()

    printing.print_sudoku(path[-1])