start_char = input()
end_char = input()


def chars_between_two_chars(start, end):
    result = ''
    for ch in range(ord(start) + 1, ord(end)):
        result += f'{chr(ch)} '
    return result


print(chars_between_two_chars(start_char, end_char))