class FlatIterator:
    def __init__(self, incoming_list):
        flatten_list = lambda incoming_list: [
            item for element in incoming_list for item in flatten_list(element)
        ] if type(incoming_list) is list else [incoming_list]
        self.list = flatten_list(incoming_list)
        # self.list = sum(incoming_list, [])
        # self.list = [el for sublist in incoming_list for el in sublist]
        # for el in sublist in incoming_list:
        #     for el in sublist:
        #         self.list.append(el)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.list):
            element = self.list[self.index]
            self.index += 1
            return element
        else:
            raise StopIteration

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None], [[123], 'name'],
]

for list in FlatIterator(nested_list):
    print(list)