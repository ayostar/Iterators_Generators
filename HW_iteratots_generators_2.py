def flat_generator(incoming_list):
    flatten_list = lambda incoming_list: [
        item for element in incoming_list for item in flatten_list(element)
    ] if type(incoming_list) is list else [incoming_list]
    flattenned_list = flatten_list(incoming_list)

    return [element for element in flattenned_list]

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
    [[123], 'name'],
]


for item in flat_generator(nested_list):
    print(item)

