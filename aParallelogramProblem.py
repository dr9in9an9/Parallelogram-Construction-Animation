# https://www.geeksforgeeks.org/python/using-matplotlib-for-animations/
# https://matplotlib.org/stable/users/explain/artists/paths.html

import matplotlib.pyplot as plt

from matplotlib.patches import PathPatch
from matplotlib.path import Path

def rectangle(len, wid, anchor, x, y):
    if anchor == "center":
        vertices = [
            (x + len/2 , y + wid/2),
            (x + len/2 , y - wid/2),
            (x - len/2 , y - wid/2),
            (x - len/2 , y + wid/2),
            (0, 0)
        ]
    elif anchor == "top left":
        vertices = [
            (x , y),
            (x , y - wid),
            (x + len , y - wid),
            (x + len , y),
            (0, 0)
        ]
    elif anchor == "bottom left":
        vertices = [
            (x , y + wid),
            (x , y),
            (x + len , y),
            (x + len , y + wid),
            (0, 0)
        ]
    

    codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]

    return Path(vertices, codes)

def prlelogrm(rectangle1, rectangle2):
    vertices = [
        (rectangle2.vertices[2][0] , rectangle1.vertices[0][1]),
        rectangle2.vertices[0],
        (rectangle1.vertices[3][0] , rectangle2.vertices[1][1]),

        (0 , 0)
    ]
    
    rectangle1.vertices
    rectangle2.vertices

    codes = [
        Path.MOVETO, 
        Path.LINETO, 
        Path.LINETO, 
        # Path.LINETO, 
        Path.CLOSEPOLY
    ]

    return Path(vertices, codes)


# path = rectangle(1.5, 1, "center", 1.5, 1)
figure, axis = plt.subplots()

# path = rectangle(4, 2, "bottom left", 1, 1)
# print(path.vertices)
# patch = PathPatch(path, facecolor='blue', edgecolor='blue', lw=0)
# axis.add_patch(patch)

# axis.add_patch(PathPatch(rectangle(2.25, 1.5, "top left", 1, 1), facecolor='green', edgecolor='green', lw=0))

top = rectangle(4, 2, "bottom left", 1, 1)
bot = rectangle(2.25, 1.5, "top left", 1, 1)

axis.add_patch(PathPatch(top, facecolor='blue', edgecolor='black', lw=1))
axis.add_patch(PathPatch(bot, facecolor='red', edgecolor='black', lw=1))

axis.add_patch(PathPatch(prlelogrm(top, bot), facecolor='none', edgecolor='yellow', lw=2))


axis.set_xlim(-1.5, 5.5)
axis.set_ylim(-1.5, 5.5)
axis.set_aspect('equal') # Optional, for better visualization
plt.show()