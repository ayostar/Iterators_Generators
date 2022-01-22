# Написать итератор, который принимает список списков, и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов. Например

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None], [[123]],
]

class FlatIterator:
    def __init__(self, incoming_list):
        self.list = [el for sublist in incoming_list for el in sublist]
        # for el in sublist in incoming_list:
        #     for el in sublist:
        #         self.list.append(el)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.list):
            list_element = self.list[self.index]
            self.index += 1
            return list_element
        else:
            raise StopIteration


for list in FlatIterator(nested_list):
    print(list)