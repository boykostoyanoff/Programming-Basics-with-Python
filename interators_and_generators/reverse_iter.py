class ReverseIter:
    def __init__(self, iter_object):
        self.iter_object = iter_object

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_object:
            last_el = self.iter_object.pop()
            return last_el
        else:
            raise StopIteration()

reversed_list = ReverseIter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
