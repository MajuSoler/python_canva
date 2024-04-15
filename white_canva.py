import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()
        print('This is the testing')
        self.canvas.bind("<B1-Motion>", self.draw)

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x, y, x+5, y+5, fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Drawing App")
    app = DrawingApp(root)
    root.mainloop()