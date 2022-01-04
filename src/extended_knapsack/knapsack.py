import numpy as np

# dynamic programming solution, adapted from
# https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem
# with a third dimension in the table for the number of items used


def solve(items: list, capacity: int, max_items: int) -> tuple:
    assert capacity >= 0
    assert max_items >= 0
    n = len(items)

    if max_items > n:
        max_items = n
    table = np.empty((n+1, capacity+1, max_items+1), dtype=object)
    table.fill((0, []))
    for i in range(1, n+1):
        item = items[i-1]
        value_i = item['value']
        weight_i = item['weight']
        for w in range(0, capacity+1):
            for count in range(1, max_items+1):
                if weight_i > w:
                    table[i, w, count] = table[i-1, w, count]
                else:
                    old_value, old_list = table[i-1, w-weight_i, count-1]
                    new_value = old_value + value_i
                    if new_value > table[i-1, w, count][0]:
                        new_list = old_list[:]
                        new_list.append(i)
                        table[i, w, count] = (new_value, new_list)
                    else:
                        table[i, w, count] = table[i-1, w, count]

    optimal_value, items_used = table[n, capacity, max_items]
    return optimal_value, [items[i-1] for i in items_used]
