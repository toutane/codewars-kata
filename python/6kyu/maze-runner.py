maze = [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 3],
        [1, 0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 2, 1, 0, 1, 0, 1]]

directions = ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E"]

# Le point (0, 0) est le coin en "bas a gauche"


def is_inside(n, size):
    return n < size and n >= 0


def maze_runner(maze, directions):
    cy, cx, size = 0, 0, len(maze)
    while cy < size and maze[cy][cx] != 2:
        while cx < size and maze[cy][cx] != 2:
            cx += 1
        if cx == size:
            cy += 1
            cx = 0
    cy = size - 1 - cy
    cd, ld = 0, len(directions)
    stop = False
    while not(stop):
        # print('Current positon: (', cx, ',', cy, ')', sep=' ')
        if not(is_inside(cy, size)) or not(is_inside(cx, size)) or maze[size - 1 - cy][cx] == 1 or cd == ld:
            stop = True
        else:
            if maze[size - 1 - cy][cx] == 3:
                stop = True
            else:
                nd = directions[cd]
                if nd == 'N':
                    cy += 1
                elif nd == 'E':
                    cx += 1
                elif nd == 'S':
                    cy -= 1
                elif nd == 'W':
                    cx -= 1
                cd += 1
    if not(is_inside(cy, size)) or not(is_inside(cx, size)) or maze[size - 1 - cy][cx] == 1:
        return 'Dead'
    elif maze[size - 1 - cy][cx] == 3:
        return 'Finish'
    else:
        return 'Lost'


print(maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E"]))
print(maze_runner(maze, ["N", "E", "E", "E", "E"]))
