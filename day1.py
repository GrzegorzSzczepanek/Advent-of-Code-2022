arr = list(map(lambda x: x.split("\n"), open("day1File", "r").read().split("\n\n")))
def calories(array):
    res = []
    for i in array:
        res.append(sum(list(map(lambda x: int(x), i))))
    res.sort(reverse=True)

    return (res[0], res[0] + res[1] + res[2])

print(calories(arr))
