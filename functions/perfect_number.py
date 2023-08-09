number = int(input())


def is_perfect(n: int):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
        if sum > n:
            break
    if sum == n:
        return True
    return False


if is_perfect(number):
    print(f'We have a perfect number!')
else:
    print(f"It's not so perfect.")
