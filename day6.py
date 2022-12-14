file = open("day6Input", "r").read()


def part1(str):
    i = 3
    for i in range(3, len(str)):

        if str[i] not in [str[i-1], str[i-2], str[i-3]]\
                and str[i-1] not in [str[i], str[i-2], str[i-3]]\
                and str[i-2] not in [str[i], str[i-1], str[i-3]]\
                and str[i-3] not in [str[i], str[i-2], str[i-1]]:

            return i + 1


def part2(str):
    for i in range(13, len(str)):
        arr = []
        for x in range(i-13, i+1):
            arr.append(str[x])

        if len(arr) == len(set(arr)):
            return i + 1


print(part2(file))
