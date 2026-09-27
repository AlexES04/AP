def order_crossover(parent1, parent2, lower_bound, upper_bound):
    n = len(parent1)
    child = [-1]*n

    child[lower_bound:upper_bound] = parent1[lower_bound:upper_bound]

    child_index = upper_bound
    current_index = upper_bound
    for i in range(n):
        if parent2[current_index] not in child:
            child[child_index] = parent2[current_index]
            child_index = (child_index + 1) % n
        current_index = (current_index+1) % n
    return child