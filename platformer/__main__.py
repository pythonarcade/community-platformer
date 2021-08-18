import arcade

from platformer.constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH
from platformer.views.view_main_menu import MainMenuView


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False)

        self.views = {}

        self.views["main_menu"] = MainMenuView()


def main() -> None:
    window = GameWindow()
    window.show_view(window.views["main_menu"])
    arcade.run()


if __name__ == "__main__":
    main()
