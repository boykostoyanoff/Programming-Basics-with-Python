text = input()

try:
    repeat_times = int(input())
    print(text * repeat_times)
except ValueError:
    pass
finally:
    print("Variable times must be an integer")
