import numpy as np
from matplotlib import pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
from queue import PriorityQueue

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(24, 10)
ax = plt.axes(xlim=(0, 600), ylim=(0, 250))

j = 0


def create_map():
    obstacles = []
    x_1 = []
    y_1 = []
    for x in range(0, 601, 1):
        for y in range(0, 251, 1):
            if (x >= 230 and x <= 370 and (y-((15/26)*x) - 32.695) <= 0
                and (y+((15/26)*x) - 378.849) <= 0 and (y+((15/26)*x) - 217.304) >= 0
                    and (y-((15/26)*x) + 128.849) >= 0):
                obstacles.append((int(x), int(y)))
                x_1.append(int(x))
                y_1.append(int(y))
            if (x >= 95 and y >= 0 and x <= 155 and y <= 105):
                obstacles.append((int(x), int(y)))
                x_1.append(int(x))
                y_1.append(int(y))
            if (x >= 95 and y >= 145 and x <= 155 and y <= 250):
                obstacles.append((int(x), int(y)))
                x_1.append(int(x))
                y_1.append(int(y))
            if (x >= 455 and (y+(2*x) - 1156.18) <= 0 and (y-2*x + 906.18) >= 0):
                obstacles.append((int(x), int(y)))
                x_1.append(int(x))
                y_1.append(int(y))
    ax.scatter(x_1, y_1, color='r', marker='o')
    return obstacles


def input_start(obstacles, str):
    print("Enter", str, "node (Sample: 10, 10 ): ")
    A = [int(i) for i in input().split(', ')]
    A_1 = (A[0], A[1])
    if A_1 in obstacles:
        print("The entered input lies on the obstacles, please try again")
        input_start(obstacles, str)
    return A_1


def moveup(que):
    global j
    coordinates = (que[3][0], que[3][1]+1)
    if coordinates not in visit and coordinates not in obstacle:
        cost_to_come = que[0] + 1
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    return
                else:
                    j += 1
                    Q.queue[i] = (cost_to_come, j, que[1], coordinates)
                    Path[coordinates] = que[3]
                    return
        parent_index = que[1]
        j += 1
        new_que = (cost_to_come, j, parent_index, coordinates)
        Path[coordinates] = que[3]
        Q.put(new_que)


def movedown(que):
    global j
    coordinates = (que[3][0], que[3][1]-1)
    if coordinates not in visit and coordinates not in obstacle:
        cost_to_come = que[0] + 1
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    return
                else:
                    j += 1
                    Q.queue[i] = (cost_to_come, j, que[1], coordinates)
                    Path[coordinates] = que[3]
                    return
        parent_index = que[1]
        j += 1
        new_que = (cost_to_come, j, parent_index, coordinates)
        Path[coordinates] = que[3]
        Q.put(new_que)


def moveleft(que):
    global j
    coordinates = (que[3][0]-1, que[3][1])
    if coordinates not in visit and coordinates not in obstacle:
        cost_to_come = que[0] + 1
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    return
                else:
                    j += 1
                    Q.queue[i] = (cost_to_come, j, que[1], coordinates)
                    Path[coordinates] = que[3]
                    return
        parent_index = que[1]
        j += 1
        new_que = (cost_to_come, j, parent_index, coordinates)
        Path[coordinates] = que[3]
        Q.put(new_que)


def moveright(que):
    global j
    coordinates = (que[3][0]+1, que[3][1])
    if coordinates not in visit and coordinates not in obstacle:
        cost_to_come = que[0] + 1
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    return
                else:
                    j += 1
                    Q.queue[i] = (cost_to_come, j, que[1], coordinates)
                    Path[coordinates] = que[3]
                    return
        parent_index = que[1]
        j += 1
        new_que = (cost_to_come, j, parent_index, coordinates)
        Path[coordinates] = que[3]
        Q.put(new_que)


