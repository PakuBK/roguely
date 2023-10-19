from tkinter import *
from tkinter import ttk

class Display:
    def __init__(self, width, height, symbol="#"):
        self.width = width
        self.height = height
        self.innerDisplay = [[symbol for y in range(height)] for x in range(width)]

    def draw(self, x, y, obj):
        for i in range(self.width):
            for j in range(self.height):
                self.innerDisplay[x][y] = obj

    def convert_display(self):
        tiles = self.innerDisplay
        string_tiles = ""
        for row in tiles:
            for tile in row:
                string_tiles += tile
            string_tiles += "\n"
        print(len(tiles))
        print(len(tiles[0]))
        return string_tiles

    def display(self):
        root = Tk()
        root.title("roguely")

        mainframe = ttk.Frame(root, padding="0 0 0 0")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text=self.convert_display()).grid(column=3, row=1, sticky=N)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        root.mainloop()