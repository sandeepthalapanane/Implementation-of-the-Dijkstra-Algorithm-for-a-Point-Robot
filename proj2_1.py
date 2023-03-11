from queue import PriorityQueue
import time
import pygame
import vidmaker

st = time.time()


def to_pygame(coords, height):
    return (coords[0], height - coords[1])


def rect_pygame(coords, height, obj_height):
    return (coords[0], height - coords[1] - obj_height)


def create_map(visit, backtrack, start, Goal):
    pygame.init()
    size = [600, 250]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Visualization")
    video = vidmaker.Video("vidmaker.mp4", late_export=True)

    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill("white")
        x, y = rect_pygame([95, 0], 250, 105)
        pygame.draw.rect(screen, "blue", [x, y, 60, 105], 0)
        x, y = rect_pygame([100, 0], 250, 100)
        pygame.draw.rect(screen, "red", [x, y, 50, 100], 0)
        x, y = rect_pygame([95, 145], 250, 105)
        pygame.draw.rect(screen, "blue", [x, y, 60, 105], 0)
        a, b = rect_pygame([100, 150], 250, 100)
        pygame.draw.rect(screen, "red", [a, b, 50, 100], 0)
        pygame.draw.rect(screen, "blue", [0, 0, 5, 250], 0)
        pygame.draw.rect(screen, "blue", [0, 0, 600, 5], 0)
        pygame.draw.rect(screen, "blue", [0, 245, 600, 5], 0)
        pygame.draw.rect(screen, "blue", [595, 0, 5, 250], 0)
        a, b = to_pygame([455, 20], 250)
        c, d = to_pygame([463, 20], 250)
        e, f = to_pygame([1031/2, 125], 250)
        g, h = to_pygame([463, 230], 250)
        i, j = to_pygame([455, 230], 250)
        pygame.draw.polygon(
            screen, "blue", ([a, b], [c, d], [e, f], [g, h], [i, j]), 0)
        a, b = to_pygame([460, 25], 250)
        c, d = to_pygame([460, 225], 250)
        e, f = to_pygame([510, 125], 250)
        pygame.draw.polygon(screen, "red", [[a, b], [c, d], [e, f]], 0)
        a, b = to_pygame([300, 2675/13], 250)
        c, d = to_pygame([230, 2150/13], 250)
        e, f = to_pygame([230, 1100/13], 250)
        g, h = to_pygame([300, 575/13], 250)
        i, j = to_pygame([370, 1100/13], 250)
        k, l = to_pygame([370, 2150/13], 250)
        pygame.draw.polygon(screen, "blue", [[a, b], [c, d], [
                            e, f], [g, h], [i, j], [k, l]], 0)
        pygame.draw.polygon(screen, "red", ((235, 87.5), (300, 50),
                            (365, 87.5), (365, 162.5), (300, 200), (235, 162.5)))
        pygame.draw.circle(screen, (255, 255, 0), to_pygame(start, 250), 1)
        pygame.draw.circle(screen, (255, 255, 0), to_pygame(Goal, 250), 1)
        for j in visit:
            pygame.draw.circle(screen, (50, 137, 131), to_pygame(j, 250), 1)
            video.update(pygame.surfarray.pixels3d(
                screen).swapaxes(0, 1), inverted=False)
            pygame.display.flip()
            clock.tick(400)
        pygame.draw.circle(screen, (255, 255, 0), to_pygame(start, 250), 1)
        pygame.draw.circle(screen, (255, 255, 0), to_pygame(Goal, 250), 1)
        for i in backtrack:
            pygame.draw.circle(screen, (255, 255, 0), to_pygame(i, 250), 1)
            video.update(pygame.surfarray.pixels3d(
                screen).swapaxes(0, 1), inverted=False)
            pygame.display.flip()
            clock.tick(400)
        pygame.draw.circle(screen, (255, 255, 0), to_pygame(start, 250), 1)
        pygame.draw.circle(screen, (255, 255, 0), to_pygame(Goal, 250), 1)
        pygame.display.flip()
        pygame.time.wait(3000)
        done = True
    pygame.quit()
    video.export(verbose=True)


def check_obstacles(coordinates):
    x, y = coordinates[0], coordinates[1]
    if (x >= 230 and x <= 370 and (y-((15/26)*x) - 32.695) <= 0
        and (y+((15/26)*x) - 378.849) <= 0 and (y+((15/26)*x) - 217.304) >= 0
            and (y-((15/26)*x) + 128.849) >= 0):
        return False
    if (x >= 95 and y >= 0 and x <= 155 and y <= 105):
        return False
    if (x >= 95 and y >= 145 and x <= 155 and y <= 250):
        return False
    if (x >= 595 or y >= 245 or x <= 5 or y <= 5):
        return False
    if (x >= 455 and (y+(2*x) - 1156.18) <= 0 and y <= 230 and y >= 20 and (y-2*x + 906.18) >= 0):
        return False
    if (x < 0 or y < 0):
        return False
    if (x > 600 or y > 250):
        return False
    return True


