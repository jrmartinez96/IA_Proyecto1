# Universidad del Valle de Guatemala
# Inteligencia Artificial
#
# Proyecto 1 (Sudoku)
# Jose Martinez 15163

from Sudoku import sudoku
import a_star

print('Bienvenido al solucionador de SUDOKU 4x4\n\n')

sudokuString = ".4.13.4.1..4.21."

if len(sudokuString) == 16:
    sudoku_matrix = sudoku.get_sudoku_matrix(sudokuString)
    a_star.a_star(sudoku_matrix, [[]], sudoku.find_n_free_spaces_in_box, sudoku.find_n_free_spaces_in_space, sudoku.end_condition, sudoku.find_white_spaces, sudoku.change_value_path)



