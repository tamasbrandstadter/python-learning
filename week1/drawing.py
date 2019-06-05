import random
import tkinter as tk


def draw_line(x_cord, y_cord):
    canvas.create_line(x_cord, y_cord, 150, 150)
    canvas.create_line(y_cord, x_cord, 150, 150)


def draw_rect(x_cord, y_cord):
    canvas.create_rectangle(x_cord, y_cord, x_cord + 50, y_cord + 50)


root = tk.Tk()

canvas = tk.Canvas(root, width='400', height='400')
canvas.pack()

# draw a red horizontal line to the canvas' middle.
canvas.create_line(0, 150, 150, 150, fill="red2", width=3)
# draw a green vertical line to the canvas' middle.
canvas.create_line(150, 0, 150, 150, fill="red2", width=3)

# Draw the canvas' diagonals.
# If it starts from the upper-left corner it should be green, otherwise it should be red.
canvas.create_line(0, 0, 300, 300, fill="green", arrow=tk.LAST)
canvas.create_line(300, 300, 0, 0, fill="red", arrow=tk.LAST)
canvas.create_line(0, 300, 300, 0, fill="red", arrow=tk.LAST)
canvas.create_line(300, 0, 0, 300, fill="red", arrow=tk.LAST)

# draw a green 10x10 square to the center of the canvas.
canvas.create_rectangle(140, 140, 150, 150, fill="green")

# Draw four different size and color rectangles.
# Avoid code duplication.
colors = ['red', 'blue', 'yellow', 'green']
for i in range(4):
    x = random.randint(30, 300)
    y = random.randint(30, 300)
    color = colors[random.randint(0, 3)]
    canvas.create_rectangle(x - 30, y - 30, x, y, fill=color)

# Fill the canvas with a checkerboard pattern.
cell_size = 300 // 8
offset_x = 10 // 8
offset_y = 10 // 8

for row in range(8):
    for column in range(8):
        if (row + column) % 2 == 0:
            color = 'white'
        else:
            color = 'black'
        x = offset_x + row * cell_size
        y = offset_y + column * cell_size
        canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill=color)

# Create a function that draws a single line and takes 2 parameters:
# The x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# Fill the canvas with lines from the edges, every 20 px, to the center.
for row in range(0, 280, 20):
    for column in (0, 280, 20):
        draw_line(row, column)

root.mainloop()
