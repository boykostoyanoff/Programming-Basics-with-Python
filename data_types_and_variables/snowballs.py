snowballs = int(input())
message = ''
h_value = 0

for i in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if h_value < value:
        h_value = value
        message = f'{weight} : {time} = {int(value)} ({quality})'

print(message)