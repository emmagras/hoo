# From Tom Elliot's blog (http://telliott99.blogspot.com/)
# The following code creates randomly located points and draws them together with arrows,
# which is pretty neat.
# This will be edited in the coming days to accomodate plotting our cars.

import os
import numpy as np
import matplotlib.pyplot as plt

def draw_arrow(x, y, w, h, i):
    a = plt.Arrow(x,y,w,h,
                  width=0.05,zorder=i+1)
    a.set_facecolor('0.7')
    a.set_edgecolor('w')
    return a

def getArrow(p1,p2,i):
    w = p2.x - p1.x
    h = p2.y - p1.y
    if w == 0:
        dy = 0.03
        dx = 0
    else:
        theta = np.arctan(np.abs(h/w))
        dx = 0.03*np.cos(theta)
        dy = 0.03*np.sin(theta)

    if w < 0:
        dx *= -1
    if h < 0:
        dy *= -1
    w -= 2*dx
    h -= 2*dy
    x = p1.x + dx
    y = p1.y + dy

    a = draw_arrow(x, y, w, h, i)

    return a

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_points_from_file(path="", filename="temp_log.csv"):
    _dir = os.path.dirname(__file__)
    path = os.path.join(_dir, "../resources/logs/")

    with open(path + filename, "r") as f:
        lines = [[int(y[-3]), int(y[-2])] for y in [x.strip("\n").split(",") for x in f.readlines()]]
    print(lines)



def make_points(count, how="random"):
    L = np.random.uniform(size=count*2)
    points = [Point(L[i], L[i+1]) for i in range(0, count*2, 2)]
    print(points)
    return points

def main(count=10):
    points = make_points(count)

    ax = plt.axes()
    ax.set_xlim(-0.01,1.01)
    ax.set_ylim(-0.01,1.01)
    for i, point in enumerate(points):
        if i:
            arrow = getArrow(points[i-1], point, i)
            ax.add_patch(arrow)
        plt.scatter(point.x, point.y, s=250, zorder=1)
    plt.show()


if __name__ == "__main__":
    main()
