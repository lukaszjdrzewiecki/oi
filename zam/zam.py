import math
import time
import sys

sys.set_int_max_str_digits(10_000_000)


def minimal_button_presses_new(n):
    # IF N IS 1
    if n == "1":
        return 0

    # GET DIGITS
    digits = len(n)

    # IF 2 <= N <= 9
    if digits == 1:
        return (10 - int(n)) + 1

    nearest_10 = 10 ** digits

    n_int = int(n)

    iterations = 0

    while True:
        if (val := nearest_10 - n_int) <= 9:
            return iterations + val + 1

        if n_int == 1:
            return iterations

        if n[0] > n[-1]:
            n = n[1:] + n[0]
            n_int = int(n)
            iterations += 1
            continue

        n_int += 1
        n = str(n_int)
        iterations += 1


def minimal_button_presses(n):
    # IF N IS 1
    if n == "1":
        return 0

    # GET DIGITS
    digits = len(n)

    # IF 2 <= N <= 9
    if digits == 1:
        return (10 - int(n)) + 1

    nearest_10 = 10 ** digits

    numbers = [n]

    iterations = 0

    while True:
        numbers_tmp = []
        for number in numbers:
            n_int = int(number)
            if (val := nearest_10 - n_int) <= 9:
                return iterations + val + 1

            if n_int == 1:
                return iterations

            numbers_tmp.extend([
                str(n_int + 1), number[1:] + number[0]
            ])

        numbers = numbers_tmp
        iterations += 1


if __name__ == "__main__":
    n = input().strip()

    # start = time.time()
    # print(minimal_button_presses_new(n))
    print(minimal_button_presses_new(n))
    # print(time.time()-start)
