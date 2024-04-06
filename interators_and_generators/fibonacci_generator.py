def fibonacci():
    first = 0
    yield first
    second = 1
    yield second
    while True:
        next_number = first + second
        first = second
        second = next_number
        yield next_number



generator = fibonacci()
for i in range(8):
    print(next(generator))