def moveupleft(que):
    global j
    coordinates = (que[3][0]-1, que[3][1]+1)
    if coordinates not in visit and coordinates not in obstacle:
        cost_to_come = que[0] + 1.4
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    return
                else:
                    j += 1
                    Q.queue[i] = (cost_to_come, j, que[1], coordinates)
                    Path[coordinates] = que[3]
                    return
        parent_index = que[1]
        j += 1
        new_que = (cost_to_come, j, parent_index, coordinates)
        Path[coordinates] = que[3]
        Q.put(new_que)


def moveupright(que):
    global j
    coordinates = (que[3][0]+1, que[3][1]+1)
    if coordinates not in visit and coordinates not in obstacle:
        cost_to_come = que[0] + 1.4
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    return
                else:
                    j += 1
                    Q.queue[i] = (cost_to_come, j, que[1], coordinates)
                    Path[coordinates] = que[3]
                    return
        parent_index = que[1]
        j += 1
        new_que = (cost_to_come, j, parent_index, coordinates)
        Path[coordinates] = que[3]
        Q.put(new_que)


def movedownleft(que):
    global j
    coordinates = (que[3][0]-1, que[3][1]-1)
    if coordinates not in visit and coordinates not in obstacle:
        cost_to_come = que[0] + 1.4
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    return
                else:
                    j += 1
                    Q.queue[i] = (cost_to_come, j, que[1], coordinates)
                    Path[coordinates] = que[3]
                    return
        parent_index = que[1]
        j += 1
        new_que = (cost_to_come, j, parent_index, coordinates)
        Path[coordinates] = que[3]
        Q.put(new_que)


def movedownright(que):
    global j
    coordinates = (que[3][0]+1, que[3][1]-1)
    if coordinates not in visit and coordinates not in obstacle:
        cost_to_come = que[0] + 1.4
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    return
                else:
                    j += 1
                    Q.queue[i] = (cost_to_come, j, que[1], coordinates)
                    Path[coordinates] = que[3]
                    return
        parent_index = que[1]
        j += 1
        new_que = (cost_to_come, j, parent_index, coordinates)
        Path[coordinates] = que[3]
        Q.put(new_que)


def generate_path(path, start, Goal):
    backtrack = []
    key = path.get(goal)
    backtrack.append((Goal))
    backtrack.append((key))
    while (key != start):
        key = path.get(key)
        backtrack.append(key)
    backtrack.reverse()
    return backtrack


obstacle = create_map()
Start = input_start(obstacle, 'Start')
goal = input_start(obstacle, 'Goal')
# Start, goal = (0, 0), (50, 50)
print(Start, goal)
visit = []
Path = {}
Q = PriorityQueue()
Q.put((0, 0, 0, (Start)))
while (Q.qsize() != 0):
    queue = Q.get()
    visit.append(queue[3])
    if (queue[3] != goal):
        if (queue[3][1]+1 >= 0 and queue[3][1]+1 <= 250):
            moveup(queue)
        if (queue[3][1]-1 >= 0 and queue[3][1]-1 <= 250):
            movedown(queue)
        if (queue[3][0]-1 >= 0 and queue[3][0]-1 <= 600):
            moveleft(queue)
        if (queue[3][0]+1 >= 0 and queue[3][0]+1 <= 600):
            moveright(queue)
        if (queue[3][1]+1 <= 250 and queue[3][0]-1 >= 0):
            moveupleft(queue)
        if (queue[3][0]+1 <= 600 and queue[3][1]+1 <= 250):
            moveupright(queue)
        if (queue[3][0]-1 >= 0 and queue[3][1]-1 >= 0):
            movedownleft(queue)
        if (queue[3][0]+1 <= 600 and queue[3][1]-1 <= 250):
            movedownright(queue)
    else:
        print('success')
        Backtrack = generate_path(Path, Start, goal)
        print(Backtrack)
        print('-----------')
        print(queue)
        break

# for ele in visit:
#     ax.scatter(ele[0], ele[1], marker='s', color='#1f77b4')
#     plt.pause(0.025)

# for i in Backtrack:
#     ax.scatter(i[0], i[1], marker='s', color='k')
#     plt.pause(0.025)
# plt.show()
