array = open("day3Input", "r").read().split("\n")

abc = "".join("abcdefghijklmnopqrstuvwxyz")
ABC = "".join("abcdefghijklmnopqrstuvwxyz".upper())


def get_char(x,y):
    for char in x:
        for char2 in y:
            if char == char2:
                return char2


def get_char2(x, y, z):
    for char in x:
        for char2 in y:
            for char3 in z:
                if char == char2 == char3:
                    return char3

def part1(arr):
    array2 = []
    for index in arr:
        x = index[0:int(len(index)/2)]
        y = index[int(len(index)/2): len(index)]
        array2.append(get_char(x,y))

    sum = 0
    for index in array2:
        if index.upper() == index:
            sum += 26 + ABC.index(index) + 1
        elif index.lower() == index:
            sum += abc.index(index) + 1

    return sum


def part2(arr):
    type = []
    sum = 0
    x = 0
    for i in range(0, int(len(arr) / 3)):
        type.append(get_char2(arr[x], arr[x + 1], arr[x + 2]))
        x += 3

    for index in type:
        if index.upper() == index:
            sum += 26 + ABC.index(index) + 1
        elif index.lower() == index:
            sum += abc.index(index) + 1
    return sum



#print(part2(array))
#print(part1(array))
#print(len(array))
#print(len(list(filter(lambda x: len(x) % 2 = 0, array))))



