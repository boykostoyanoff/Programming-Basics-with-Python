def add_subtract(f_num, s_num, t_num):
    def sum_numbers(a, b):
        return a + b

    def subtract(c, d):
        return c - d

    return subtract(sum_numbers(f_num, s_num), t_num)


i = int(input())
j = int(input())
k = int(input())

print(add_subtract(i, j, k))
