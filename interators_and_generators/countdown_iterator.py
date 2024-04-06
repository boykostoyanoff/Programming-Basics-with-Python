class countdown_iterator:
    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 0:
            value = self.count
            self.count -= 1
            return value
        else:
            raise StopIteration