# Universidad del Valle de Guatemala
# Inteligencia Artificail
#
# Proyecto 1 (Sudoku)
# Jose Martinez 15163


def clear():
    for i in range(40):
        print('')


def print_sudoku(sudoku_matrix):
    i_row = 0
    for r in sudoku_matrix:
        if i_row % 2 == 0:
            print("++----------------------------------------++")
        else:
            print("||---------|---------||---------|---------||")

        row_string = ''
        i_col = 0
        for c in r:
            cStr = " "
            if c != ".":
                cStr = c

            if i_col % 2 == 0:
                row_string = row_string + "||    " + cStr + "    "
            else:
                row_string = row_string + "|    " + cStr + "    "
            i_col += 1
        row_string = row_string + "||"
        print(row_string)
        i_row += 1

    print("++----------------------------------------++")

