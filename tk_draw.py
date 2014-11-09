## module to draw things with tkinter

from Tkinter import *
import board_properties as Config

"""
/*\ tkinter draw function /*\
Returns a Tkinter instance for future Tkinter calls
"""

def     get_instance():
    return Tk()

"""
/*\ tkinter draw function /*\
Returns a canvas object to draw on
"""

def     get_window(instance):
    canvas = Canvas(instance, width=Config.xmax, height=Config.ymax)
    canvas.pack()
    return canvas

"""
/*\ tkinter draw function /*\
Calls Tkinter mainloop() function
"""

def     do_mainloop():
    mainloop()
    return

"""
/*\ tkinter draw function /*\
Draws the map in the canvas on the window
Ghost is red, pacman is yellow, path taken is pink
"""

def     draw_map(window, fileMap, path, distances):
    y = 0
    tmpy = 0
    yMax = len(fileMap)
    xMax = len(fileMap[0])
    yLen = Config.ymax / yMax
    xLen = Config.xmax / xMax
    for line in fileMap:
        x = 0
        tmpx = 0
        for case in line:
            seek = look_for_path(tmpx, tmpy, xMax, path)
            if seek != -1:
                window.create_rectangle(x, y, x + xLen, y + yLen, fill="pink")
                canvas_id = window.create_text(x, y, anchor="nw", fill="black")
                window.itemconfig(canvas_id, text=distances[str(xMax * tmpy + tmpx)], font=('Helvetica', '20'))
            if case == Config.ghost_rpz:
                window.create_rectangle(x, y, x + xLen, y + yLen, fill="red")
            elif case == Config.pacman_rpz:
                window.create_rectangle(x, y, x + xLen, y + yLen, fill="yellow")
            elif case == Config.wall_rpz:
                window.create_rectangle(x, y, x + xLen, y + yLen, fill="white")
            elif seek == -1:
                window.create_rectangle(x, y, x + xLen, y + yLen, fill="black")
            x += xLen + 1
            tmpx += 1
        y += yLen + 1
        tmpy += 1
    return

"""
/*\ tkinter draw function /*\
Search if the actual case is on the ghost path to print the distance after
"""

def     look_for_path(x, y, xmax, path):
    i = 0
    while i < len(path):
        if int(path[i]) == ((xmax * y) + x):
            path.remove(path[i])
            return i
        i += 1
    return -1
