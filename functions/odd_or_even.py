def get_odds(numbers: list):
    if not numbers:
        return 0
    return [n for n in numbers if n % 2 == 1]


def get_evens(numbers: list):
    if not numbers:
        return 0
    return [n for n in numbers if n % 2 == 0]


def even_odd(*args):
    my_funcs = {'odd': get_odds,
                'even': get_evens}

    args = list(args)
    command = args.pop()
    return my_funcs[command](args)


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
