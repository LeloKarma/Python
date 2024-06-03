import tkinter as tk
import math
import random

def draw_spirograph(canvas, R, r, d):
    canvas.delete("all")
    width, height = 400, 400
    canvas.config(bg="black")

    theta = 0.0
    x0 = width // 2
    y0 = height // 2
    while theta < 2 * math.pi * r:
        x = (R - r) * math.cos(theta) + d * math.cos((R - r) / r * theta)
        y = (R - r) * math.sin(theta) - d * math.sin((R - r) / r * theta)
        canvas.create_oval(x0 + x - 1, y0 + y - 1, x0 + x + 1, y0 + y + 1, outline=random.choice(colors))
        theta += 0.01

def update_canvas():
    R = random.randint(50, 150)
    r = random.randint(10, 50)
    d = random.randint(50, 150)
    draw_spirograph(canvas, R, r, d)
    
    # Clear any previous message text
    canvas.delete("message")
    
    message = random.choice(messages)
    canvas.create_text(200, 200, text=message, fill="white", font=("Helvetica", 32, "bold"), tags="message")

root = tk.Tk()
root.title("Creative Tkinter Art")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

button = tk.Button(root, text="Generate Art", command=update_canvas)
button.pack()

colors = ['#FF5733', '#FFBD33', '#DBFF33', '#75FF33', '#33FF57', '#33FFBD', '#33DBFF', '#3375FF', '#5733FF', '#BD33FF', '#FF33DB', '#FF3375']
messages = ["Stay Creative!", "Code Art!", "Python Power!", "Keep Coding!", "Tkinter Magic!", "Hello World!", "Programming Fun!", "Create & Inspire!", "Tech Art!", "Innovate!"]

update_canvas()

root.mainloop()