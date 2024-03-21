import math


def math_operations(*args, **kwargs):
    result = ''
    for index in range(len(args)):
        mod = index % 4
        if mod == 1:
            kwargs['s'] -= args[index]
        elif mod == 2:
            if not args[index] == 0:
                kwargs['d'] /= args[index]
        elif mod == 3:
            kwargs['m'] *= args[index]
        else:
            kwargs['a'] += args[index]

    for k, v in kwargs.items():
        kwargs[k] = round(v, 1)

    for k, v in dict(sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))).items():
        result += f"{k}: {v:.1f}\n"

    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
