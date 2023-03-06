import numpy as np
from matplotlib import pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(24, 10)
ax = plt.axes(xlim=(0, 600), ylim=(0, 250))

def create_map():
    obstacles = []
    for x in range(0, 601, 1):
        for y in range(0, 251, 1):
            if (x >= 230 and x <= 370 and (y-((15/26)*x) - 32.695) <= 0
                and (y+((15/26)*x) - 378.849) <= 0 and (y+((15/26)*x) - 217.304) >= 0
                    and (y-((15/26)*x) + 128.849) >= 0):
                ax.plot(int(x), int(y), color='r', marker='o', markersize=5)
                obstacles.append([int(x), int(y)])
            if (x >= 95 and y >= 0 and x <= 155 and y <= 105):
                ax.plot(int(x), int(y), color='r', marker='o', markersize=5)
                obstacles.append([int(x), int(y)])
            if (x >= 95 and y >= 145 and x <= 155 and y <= 250):
                ax.plot(int(x), int(y), color='r', marker='o', markersize=5)
                obstacles.append([int(x), int(y)])
            if (x >= 455 and (y+(2*x) - 1156.18) <= 0 and (y-2*x + 906.18) >= 0):
                ax.plot(int(x), int(y), color='r', marker='o', markersize=5)
                obstacles.append([int(x), int(y)])
    plt.show()
    return obstacles

obstacle = create_map()
