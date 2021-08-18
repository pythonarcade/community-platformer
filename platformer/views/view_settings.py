"""
Main Menu
"""
import arcade

from platformer.views import View


class SettingsView(View):
    def __init__(self):
        super().__init__()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.ALMOND)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(
            "Settings is Under Construction",
            self.window.width / 2,
            self.window.height / 2,
            arcade.color.ALLOY_ORANGE,
            font_size=44,
            anchor_x="center",
            anchor_y="center",
        )

        arcade.draw_text(
            "Press Escape to Go Back",
            self.window.width / 2,
            self.window.height / 2 - 100,
            arcade.color.ALLOY_ORANGE,
            font_size=20,
            anchor_x="center",
            anchor_y="center",
        )

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            self.window.show_view(self.window.views["main_menu"])
