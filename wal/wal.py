# This is a sample Python script.

n = int(input())
robots = []
for i in range(n):
    s, z = map(int, input().split())
    robots.append((s, z, i))

# Znajdź robota z maksymalną siłą
max_s_robot = max(robots, key=lambda x: x[0])
# Znajdź robota z maksymalną zwinnością
max_z_robot = max(robots, key=lambda x: x[1])

# Sprawdź, czy to ten sam robot
if max_s_robot[2] == max_z_robot[2]:
    print("NIE")
else:
    print("TAK")

