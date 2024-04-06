class dictionary_iter:
    def __init__(self, my_dict):
        self.my_dict = my_dict
        self.my_dict_keys = list(my_dict.keys())[::-1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.my_dict_keys:
            key = self.my_dict_keys.pop()
            value = self.my_dict.pop(key)
            return key, value
        else:
            raise StopIteration

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
