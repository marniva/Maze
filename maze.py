mazeStr = '*****\n*o*x*\n*   *\n*****\n'

maze = []
line = []

for i in mazeStr:
    if i != '\n':
        line.append(i)
        if i == 'x':
            exitPos = (len(line) - 1, len(maze))
        if i == 'o':
            playerPos = (len(line) - 1, len(maze))
    else:
        maze.append(line)
        line = []

# maze = mazeStr.split('\n')
# print(maze[0][0])

def printMaze(maze : list):
    for line in maze:
        for char in line:
            print(char, end='')
        print('\n', end='')

def gotoFreeDirection() -> bool:
    global playerDir
    global playerPos
    global directions
    global traversed
    global maze

    newPos = (playerPos[0] + directions[playerDir][0], playerPos[1] + directions[playerDir][1])
    if maze[newPos[1]][newPos[0]] == '*':
        playerDir -= 1
        if playerDir < 0:
            playerDir = 3
        gotoFreeDirection()
        return False
    else:
        if playerPos not in traversed:
            traversed.append(playerPos)
        playerPos = newPos
        return True

printMaze(maze)

directions = {0:(0,-1), 1:(1,0), 2:(0,1), 3:(-1,0)}
directionTags = {0:'north', 1:'east', 2:'south', 3:'west'}
playerDir = 1
traversed = []

print(f'Current position: {playerPos}')
while len(traversed) < len(maze) or playerPos != exitPos:
    playerDir += 1
    playerDir = playerDir % 4
    gotoFreeDirection()
    print(f'At {playerPos} facing {directionTags[playerDir]}')

print(f'Exit at {playerPos}')
