import numpy as np


def dp(item_count, capacity, items):
    weight = 0
    taken = [0] * item_count

    # Create Matrix
    mat = np.zeros((capacity + 1, item_count + 1))
    print(mat.shape)
    for i in range(1, item_count + 1):
        for j in range(1, capacity + 1):
            curr_v = items[i - 1].value
            curr_w = items[i - 1].weight

            prev_bundle_weight = max(0, j - curr_w)

            if j - items[i - 1].weight >= 0:
                prev_bundle_value = mat[j - items[i - 1].weight, i - 1]
            else:
                prev_bundle_value = 0

            if j >= prev_bundle_weight + curr_w:
                # item fits in the knapsack
                old_value = mat[j, i - 1]
                new_value = prev_bundle_value + curr_v

                mat[j, i] = max(old_value, new_value)
            else:
                # item doesn't fit
                mat[j, i] = mat[j, i - 1]

    # Trace the matrix
    i, j = capacity, item_count
    value = mat[i, j]

    while j != 0:
        if mat[i, j] == mat[i, j - 1]:
            taken[j - 1] == 0
        else:
            taken[j - 1] = 1
            weight += items[j - 1].weight
            i -= items[j - 1].weight

        j -= 1

    return int(value), int(weight), taken
