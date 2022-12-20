file = open("day7Input", "r").read().split("\n")


def part1(arr):
    commands = []
    files = []
    dirs = []

    for i in range(2, len(arr)):
        ite = 0
        if arr[i][0:3] == "dir":
            dirs.append([arr[i]])
        if arr[i][0:4] == "$ cd":
            for j in dirs:
                if j[ite][-1] == arr[i][-1]:
                    dirs[ite].append([])




    return dirs


print(part1(file))
