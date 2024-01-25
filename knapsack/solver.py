#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from hats.greedy import high_density_first, high_value_first, low_weight_first

Item = namedtuple("Item", ["index", "value", "weight"])


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split("\n")

    firstLine = lines[0].split()

    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full

    if item_count <= 30:
        value, weight, taken = low_weight_first(item_count, capacity, items)
    else:
        value, weight, taken = high_density_first(item_count, capacity, items)

    # prepare the solution in the specified output format
    output_data = str(value) + " " + str(0) + "\n"
    output_data += " ".join(map(str, taken))
    return output_data


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print(
            "This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)"
        )
