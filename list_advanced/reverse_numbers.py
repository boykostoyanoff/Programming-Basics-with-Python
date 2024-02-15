from collections import deque
numbers_string = input().split()

numbers_int = deque(int(n) for n in numbers_string)
while numbers_int:
    print(numbers_int.pop(), end="")
    if not numbers_int:
        break
    print(end=" ")
