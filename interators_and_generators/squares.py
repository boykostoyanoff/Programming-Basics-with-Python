def squares(n: int):
    for num in range(1, n+ 1):
        yield num * num


print(list(squares(5)))