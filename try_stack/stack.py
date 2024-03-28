class Stack:
    data = []
    def push(self, element):
        Stack.data.append(element)

    def pop(self):
        last_element = Stack.data[-1]
        Stack.data = Stack.data[:-1]
        return last_element

    def top(self):
        return max(Stack.data)

    def is_empty(self):
        return False if Stack.data else True

    def __str__(self):
        data_sorted = list(sorted(Stack.data, reverse=True))
        result = '[' + ', '.join(data_sorted) + ']'
        return result