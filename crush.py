import tkinter as tk
from tkinter import simpledialog
import random

def draw_heart(canvas, x, y, size):
    # Coordinates for drawing the heart shape
    canvas.create_oval(x, y, x + size, y + size, fill="red", outline="red")
    canvas.create_oval(x + size, y, x + 2 * size, y + size, fill="red", outline="red")
    canvas.create_polygon(x, y + size * 0.5, x + size, y + size * 1.5, x + 2 * size, y + size * 0.5, fill="red", outline="red")

def animate_bubbling_hearts(canvas, heart_list):
    for _ in range(100):
        canvas.delete("all")
        for heart in heart_list:
            heart['y'] -= random.randint(1, 5)
            draw_heart(canvas, heart['x'], heart['y'], heart['size'])
        canvas.update()
        canvas.after(50)

def animate_sliding_hearts(canvas, heart_list):
    for _ in range(50):
        canvas.delete("all")
        for heart in heart_list:
            heart['y'] -= 5
            draw_heart(canvas, heart['x'], heart['y'], heart['size'])
        canvas.update()
        canvas.after(50)

def draw_message(canvas, name):
    canvas.delete("all")
    width, height = 500, 400
    
    # Draw decorative border
    canvas.create_rectangle(20, 20, width-20, height-20, outline="pink", width=10)
    
    # Draw small hearts around the border
    for i in range(25, width-25, 50):
        draw_heart(canvas, i, 30, 10)
        draw_heart(canvas, i, height-60, 10)
    for i in range(25, height-25, 50):
        draw_heart(canvas, 30, i, 10)
        draw_heart(canvas, width-60, i, 10)
    
    # Display the message
    canvas.create_text(width/2, height/2, text=f"Hey {name}, \n\nJust wanted to let you know that \nyou're on my mind. ❤️", font=("Arial", 18, "bold"), fill="black")

def main():
    # Create main window
    root = tk.Tk()
    root.title("Message to Crush")

    # Create canvas
    canvas = tk.Canvas(root, width=500, height=400)
    canvas.pack()

    # Prompt user for crush's name
    crush_name = simpledialog.askstring("Input", "Enter your crush's name:")

    # Initialize hearts
    heart_list = [{'x': random.randint(50, 450), 'y': random.randint(400, 800), 'size': random.randint(10, 30)} for _ in range(30)]
    
    # Animate hearts
    if crush_name:
        animate_bubbling_hearts(canvas, heart_list)
        animate_sliding_hearts(canvas, heart_list)
        draw_message(canvas, crush_name)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()