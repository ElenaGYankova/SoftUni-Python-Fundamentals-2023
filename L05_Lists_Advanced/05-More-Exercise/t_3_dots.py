size = int(input())
maze = []
for _ in range(size):
    row = input()
    row = [x for x in row]
    maze.append(row)
kate_position = []
for row in range(len(maze)):
    for column in range(len(maze[row])):
        if maze[row][column] == "k":
            kate_position = [row, column]
row = kate_position[0]
column = kate_position[1]
escape_fond = False
while True:
    if row - 1 < 0 or column - 1 < 0 or row + 1 > len(maze) - 1 or column + 1 > len(maze[0]) - 1:
        escape_fond = True
        break
    if maze[row - 1][column] != " " and maze[row][column - 1] != " " and \
            maze[row + 1][column] != " " and maze[row][column + 1] != " ":
        print("Kate cannot get out")
        break
    if maze[row - 1][column] == " ":
        maze[row - 1][column] = "k"
        row -= 1
    elif maze[row][column - 1] == " ":
        maze[row][column - 1] = "k"
        column -= 1
    elif maze[row + 1][column] == " ":
        maze[row + 1][column] = "k"
        row += 1
    elif maze[row][column + 1] == " ":
        maze[row][column + 1] = "k"
        column += 1
if escape_fond:
    count_moves = 0
    for x in maze:
        count_moves += x.count("k")
        count_moves += x.count(" ")
    print(f'Kate got out in {count_moves} moves')
