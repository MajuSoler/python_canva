import tkinter as tk
from tkinter import colorchooser  # Import the colorchooser module
class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()
        print('This is the testing')
        self.canvas.bind("<B1-Motion>", self.draw)
        # Add a button to change color
        self.color_button = tk.Button(root, text="Change Color", command=self.change_color)
        self.color_button.pack()

        self.color = "black"

          # Add a button to change color
        self.color_button = tk.Button(root, text="Change Color", command=self.change_color)
        self.color_button.pack()

        # Default color
        self.color = "black"
    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x, y, x+5, y+5, fill=self.color)

<<<<<<< HEAD
    def change_color(self):
        # Toggle between black and red colors
        if self.color == "black":
            self.color = "red"
        else:
            self.color = "black"
=======

    def change_color(self):
        # Open a color chooser dialog to select a color
        color = colorchooser.askcolor(title="Choose a color")[1]  # askcolor returns a tuple, we need the second element
        if color:  # If a color was selected
            self.color = color  # Update the current color

>>>>>>> 1c3b430fbd38f3ac5190dd42ac58bde85dd86a49

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Drawing App")
    app = DrawingApp(root)
    root.mainloop()