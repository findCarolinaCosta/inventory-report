from collections import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterable_data):
        self.data = iterable_data
        self.index = 0

    def __next__(self):
        try:
            current_data = self.data[self.index]

            self.index += 1
            return current_data

        except IndexError:
            raise StopIteration
