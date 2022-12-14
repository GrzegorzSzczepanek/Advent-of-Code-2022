ABC = "".join("abcdefghijklmnopqrstuvwxyz".upper())
file = open("day5Input", "r").read().split("\n\n")

def part1(file):

    partLen = list(map(lambda x: x.replace(" ", ""), file[0].split("\n")))
    partLen = list(map(lambda x: x.replace("[", ""), partLen))
    partLen = list(map(lambda x: x.replace("]", ""), partLen))

    part1 = file[0].split("\n")
    part2 = file[1]

    arr = []

    maxLen = max(len(x) for x in partLen)

    for i in range(maxLen):
        arr.append([])


    strToInput = list(map(lambda x: x.replace("    ", "[-]").replace(" ", ""), part1))

    for i in range(0, maxLen):
        while len(strToInput[i]) != 27:
            strToInput[i] += "[-]"

    strToInput = list(map(lambda x: x.replace("[", ""), strToInput))
    strToInput = list(map(lambda x: x.replace("]", ""), strToInput))

    for i in strToInput:
        for el in range(0, maxLen):
            if i[el] not in "0123456789":
                arr[el].append(i[el])

    arr = list(map(lambda y: list(filter(lambda x: x != "-", y)), arr))
    part2 = part2.split("\n")

    for i in part2:
        part2[part2.index(i)] = list(map(lambda y: int(y), list(filter(lambda x: x.isdigit(), i.split(" ")))))

    #print(part2)
    arr = list(map(lambda x: "".join(x), arr))
    arr2 = list(map(lambda x: "".join(x), arr))

    for i in part2:
        try:
            el = arr[i[1] - 1][:i[0]]
            arr[i[2]-1] = el[::-1] + arr[i[2]-1]
            arr[i[1]-1] = arr[i[1] - 1][i[0]:]

            el = arr2[i[1] - 1][:i[0]]
            arr2[i[2] - 1] = el + arr2[i[2] - 1]
            arr2[i[1] - 1] = arr2[i[1] - 1][i[0]:]

        except IndexError:
            return [part2.index(i), i]

    res = ""
    res2 = ""
    for i in arr:
        res += i[0]

    for i in arr2:
        res2 += i[0]

    return [res, res2, arr]

print(part1(file))
