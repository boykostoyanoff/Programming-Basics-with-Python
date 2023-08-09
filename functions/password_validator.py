def is_password_length_valid(word):
    if 6 <= len(word) <= 10:
        return True
    return False


def is_consist_only_letters_and_digits(word: str):
    for ch in word:
        if not ch.isdigit() and not ch.isalpha():
            return False

    return True


def is_have_at_least_two_digits(word: str):
    digits_count = 0
    for ch in word:
        if ch.isdigit():
            digits_count += 1
            if digits_count == 2:
                return True
    return False


def is_valid_password(word):
    is_valid = True
    if not is_password_length_valid(word):
        print(f'Password must be between 6 and 10 characters')
        is_valid = False
    if not is_consist_only_letters_and_digits(word):
        print(f'Password must consist only of letters and digits')
        is_valid = False
    if not is_have_at_least_two_digits(word):
        print(f"Password must have at least 2 digits")
        is_valid = False
    return is_valid


password = input()
if is_valid_password(password):
    print(f'Password is valid')