# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def can_eliminate_all(n, robots):
    # Znajdujemy robota z najmniejszą siłą
    min_strength_robot = min(robots, key=lambda x: x[0])
    # Sprawdzamy, czy ma on najwyższą zwinność
    max_agility = max(robot[1] for robot in robots)

    if min_strength_robot[1] == max_agility:
        return "TAK"
    else:
        return "NIE"


n = int(input().strip())
robots = [tuple(map(int, input().split())) for _ in range(n)]

# Wyświetlenie wyniku
print(can_eliminate_all(n, robots))

