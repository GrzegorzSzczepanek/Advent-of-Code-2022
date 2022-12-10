array = list(map(lambda x: list(map(lambda y: list(map(lambda z: int(z) ,y.split("-"))), x.split(","))), open("day4Input", "r").read().split("\n")))


def part1(arr):
    contain = 0

    for index in arr:
        # current = index

        if index[1][0] > index[0][0] or index[1][1] < index[0][1]:
            index.reverse()

        check = [index[1][0], index[1][1],
                 index[0][0], index[0][1]]
        mini = min(check)
        maxi = max(check)

        # print(index)
        if index[1][0] == mini and index[1][1] == maxi:
            contain += 1

    return contain


def part2(arr):
    contain = 0
    for index in arr:
        check = [index[1][0], index[1][1],
                 index[0][0], index[0][1]]

        arr1 = []
        arr2 = []

        # if index[1][0] > index[0][0] or index[1][1] < index[0][1]:
        #     contain += 1
        #
        if index[1][0] < index[0][0]:
            index.reverse()
        if index[1][0] >= index[0][0] and index[1][0] <= index[0][1]:
            contain += 1

    return contain
