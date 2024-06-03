import tkinter as tk
from tkinter import simpledialog
import random

def create_confetti(canvas, confetti_list):
    for _ in range(100):
        x = random.randint(0, 500)
        y = random.randint(0, 400)
        size = random.randint(5, 15)
        color = random.choice(["red", "green", "blue", "yellow", "pink", "purple", "orange"])
        confetti_list.append({'x': x, 'y': y, 'size': size, 'color': color})

def animate_confetti(canvas, confetti_list):
    for _ in range(100):
        canvas.delete("all")
        for confetti in confetti_list:
            confetti['y'] += random.randint(1, 5)
            if confetti['y'] > 400:
                confetti['y'] = random.randint(-50, -10)
            canvas.create_oval(confetti['x'], confetti['y'], confetti['x'] + confetti['size'], confetti['y'] + confetti['size'], fill=confetti['color'], outline=confetti['color'])
        canvas.update()
        canvas.after(50)

def draw_card(canvas, name):
    canvas.delete("all")
    width, height = 500, 400

    # Draw a frame for the card
    canvas.create_rectangle(50, 50, width-50, height-50, outline="black", width=5)
    canvas.create_rectangle(60, 60, width-60, height-60, outline="gold", width=3)
    
    # Display the message
    canvas.create_text(width/2, height/2 - 50, text=f"Dear {name},", font=("Arial", 24, "bold"), fill="black")
    canvas.create_text(width/2, height/2, text="Wishing you a wonderful day\nfilled with joy and happiness!", font=("Arial", 18), fill="black")
    canvas.create_text(width/2, height/2 + 50, text="🎉🎈🎁", font=("Arial", 36), fill="black")

def main():
    # Create main window
    root = tk.Tk()
    root.title("Digital Card")

    # Create canvas
    canvas = tk.Canvas(root, width=500, height=400)
    canvas.pack()

    # Prompt user for their name
    name = simpledialog.askstring("Input", "Enter your name:")

    # Initialize confetti
    confetti_list = []
    create_confetti(canvas, confetti_list)
    
    # Animate confetti and then display the card
    if name:
        animate_confetti(canvas, confetti_list)
        draw_card(canvas, name)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()