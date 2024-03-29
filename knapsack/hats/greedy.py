import pandas as pd


def high_density_first(item_count, capacity, items):
    """ """

    value = 0
    weight = 0

    input_df = pd.DataFrame(items).set_index("index")

    print(item_count)

    input_df["taken"] = 0

    input_df["value_by_weight"] = input_df["value"] / input_df["weight"]
    input_df = input_df.sort_values(by="value_by_weight", ascending=False)

    for idx, r in input_df.iterrows():
        if weight + r.weight <= capacity:
            input_df.loc[idx, "taken"] = 1
            weight += r.weight
            value += r.value

    input_df.sort_index(inplace=True)
    taken = input_df["taken"].astype(int).to_list()

    return int(value), int(weight), taken


def high_value_first(item_count, capacity, items):
    """ """

    value = 0
    weight = 0

    print(item_count)
    input_df = pd.DataFrame(items).set_index("index")

    input_df["taken"] = 0

    input_df = input_df.sort_values(by="value", ascending=False)

    for idx, r in input_df.iterrows():
        if weight + r.weight <= capacity:
            input_df.loc[idx, "taken"] = 1
            weight += r.weight
            value += r.value

    input_df.sort_index(inplace=True)
    taken = input_df["taken"].astype(int).to_list()

    return int(value), int(weight), taken


def low_weight_first(item_count, capacity, items):
    """ """

    value = 0
    weight = 0

    input_df = pd.DataFrame(items).set_index("index")

    input_df["taken"] = 0

    input_df = input_df.sort_values(by="weight")

    for idx, r in input_df.iterrows():
        if weight + r.weight <= capacity:
            input_df.loc[idx, "taken"] = 1
            weight += r.weight
            value += r.value

    input_df.sort_index(inplace=True)
    taken = input_df["taken"].astype(int).to_list()

    return int(value), int(weight), taken
