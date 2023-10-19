from text_display import Display
from player import Player
import keyboard

class Game:
    def __init__(self, width, height, std_symbol="#"):
        self.width = width
        self.height = height
        self.world = [[std_symbol for _ in range(width)] for _ in range(height)]

        self.display = Display(self.world, spacing=1)
        self.player = Player()
        self.under_player_symbol = std_symbol

        self.setup_keyboard_events()

        self.display.update_tile_at(self.player.pos, self.player.symbol)
        self.display.display()
        #self.display.console_test()

        keyboard.wait()


    def setup_keyboard_events(self):
        keyboard.add_hotkey("up", self.handle_player_movement, args=[(0, -1)])
        keyboard.add_hotkey("down", self.handle_player_movement, args=[(0, 1)])
        keyboard.add_hotkey("left", self.handle_player_movement, args=[(-1, 0)])
        keyboard.add_hotkey("right", self.handle_player_movement, args=[(1, 0)])
        keyboard.add_hotkey("enter", self.test_tile_manipulation, args=["X"])
        keyboard.add_hotkey("esc", self.quit_game)

    def update_world_tile(self, pos : tuple, symbol : str):
        x,y = pos
        self.world[x][y] = symbol
        self.display.update_tile_at(pos, symbol)

    def handle_player_movement(self, dir):
        new_pos = self.player.calculate_new_pos(dir)
        # check if pos is viable
        print(new_pos, self.height)
        # check width
        if new_pos[0] >= self.width or new_pos[1] >= self.height or (new_pos[0] < 0) or new_pos[1] < 0:
            return

        world_symbol = self.world[self.player.pos[0]][self.player.pos[1]]

        self.display.update_tile_at(self.player.pos, world_symbol)  # replace the p-symbol with orginal symbol

        self.display.update_tile_at(new_pos, self.player.symbol)

        self.player.pos = new_pos
        self.display.display()

    def test_tile_manipulation(self, symbol):
        self.update_world_tile(self.player.pos, symbol)
        self.display.display()

    def quit_game(self):
        self.display.clear()
        quit()


