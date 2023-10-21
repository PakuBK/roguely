import asyncio

from text_display import Display
from player import Player
import keyboard
from tile import Tile

class Game:
    def __init__(self, width, height, std_symbol="#"):
        self.width = width
        self.height = height

        self.world = [[Tile(std_symbol) for _ in range(width)] for _ in range(height)]
        self.entities = []

        self.display = Display(get_render_copy(self.world), spacing=1)
        self.player = Player()

        self.setup_keyboard_events()

        self.loop = asyncio.get_event_loop()
        asyncio.ensure_future(self.game_tick())
        self.loop.run_forever()

    def setup_keyboard_events(self):
        keyboard.add_hotkey("up", self.handle_player_movement, args=[(-1, 0)])
        keyboard.add_hotkey("down", self.handle_player_movement, args=[(1, 0)])
        keyboard.add_hotkey("left", self.handle_player_movement, args=[(0, -1)])
        keyboard.add_hotkey("right", self.handle_player_movement, args=[(0, 1)])
        keyboard.add_hotkey("esc", self.quit_game)

    async def game_tick(self):
        while True:
            await asyncio.sleep(0.03)
            # get world tileset
            # handle logic
            self.display.update(self.generate_render_text_image())

    def update_world_tile(self, pos: tuple, symbol: str):
        x,y = pos
        self.world[x][y] = symbol

    def handle_player_movement(self, dir):
        new_pos = self.player.calculate_new_pos(dir)
        if new_pos[0] >= self.width or new_pos[1] >= self.height or (new_pos[0] < 0) or new_pos[1] < 0:
            return
        self.player.pos = new_pos

    def generate_render_text_image(self) -> list:
        """ layer the entities over the world tileset and return as a str list"""
        render_img = get_render_copy(self.world)
        entities = self.entities.copy()
        player = self.player
        for entity in entities:
            x,y = entity.pos
            render_img[x][y] = entity.symbol
        p_x, p_y = player.pos
        render_img[p_x][p_y] = player.symbol
        return render_img


    def quit_game(self):
        self.display.live_display.stop()
        self.display.clean_up()
        self.loop.stop()
        quit()


def get_render_copy(tileset) -> list:
    return [[tile.symbol for tile in row] for row in tileset]


