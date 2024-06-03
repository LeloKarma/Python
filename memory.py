import tkinter as tk
from tkinter import simpledialog

class MemoryCandles:
    def __init__(self, root, name):
        self.root = root
        self.canvas = tk.Canvas(root, width=600, height=400, bg="black")
        self.canvas.pack()
        self.name = name
        self.candles = []
        self.init_candles()
        self.light_candles()

    def init_candles(self):
        candle_positions = [(120, 300), (220, 300), (320, 300), (420, 300), (520, 300)]
        for pos in candle_positions:
            candle = self.canvas.create_rectangle(pos[0] - 10, pos[1], pos[0] + 10, pos[1] - 100, fill="grey", outline="grey")
            flame = self.canvas.create_oval(pos[0] - 5, pos[1] - 110, pos[0] + 5, pos[1] - 90, fill="black", outline="black")
            self.candles.append((candle, flame))

    def light_candles(self):
        for i, (candle, flame) in enumerate(self.candles):
            self.root.after(i * 1000, self.light_candle, candle, flame)
        self.root.after(len(self.candles) * 1000, self.show_message)

    def light_candle(self, candle, flame):
        self.canvas.itemconfig(candle, fill="white", outline="white")
        self.canvas.itemconfig(flame, fill="yellow", outline="yellow")

    def show_message(self):
        width, height = 600, 400
        self.canvas.create_text(width / 2, height / 2 - 150, text=f"In Loving Memory of {self.name}", font=("Arial", 24, "bold"), fill="white")
        self.canvas.create_text(width / 2, height / 2 - 110, text="You are always in our hearts. 🕯️", font=("Arial", 18), fill="white")

def main():
    # Create main window
    root = tk.Tk()
    root.title("In Loving Memory")

    # Prompt user for the loved one's name
    name = simpledialog.askstring("Input", "Enter the name of your loved one:")

    # Initialize MemoryCandles scene
    if name:
        MemoryCandles(root, name)
 
    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
