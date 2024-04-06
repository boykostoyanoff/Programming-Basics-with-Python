class Vowels:
    VOWELS = ['A', 'E', 'I', 'O', 'U']

    def __init__(self, text: str):
        self.text = text

    def __iter__(self):
        return self

    def __next__(self):
        if self.text:
            for i in range(len(self.text)):
                char = self.text[i]
                if char.upper() in Vowels.VOWELS:
                    self.text = self.text[i + 1:]
                    return char
        else:
            raise StopIteration()


my_string = Vowels('Abcedifuty0o')
for char in my_string:
    print(char)
