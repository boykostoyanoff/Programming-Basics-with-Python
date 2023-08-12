numbers = [int(x) for x in input().split(', ')]
tenths = 0
max_el = max(numbers)

while tenths < max_el:
    tenths_list = list()
    for x in numbers:
        if tenths < x <= tenths + 10:
            tenths_list.append(x)

    print(f"Group of {tenths + 10}'s: {tenths_list}")

    tenths += 10
