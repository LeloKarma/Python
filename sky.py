import tkinter as tk
from tkinter import simpledialog
import random

class StarryNight:
    def __init__(self, root, name):
        self.root = root
        self.canvas = tk.Canvas(root, width=500, height=400, bg="black")
        self.canvas.pack()
        self.name = name
        self.stars = []

        self.canvas.bind("<Button-1>", self.add_star)
        self.root.after(5000, self.show_message)

    def add_star(self, event):
        x, y = event.x, event.y
        size = random.randint(2, 5)
        star = self.canvas.create_oval(x, y, x + size, y + size, fill="white", outline="white")
        self.stars.append(star)
        self.twinkle_star(star, size)

    def twinkle_star(self, star, size):
        colors = ["white", "yellow", "light blue"]
        def twinkle():
            current_color = self.canvas.itemcget(star, "fill")
            new_color = random.choice([color for color in colors if color != current_color])
            self.canvas.itemconfig(star, fill=new_color)
            self.root.after(500, twinkle)
        twinkle()

    def show_message(self):
        for star in self.stars:
            self.canvas.delete(star)
        width, height = 500, 400
        self.canvas.create_text(width/2, height/2, text=f"Good night, {self.name}!", font=("Arial", 24, "bold"), fill="white")

def main():
    # Create main window
    root = tk.Tk()
    root.title("Starry Night")

    # Prompt user for their name
    name = simpledialog.askstring("Input", "Enter your name:")

    # Initialize StarryNight scene
    if name:
        StarryNight(root, name)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()