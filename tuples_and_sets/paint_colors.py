import math

data = input().split(' ')
colors = {"red": "red",
          "yellow": "yellow",
          "blue": "blue",
          "orange": "orange",
          "purple": "purple",
          "green": "green"}
result = list()

while data:
    if len(data) == 1:
        word = data.pop()
        if word in colors.values():
            result.append(word)
        else:
            if len(word) > 2:
                data.append(word[:-1])
    else:
        left = data[0]
        right = data[-1]
        if (left + right) in colors.values():
            result.append(left + right)
            data.pop()
            data.pop(0)
        elif (right + left) in colors.values():
            result. append(right + left)
            data.pop()
            data.pop(0)
        else:
            left = left[:-1]
            right = right[:-1]
            middle = math.ceil(len(data) / 2)
            if right:
                data.insert(middle, right)
            if left:
                data.insert(middle, left)
            data.pop()
            data.pop(0)
if "red" not in result or "yellow" not in result:
    while "orange" in result:
        result.remove("orange")
if "red" not in result or "blue" not in result:
    while "purple" in result:
        result.remove("purple")
if "yellow" not in result or "blue" not in result:
    while "green" in result:
        result.remove("green")
print(result)

