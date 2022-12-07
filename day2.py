array = open("day2Input", "r").read().split("\n")

wins = {
    "X": "C",
    "Y": "A",
    "Z": "B"
}
draws = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}


def part2(arr):
    points = 0


    for index in arr:
        if index[1] == "Y" and index[0] == "A":
            points += 4
        elif index[1] == "Y" and index[0] == "B":
            points += 5
        elif index[1] == "Y" and index[0] == "C":
            points += 6

        if index[1] == "X" and index[0] == "A":
            points += 3
        elif index[1] == "X" and index[0] == "B":
            points += 1
        elif index[1] == "X" and index[0] == "C":
            points += 2

        if index[1] == "Z" and index[0] == "A":
            points += 8
        elif index[1] == "Z" and index[0] == "B":
            points += 9
        elif index[1] == "Z" and index[0] == "C":
            points += 7
    return points


def part1(arr):
    points = 0
    for i in range(0, len(arr)):
        arr[i] = arr[i].split(" ")

    for i in arr:

        myPick = i[1]
        rival = i[0]
        if wins[myPick] == rival:
            points += 6
        elif draws[i[1]] == rival:
            points += 3
        else:
            points += 0

        if myPick == "X":
            points += 1
        elif myPick == "Y":
            points += 2
        elif myPick == "Z":
            points += 3

    return points


print(part1(array))
print(part2(array))
