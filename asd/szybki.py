from collections import deque


def minimal_button_presses(n):
    visited = set()
    queue = deque()
    queue.append((n, 0))

    while queue:
        current, presses = queue.popleft()

        if current == 1:
            return presses

        if current in visited:
            continue
        visited.add(current)

        if current > 1:
            # Rozważamy rotację cyfr
            current_str = str(current)
            if len(current_str) > 1:
                rotated = int(current_str[1:] + current_str[0])
                if rotated not in visited:
                    queue.append((rotated, presses + 1))
        else:
            # Dla current <= 1, dodajemy 1
            next_num = current + 1
            if next_num not in visited:
                queue.append((next_num, presses + 1))

    return -1  # Nie można osiągnąć liczby 1


n = int(input().strip())
print(minimal_button_presses(n))
