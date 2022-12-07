###########################################part 1
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


def sum_points(arr):
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


print(sum_points(array))
