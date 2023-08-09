words = input().split(' ')
palindrome = input()


def is_palindrome(word: str):
    if word[:] == word[::-1]:
        return True
    return False


palindrome_list = [w for w in words if is_palindrome(w)]
count_palindrome = palindrome_list.count(palindrome)

print(palindrome_list)
print(f'Found palindrome {count_palindrome} times')