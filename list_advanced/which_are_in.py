first_string = input().split(', ')
second_string = input().split(', ')
result = list()


def is_sub_string(f_string: str, s_string: str):
    for i in range(0, len(s_string) - len(f_string) + 1):
        part = s_string[i:i + len(f_string)]
        if f_string == part:
            return True
    return False


for f_el in first_string:
    is_el_in = False
    for s_el in second_string:
        if is_sub_string(f_el, s_el):
            if f_el not in result:
                result.append(f_el)

print(result)