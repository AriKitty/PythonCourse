import math
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


def circle(page, radius, g, h, color='red'):
    # needs the top-left and bottom-right coordinates of a bounding rectangle
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     print(x)
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill='black')  # uses (x,y) points. Line from (-x, 0) to (x, 0)
    page.create_line(0, -y_origin, 0, y_origin, fill='black')


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill='blue')


mainWindow = tkinter.Tk()
mainWindow.title('Parabola')
mainWindow.geometry('640x480')

canvas = tkinter.Canvas(mainWindow, width=640, height=480, background='lightpink')
canvas.grid(row=0, column=0)

draw_axes(canvas)
parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 100, 100, 100, color='yellow')
circle(canvas, 100, 100, -100, color='blue')
circle(canvas, 100, -100, 100, color='purple')
circle(canvas, 100, -100, -100, color='green')
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)

mainWindow.mainloop()
