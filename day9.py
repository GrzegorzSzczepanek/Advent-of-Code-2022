file = open("day9Input", "r").read().split("\n")

#print(file)

board = []
for i in range(0, 100):
    board.append(list("."*100))

#print(len(board))

def part1(input):
    count = -1
    x = 99
    y = 0
    # initial position
    for i in input:
        if i[0] == "R":
            for j in range(0, int(i[2])):
                board[x][y] = "#"
                y += 1
        elif i[0] == "L":
            for j in range(0, int(i[2])):
                board[x][y] = "#"
                y += 1
                
        return y


print(part1(file))
