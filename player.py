class Player:
    def __init__(self, symbol="P"):
        self.symbol = f"[italic red]{symbol}[/italic red]"
        self.pos = (0,0)

    def calculate_new_pos(self, dir) -> tuple:
        return (self.pos[0] + dir[0], self.pos[1] + dir[1])

