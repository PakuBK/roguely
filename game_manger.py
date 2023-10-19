from text_display import Display
from player import Player
import keyboard

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.world = [["#" for _ in range(width)] for _ in range(height)]

        self.display = Display(self.world, spacing=1)
        self.player = Player()

        self.setup_keyboard_events()

        self.display.update_tile_at(self.player.pos, self.player.symbol)
        self.display.display()
        #self.display.console_test()

        keyboard.wait("esc")

    def setup_keyboard_events(self):
        keyboard.add_hotkey("up", self.handle_player_movement, args=[(0, -1)])
        keyboard.add_hotkey("down", self.handle_player_movement, args=[(0, 1)])
        keyboard.add_hotkey("left", self.handle_player_movement, args=[(-1, 0)])
        keyboard.add_hotkey("right", self.handle_player_movement, args=[(1, 0)])

    def handle_player_movement(self, dir):
        new_pos = self.player.calculate_new_pos(dir)
        # check if pos is viable
        print(new_pos, self.height)
        # check width
        if new_pos[0] >= self.width or new_pos[1] >= self.height or (new_pos[0] < 0) or new_pos[1] < 0:
            return

        self.display.update_tile_at(self.player.pos, "#")
        self.display.update_tile_at(new_pos, self.player.symbol)

        self.player.pos = new_pos
        self.display.display()


