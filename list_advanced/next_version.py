version = input()
version_list = [int(v) for v in version.split('.')]

for i in range(-1, -len(version_list), -1):
    if i == -1:
        version_list[i] += 1

    increase = version_list[i] // 10
    version_list[i] = version_list[i] % 10
    version_list[i - 1] += increase

version_list = [str(x) for x in version_list]

print('.'.join(version_list))

