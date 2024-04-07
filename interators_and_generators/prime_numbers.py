
def get_primes(numbers: list):
    def is_prime(num):
        flag = False
        if num > 1:
            # check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    # if factor is found, set flag to True
                    flag = True
                    # break out of loop
                    break

            # check if flag is True
            if flag:
                return False
            else:
                return True
    index = 0
    while index < len(numbers):
        if is_prime(numbers[index]):
            yield numbers[index]
        index += 1

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
