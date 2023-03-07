import numpy as np
from matplotlib import pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
from queue import PriorityQueue

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(24, 10)
ax = plt.axes(xlim=(0, 600), ylim=(0, 250))
i = 0


def create_map():
    obstacles = []
    for x in range(0, 601, 1):
        for y in range(0, 251, 1):
            if (x >= 230 and x <= 370 and (y-((15/26)*x) - 32.695) <= 0
                and (y+((15/26)*x) - 378.849) <= 0 and (y+((15/26)*x) - 217.304) >= 0
                    and (y-((15/26)*x) + 128.849) >= 0):
                # ax.plot(int(x), int(y), color='r', marker='o', markersize=5)
                obstacles.append([int(x), int(y)])
            if (x >= 95 and y >= 0 and x <= 155 and y <= 105):
                # ax.plot(int(x), int(y), color='r', marker='o', markersize=5)
                obstacles.append([int(x), int(y)])
            if (x >= 95 and y >= 145 and x <= 155 and y <= 250):
                # ax.plot(int(x), int(y), color='r', marker='o', markersize=5)
                obstacles.append([int(x), int(y)])
            if (x >= 455 and (y+(2*x) - 1156.18) <= 0 and (y-2*x + 906.18) >= 0):
                # ax.plot(int(x), int(y), color='r', marker='o', markersize=5)
                obstacles.append([int(x), int(y)])
    # plt.show()
    return obstacles


def input_start_goal(obstacles):
    print("Enter start node (Sample: 10, 10 ): ")
    A = [int(i) for i in input().split(', ')]
    A_1 = [A[0], A[1]]
    if A_1 in obstacles:
        print("The entered input lies on the obstacles, please try again")
    print("Enter goal node (Sample: 100, 100 ): ")
    B = [int(i) for i in input().split(', ')]
    B_1 = [B[0], B[1]]
    if B_1 in obstacles:
        print("The entered input lies on the obstacles, please try again")
    return A_1, B_1


def moveup(que):
    coordinates = (que[3][0]+1, que[3][1])
    if coordinates not in visit:
        cost_to_come = que[0] + 1
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    parent_index = que[1]
                    i += 1
                    new_que = (cost_to_come, i, parent_index, coordinates)
                    Q.put(new_que)
                else:
                    i += 1
                    Q.queue[i] = (cost_to_come, i, que[1], coordinates)


def movedown(que):
    coordinates = (que[3][0]-1, que[3][1])
    if coordinates not in visit:
        cost_to_come = que[0] + 1
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    parent_index = que[1]
                    i += 1
                    new_que = (cost_to_come, i, parent_index, coordinates)
                    Q.put(new_que)
                else:
                    i += 1
                    Q.queue[i] = (cost_to_come, i, que[1], coordinates)


def moveleft(que):
    coordinates = (que[3][0], que[3][1]-1)
    if coordinates not in visit:
        cost_to_come = que[0] + 1
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    parent_index = que[1]
                    i += 1
                    new_que = (cost_to_come, i, parent_index, coordinates)
                    Q.put(new_que)
                else:
                    i += 1
                    Q.queue[i] = (cost_to_come, i, que[1], coordinates)


def moveright(que):
    coordinates = (que[3][0], que[3][1]+1)
    if coordinates not in visit:
        cost_to_come = que[0] + 1
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    parent_index = que[1]
                    i += 1
                    new_que = (cost_to_come, i, parent_index, coordinates)
                    Q.put(new_que)
                else:
                    i += 1
                    Q.queue[i] = (cost_to_come, i, que[1], coordinates)


def moveupleft(que):
    coordinates = (que[3][0]+1, que[3][1]-1)
    if coordinates not in visit:
        cost_to_come = que[0] + 1.4
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    parent_index = que[1]
                    i += 1
                    new_que = (cost_to_come, i, parent_index, coordinates)
                    Q.put(new_que)
                else:
                    i += 1
                    Q.queue[i] = (cost_to_come, i, que[1], coordinates)


def moveupright(que):
    coordinates = (que[3][0]+1, que[3][1]+1)
    if coordinates not in visit:
        cost_to_come = que[0] + 1.4
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    parent_index = que[1]
                    i += 1
                    new_que = (cost_to_come, i, parent_index, coordinates)
                    Q.put(new_que)
                else:
                    i += 1
                    Q.queue[i] = (cost_to_come, i, que[1], coordinates)


def movedownleft(que):
    coordinates = (que[3][0]-1, que[3][1]-1)
    if coordinates not in visit:
        cost_to_come = que[0] + 1.4
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    parent_index = que[1]
                    i += 1
                    new_que = (cost_to_come, i, parent_index, coordinates)
                    Q.put(new_que)
                else:
                    i += 1
                    Q.queue[i] = (cost_to_come, i, que[1], coordinates)


def movedownright(que):
    coordinates = (que[3][0]-1, que[3][1]+1)
    if coordinates not in visit:
        cost_to_come = que[0] + 1.4
        for i in range(Q.qsize()):
            if Q.queue[i][3] == coordinates:
                if Q.queue[i][0] < cost_to_come:
                    parent_index = que[1]
                    i += 1
                    new_que = (cost_to_come, i, parent_index, coordinates)
                    Q.put(new_que)
                else:
                    i += 1
                    Q.queue[i] = (cost_to_come, i, que[1], coordinates)


obstacle = create_map()
# Start, goal = input_start_goal(obstacle)
Start, goal = (0, 0), (600, 250)
print(Start, goal)

visit = []
visit.append(Start)
Path = {}
Q = PriorityQueue()
Q.put((0, 0, 0, (Start)))
while (Q.qsize() != 0):
    queue = Q.get()
    visit.append(queue[3])
    if (queue[3] != goal):
        if (queue[3][0]+1 >= 0 and queue[3][0]+1 <= 600):
            moveup(queue)
        if (queue[3][0]-1 >= 0 and queue[3][0]-1 <= 600):
            movedown(queue)
        if (queue[3][1]-1 >= 0 and queue[3][1]-1 <= 600):
            moveleft(queue)
        if (queue[3][1]+1 >= 0 and queue[3][1]+1 <= 600):
            moveright(queue)
        if (queue[3][0]+1 <= 600 and queue[3][1]-1 >= 0):
            moveupleft(queue)
        if (queue[3][0]+1 <= 600 and queue[3][1]+1 <= 600):
            moveupright(queue)
        if (queue[3][0]-1 >= 0 and queue[3][1]-1 >= 0):
            movedownleft(queue)
        if (queue[3][0]-1 >= 0 and queue[3][1]+1 <= 600):
            movedownright(queue)
    else:
        print('success')
