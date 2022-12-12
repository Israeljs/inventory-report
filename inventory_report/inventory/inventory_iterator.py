from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def get_data(self, index):
        return self.data[index]

    def __next__(self):
        info = self.get_data(self.index)

        if not info:
            raise StopIteration()

        self.index += 1
        return info