# Universidad del Valle de Guatemala
# Inteligencia Artificial
#
# Proyecto 1 (Fifteen)
# Jose Martinez 15163

import Fifteen.fifteen as f
import a_star

print('Bienvenido al solucionador de Fifteen Game\n\n')
#F21C856B49A73ED
fifteenString = "574B19A8C6F.D3E2"
numbers_tried_initial = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0}

if len(fifteenString) == 16:
    fifteen_matrix = f.get_fifteen_matrix(fifteenString)

    a_star.a_star(fifteen_matrix, numbers_tried_initial, f.movements_to_final, f.distance_of_block_to_final, f.end_condition, f.find_possible_blocks_to_move, f.change_path_fifteen)
