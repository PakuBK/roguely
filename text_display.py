from rich import print as rprint
from rich.console import Console
import os

class Display:
    def __init__(self, world, spacing=1):
        self.console = Console()
        self.width = len(world[0][0])
        self.height = len(world[0])
        self.spacing = spacing
        self.display_image = [[ele + " " * spacing for ele in row] for row in world]

    def overwrite_image(self, image) -> None:
        self.display_image = [[ele + " " * self.spacing for ele in row] for row in image]

    def update_tile_at(self, pos: tuple, symbol:str) -> None:
        x,y = pos
        image = self.display_image.copy()
        image[y][x] = symbol + " " * self.spacing

    def display(self) -> None:
        console = self.console
        console.clear()
        for row in self.display_image:
            console.print("".join(row), justify="center")
            console.print("\n" * (self.spacing // 4), end="")

    def clear(self) -> None:
        self.console.clear()

