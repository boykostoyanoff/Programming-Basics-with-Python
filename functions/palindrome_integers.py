numbers = input().split(', ')


def is_palindrome(n):
    if n[:] == n[::-1]:
        return True
    return False


for num in numbers:
    print(is_palindrome(num))