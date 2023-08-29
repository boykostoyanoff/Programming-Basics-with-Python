resource_dict = dict()

while True:
    res = input()
    if res == 'stop':
        break
    if res not in resource_dict.keys():
        resource_dict[res] = 0
    resource_dict[res] += int(input())

for res in resource_dict.keys():
    print(f'{res} -> {resource_dict[res]}')