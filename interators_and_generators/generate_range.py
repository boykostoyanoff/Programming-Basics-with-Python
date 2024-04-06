def genrange(start: int, end: int):
    num = start
    while num <= end:
        num += 1
        yield num - 1


print(list(genrange(1, 10)))
