import sys

sys.set_int_max_str_digits(1_000_000_000)


def minimal_button_presses(n):
    queue = [(n, 0)]
    visited_set = {n}
    index = 0
    while index < len(queue):
        current, presses = queue[index]
        index += 1

        if current == 1:
            return presses

        next_num = current + 1
        if next_num not in visited_set:
            visited_set.add(next_num)
            queue.append((next_num, presses + 1))

        current_str = str(current)
        if len(current_str) > 1:
            rotated_num = int(current_str[1:] + current_str[0])
            if rotated_num not in visited_set:
                visited_set.add(rotated_num)
                queue.append((rotated_num, presses + 1))


n = int(input().strip())
print(minimal_button_presses(n))
