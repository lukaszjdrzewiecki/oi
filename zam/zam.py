from collections import deque
import sys

sys.set_int_max_str_digits(1_000_000_000)


def rotate(number):
    """
    Funkcja obraca liczbę cyklicznie. Przenosi najbardziej znaczącą cyfrę
    na koniec i usuwa zera wiodące w wynikowej liczbie.
    """
    number_str = str(number)
    rotated_number = int(number_str[1:] + number_str[0])
    return rotated_number


def minimum_presses_to_one(n):
    """
    Funkcja oblicza minimalną liczbę naciśnięć przycisków, aby uzyskać liczbę 1.
    """
    if n == 1:
        return 0  # Jeśli początkowa liczba to 1, nie musimy wykonywać żadnych operacji

    queue = deque([(n, 0)])  # Kolejka z parą (liczba, liczba kroków)
    visited = set([n])  # Zbiór odwiedzonych stanów, aby uniknąć zapętlenia

    while queue:
        current_number, steps = queue.popleft()

        # Operacja: Dodaj 1 do liczby
        incremented_number = current_number + 1
        if incremented_number == 1:
            return steps + 1
        if incremented_number not in visited:
            visited.add(incremented_number)
            queue.append((incremented_number, steps + 1))

        # Operacja: Cyfrowy obrót liczby
        rotated_number = rotate(current_number)
        if rotated_number == 1:
            return steps + 1
        if rotated_number not in visited:
            visited.add(rotated_number)
            queue.append((rotated_number, steps + 1))

    return -1  # W przypadku gdyby liczba 1 nie była osiągalna, choć teoretycznie jest


if __name__ == "__main__":
    n = int(input().strip())
    print(minimum_presses_to_one(n))

    # start = time.time()
    # print(minimal_button_presses_new(n))
    # print(minimal_button_presses(n))
    # print(time.time()-start)
