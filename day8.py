myFile = open("day8Input", "r").read().split("\n")


def part1(file):
    columns = []
    rows = []

    for i in file:
        columns.append([])

    for i in file:
        rows.append(i)

    for i in rows:
        for j in range(0, len(i)):
            columns[j].append(i[j])

    # these for loops are meant to create two arrays with columns and rows of the input

    visible = (len(columns) * 2) + (len(columns) * 2) - 4
    # base number of visible trees

    indexes = []  # indexes of trees in rows
    for i in range(1, len(rows) - 1):
        for j in range(1, len(columns) - 1):
            x = j - 1
            y = j + 1

            while x >= 0 and int(rows[i][j]) > int(rows[i][x]):
                if x == 0:
                    indexes.append(str(i) + "," + str(j))
                x -= 1
            try:
                while y < len(rows) and \
                        int(rows[i][j]) > int(rows[i][y]):
                    if y == len(rows) - 1:
                        indexes.append(str(i) + "," + str(j))
                    y += 1
            except IndexError:
                return y
            # These while loops are used to check whether tree is matching the conditions from left and right
    #####################################################
    for i in range(1, len(columns) - 1):
        for j in range(1, len(columns) - 1):
            x = j-1
            y = j+1

            while x >= 0 and int(columns[i][j]) > int(columns[i][x]):
                if x == 0:
                    indexes.append(str(j) + "," + str(i))
                x -= 1
            try:
                while y < len(columns) and \
                        int(columns[i][j]) > int(columns[i][y]):
                    if y == len(columns) - 1:
                        indexes.append(str(j) + "," + str(i))
                    y += 1
            except IndexError:
                return y
            # These while loops are used to check whether tree is matching the conditions from top and bottom.
    return len(list(set(indexes))) + visible

def part2(file):

    return 1

print(part1(myFile))
