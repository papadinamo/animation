import tkinter as tk
import math


def draw_rose():
    canvas.delete("all")
    n = n_slider.get()
    d = d_slider.get()

    k = n / d
    scale = 150
    points = []

    for theta in range(0, 360 * d, 1):
        rad = math.radians(theta)
        r = math.sin(k * rad)
        x = width / 2 + scale * r * math.cos(rad)
        y = height / 2 - scale * r * math.sin(rad)
        points.append((x, y))

    for i in range(len(points) - 1):
        canvas.create_line(points[i][0], points[i][1],
                           points[i + 1][0], points[i + 1][1],
                           fill="white", width=1.5)


root = tk.Tk()
root.title("Полярная роза")
root.configure(bg="#2e2e2e")

width, height = 500, 500
canvas = tk.Canvas(root, width=width, height=height, bg="#2e2e2e", highlightthickness=0)
canvas.pack()

frame = tk.Frame(root, bg="#2e2e2e")
frame.pack(pady=10)

tk.Label(frame, text="n", fg="white", bg="#2e2e2e").grid(row=0, column=0)
n_slider = tk.Scale(frame, from_=1, to=15, orient="horizontal", command=lambda x: draw_rose(), bg="#2e2e2e", fg="white")
n_slider.set(3)
n_slider.grid(row=0, column=1)

tk.Label(frame, text="d", fg="white", bg="#2e2e2e").grid(row=1, column=0)
d_slider = tk.Scale(frame, from_=1, to=15, orient="horizontal", command=lambda x: draw_rose(), bg="#2e2e2e", fg="white")
d_slider.set(2)
d_slider.grid(row=1, column=1)

draw_rose()
root.mainloop()

