import math

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def parabola(page, size):
    for x in range(-size, size):
        y = x * x / size
        plot(page, x, y)


# Modify the circle to accept colour of circle or default value be red
def circle(page, radius, h, k, color="red"):
    page.create_oval(h + radius, k + radius, h - radius, k - radius, outline=color, width=2)
    # for x in range(h * 100, (h + radius) * 100):
    #     x /= 100
    #     print(x)
    #     y = k + (math.sqrt(radius ** 2 - (x - h) ** 2))
    #     plot(page, x, y)
    #     plot(page, x, 2 * k - y)
    #     plot(page, 2 * h - x, y)
    #     plot(page, 2 * h - x, 2 * k - y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, -y_origin, 0, y_origin, fill="black")
    print(locals())


def plot(page, x, y):
    page.create_line(x,  -y, x + 1, -y + 1, fill="red")


mainWindow = tkinter.Tk()
mainWindow.geometry("640x480")
mainWindow.title("Parabola")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)

circle(canvas, 100, 100, 100, "green")
circle(canvas, 100, 100, -100, color="yellow")
circle(canvas, 100, -100, 100, color="black")
circle(canvas, 100, -100, -100, "blue")
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30, color="green")
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30, color="magenta")
circle(canvas, 30, 0, 0, color="cyan")

mainWindow.mainloop()