def input_start(str):
    while True:
        print("Enter", str, "node (Sample: 10, 10 ): ")
        A = [int(i) for i in input().split(', ')]
        A_1 = (A[0], A[1])
        if not check_obstacles(A_1):
            print(
                "The entered input lies on the obstacles (or) not valid, please try again")
        else:
            return A_1


def check_conditions(que, coordinates, cost_to_come):
    if coordinates in touch:
        if touch[coordinates] > cost_to_come:
            new_que = (cost_to_come, coordinates)
            Path[coordinates] = que[1]
            Q.put(new_que)
            touch[coordinates] = cost_to_come
            return
        else:
            return
    new_que = (cost_to_come, coordinates)
    Path[coordinates] = que[1]
    Q.put(new_que)
    touch[coordinates] = cost_to_come


def moveup(que):
    coordinates = (que[1][0], que[1][1]+1)
    if check_obstacles(coordinates) and coordinates not in visit:
        cost_to_come = que[0] + 1
        check_conditions(que, coordinates, cost_to_come)


def movedown(que):
    coordinates = (que[1][0], que[1][1]-1)
    if check_obstacles(coordinates) and coordinates not in visit:
        cost_to_come = que[0] + 1
        check_conditions(que, coordinates, cost_to_come)


def moveleft(que):
    coordinates = (que[1][0]-1, que[1][1])
    if check_obstacles(coordinates) and coordinates not in visit:
        cost_to_come = que[0] + 1
        check_conditions(que, coordinates, cost_to_come)


def moveright(que):
    coordinates = (que[1][0]+1, que[1][1])
    if check_obstacles(coordinates) and coordinates not in visit:
        cost_to_come = que[0] + 1
        check_conditions(que, coordinates, cost_to_come)


def moveupleft(que):
    coordinates = (que[1][0]-1, que[1][1]+1)
    if check_obstacles(coordinates) and coordinates not in visit:
        cost_to_come = que[0] + 1.4
        check_conditions(que, coordinates, cost_to_come)


def moveupright(que):
    coordinates = (que[1][0]+1, que[1][1]+1)
    if check_obstacles(coordinates) and coordinates not in visit:
        cost_to_come = que[0] + 1.4
        check_conditions(que, coordinates, cost_to_come)


def movedownleft(que):
    coordinates = (que[1][0]-1, que[1][1]-1)
    if check_obstacles(coordinates) and coordinates not in visit:
        cost_to_come = que[0] + 1.4
        check_conditions(que, coordinates, cost_to_come)


def movedownright(que):
    coordinates = (que[1][0]+1, que[1][1]-1)
    if check_obstacles(coordinates) and coordinates not in visit:
        cost_to_come = que[0] + 1.4
        check_conditions(que, coordinates, cost_to_come)


def generate_path(path, start, Goal):
    backtrack = []
    key = path.get(Goal)
    backtrack.append(Goal)
    backtrack.append(key)
    while (key != start):
        key = path.get(key)
        backtrack.append(key)
    backtrack.reverse()
    return backtrack


def dijkstra_algorithm():
    while (Q.qsize() != 0):
        queue = Q.get()
        if (queue[1] != goal):
            if queue[1] not in visit:
                visit.append(queue[1])
                if (queue[1][1]+1 >= 0 and queue[1][1]+1 <= 250):
                    moveup(queue)
                if (queue[1][1]-1 >= 0 and queue[1][1]-1 <= 250):
                    movedown(queue)
                if (queue[1][0]-1 >= 0 and queue[1][0]-1 <= 600):
                    moveleft(queue)
                if (queue[1][0]+1 >= 0 and queue[1][0]+1 <= 600):
                    moveright(queue)
                if (queue[1][1]+1 <= 250 and queue[1][0]-1 >= 0):
                    moveupleft(queue)
                if (queue[1][0]+1 <= 600 and queue[1][1]+1 <= 250):
                    moveupright(queue)
                if (queue[1][0]-1 >= 0 and queue[1][1]-1 >= 0):
                    movedownleft(queue)
                if (queue[1][0]+1 <= 600 and queue[1][1]-1 <= 250):
                    movedownright(queue)
        else:
            print('success')
            Backtrack = generate_path(Path, Start, goal)
            print(Backtrack)
            print('-----------')
            print(queue)
            et = time.time()
            elapsed_time = et - st
            print('Time to calculate path:', elapsed_time, 'seconds')
            create_map(visit, Backtrack, Start, goal)
            break


Start = input_start('Start')
goal = input_start('Goal')
print(Start, goal)
visit = []
touch = {}
Path = {}
Q = PriorityQueue()
Q.put((0, Start))
dijkstra_algorithm()