

def a_star(initial_state, initial_numbers_tired, path_cost_function, heucaristic_function, end_condition_function, possible_nodes_function, change_state_function):
    path = [initial_state]
    numbers_tried = initial_numbers_tired

    while end_condition_function(path[-1]):
        last_state = path[-1]

        all_f_n = []
        possible_nodes = possible_nodes_function(last_state)

        for node in possible_nodes:
            g_n = path_cost_function(last_state, node, numbers_tried, path)
            h_n = heucaristic_function(last_state, node)

            f_n = g_n + h_n
            all_f_n.append(f_n)

        selected_f_n = all_f_n[0]
        selected_node = possible_nodes[0]


        for i in range(1, len(possible_nodes)):
            if all_f_n[i] < selected_f_n:
                selected_node = possible_nodes[i]
                selected_f_n = all_f_n[i]
        change_state_function(path, numbers_tried, selected_node)