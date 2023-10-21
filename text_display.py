from rich import print as rprint
from rich.console import Console
import os
import time
import random

from rich.live import Live
from rich.table import Table

class Display:
    def __init__(self, world, spacing=0):
        self.console = Console()
        self.width = len(world[0][0])
        self.height = len(world[0])
        self.spacing = spacing
        self.table = self.generate_as_table(world)
        self.live_display = Live(self.table, auto_refresh=False)
        self.live_display.start(True)

    def update(self, img):
        self.table = self.generate_as_table(img)
        self.live_display.update(self.table, refresh=True)


    def generate_as_table(self, img) -> Table:
        table = Table()
        table.show_edge = False
        table.show_header = False
        # set up horizontal spacing
        img = [[ele + " " * self.spacing for ele in row] for row in img]
        for row in img:
            table.add_row("".join(row))
        return table

    def clean_up(self):
        os.system('cls')