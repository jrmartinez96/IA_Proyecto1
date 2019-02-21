# Universidad del Valle de Guatemala
# Inteligencia Artificail
#
# Proyecto 1 (Sudoku)
# Jose Martinez 15163

import math

def get_fifteen_matrix(fifteenString):
    fifteenMatrix = [[0 for x in range(4)] for y in range(4)]
    for nRow in range(4):
        for nCol in range(4):
            if fifteenString[(nRow * 4) + nCol] == '.':
                fifteenMatrix[nRow][nCol] = 0
            else:
                fifteenMatrix[nRow][nCol] = int(fifteenString[(nRow * 4) + nCol], 16)
    return fifteenMatrix


def print_fifteen(fiftenn_matrix):
    i_row = 0
    print("+------------------------------+")
    for r in fiftenn_matrix:

        row_string = ''
        i_col = 0
        for c in r:
            cStr = " "
            if c != 0:
                cStr = str(c)

            row_string = row_string + "|\t" + cStr + "\t"
            i_col += 1
        row_string = row_string + "|"
        print(row_string)
        i_row += 1

        if i_row == len(fiftenn_matrix):
            print("+------------------------------+")
        else:
            print("|-------|-------|------|-------|")


def find_white_space(fifteen_matrix):
    space = []

    i=0
    for row in fifteen_matrix:
        j = 0
        for col in row:
            if col == 0:
                space = [i, j]
            j += 1
        i += 1

    return space


def movements_to_final(fifteen_matrix, space, numbers_tried, path):
    final_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

    # Get row an col
    row_i_fifteen_matrix = space[0]
    col_j_fifteen_matrix = space[1]

    # Get value of the space to check distance
    value_fifteen_matrix = fifteen_matrix[row_i_fifteen_matrix][col_j_fifteen_matrix]

    den = 1
    for key, value in numbers_tried.items():
        den = den + value

    movements = (numbers_tried[str(value_fifteen_matrix)] / den) * 16
    try:
        if path[-2] == change_value_fifteen(fifteen_matrix.copy(), space):
            movements = 64 * (numbers_tried[str(value_fifteen_matrix)] / den)
    except:
        movements = movements


    return movements


def distance_of_block_to_final(fifteen_matrix, space):
    final_matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]

    # Get row an col
    row_i_fifteen_matrix = space[0]
    col_j_fifteen_matrix = space[1]

    # Get value of the space to check distance
    value_fifteen_matrix = fifteen_matrix[row_i_fifteen_matrix][col_j_fifteen_matrix]

    # Get the space where it's value is 0
    white_space = find_white_space(fifteen_matrix)

    space_final_matrix = []

    row_i_final_matrix = 0
    for row in final_matrix:
        col_j_final_matrix = 0
        for col in row:
            if col == value_fifteen_matrix:
                space_final_matrix = [row_i_final_matrix, col_j_final_matrix]
            col_j_final_matrix += 1
        row_i_final_matrix += 1

    distance = math.sqrt((space[0] - space_final_matrix[0]) ** 2 + (space[1] - space_final_matrix[1]) ** 2)

    return distance *-1


def end_condition(fifteen_matrix):
    final_matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]

    if(fifteen_matrix == final_matrix):
        return False

    return True


def find_possible_blocks_to_move(fifteen_matrix):
    blocks = []

    white_space = find_white_space(fifteen_matrix)

    white_space_row = white_space[0]
    white_space_col = white_space[1]

    blocks.append([white_space_row - 1, white_space_col]) # Upper space
    blocks.append([white_space_row, white_space_col + 1]) # Right space
    blocks.append([white_space_row + 1, white_space_col]) # Down space
    blocks.append([white_space_row, white_space_col - 1]) # Left space

    blocks_to_remove = []
    for space in blocks:
        space_row = space[0]
        space_col = space[1]

        if ((space_row < 0) or (space_row > 3)) or ((space_col < 0) or (space_col > 3)):
            blocks_to_remove.append(space)

    for space in blocks_to_remove:
        blocks.remove(space)

    return blocks

def change_value_fifteen(fifteen_matrix, selected_space):
    # Get white space
    white_space = find_white_space(fifteen_matrix)

    # Get value to move
    value_to_move = fifteen_matrix[selected_space[0]][selected_space[1]]

    # White space row copy
    white_space_row_copy = fifteen_matrix[white_space[0]].copy()

    # Value space row copy
    value_space_row_copy = fifteen_matrix[selected_space[0]].copy()

    # Change values of rows copies
    if selected_space[0] == white_space[0]:
        white_space_row_copy[white_space[1]] = value_to_move
        white_space_row_copy[selected_space[1]] = 0
    else:
        white_space_row_copy[white_space[1]] = value_to_move
        value_space_row_copy[selected_space[1]] = 0

    # Change rows in matrix
    if selected_space[0] == white_space[0]:
        fifteen_matrix[white_space[0]] = white_space_row_copy
    else:
        fifteen_matrix[white_space[0]] = white_space_row_copy
        fifteen_matrix[selected_space[0]] = value_space_row_copy

    return fifteen_matrix


def change_path_fifteen(path, numbers_tried, selected_space):
    fifteen_matrix = path[-1].copy()
    value = fifteen_matrix[selected_space[0]][selected_space[1]]
    numbers_tried[str(value)] = numbers_tried[str(value)] + 1

    new_fifteen_matrix = change_value_fifteen(fifteen_matrix, selected_space)

    if len(path) % 1000 == 0:
        print_fifteen(new_fifteen_matrix)
    elif not end_condition(new_fifteen_matrix):
        print_fifteen(new_fifteen_matrix)
    #print_fifteen(new_fifteen_matrix)


    path.append(new_fifteen_matrix)
