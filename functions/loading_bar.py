def loading_bar(num: int):
    n = num // 10
    result = f"[{'%' * n}{'.' * (10 - n)}]"

    return result


number = int(input())
if number == 100:
    print('100% Complete!')
    print(loading_bar(number))
else:
    print(f"{number}% {loading_bar(number)}")
    print('Still loading...')
