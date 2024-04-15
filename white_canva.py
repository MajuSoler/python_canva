import tkinter as tk

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

        # Default color
        self.color = "black"
    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x, y, x+5, y+5, fill=self.color)

    def change_color(self):
        # Toggle between black and red colors
        if self.color == "black":
            self.color = "red"
        else:
            self.color = "black"

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Drawing App")
    app = DrawingApp(root)
    root.mainloop()