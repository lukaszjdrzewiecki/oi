def openInput():
    roboty = []

    n = int(input())

    for _ in range(n):
        sila, zwinnosc = map(int, input().split())

        roboty.append(
            [sila, zwinnosc]
        )

    return roboty


def walka(robot1, robot2, robot1idx, robot2idx):
    # SILA                      ZWINNOSC
    if (robot1[0] < robot2[0]) and (robot1[1] < robot2[1]):
        return robot1idx

    if (robot1[0] > robot2[0]) and (robot1[1] > robot2[1]):
        return robot2idx

    return -1


if __name__ == "__main__":
    roboty = openInput()

    roboty = sorted(roboty, key=lambda x: x[1], reverse=True)

    ilosc_robotow = len(roboty)

    while True:
        if ilosc_robotow == 0:
            print("TAK")
            break

        if ilosc_robotow == 1:
            print("NIE")
            break

        indeksy = []

        for i in range(ilosc_robotow // 2):
            pierwszy = i
            ostatni = ilosc_robotow - i - 1

            werdykt = walka(
                roboty[pierwszy],
                roboty[ostatni],
                pierwszy,
                ostatni
            )

            if werdykt == -1:
                indeksy.append(ostatni)
                indeksy.append(pierwszy)

            else:
                indeksy.append(werdykt)

            break

        for i in sorted(indeksy, reverse=True):
            roboty.pop(i)

        ilosc_robotow = len(roboty)
