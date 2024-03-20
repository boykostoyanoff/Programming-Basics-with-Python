def age_assignment(*names, **ages):
    names = list(names)
    names.sort(reverse=False)
    result = ''
    for name in names:
        result += f"{name} is {ages[name[0]]} years old.\n"
    return result


print(age_assignment("Peter", "George", G=26, P=19))