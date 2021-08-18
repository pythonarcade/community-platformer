"""
Main Menu
"""
import arcade
import arcade.gui

from platformer.views.view_game import GameView
from platformer.views.view_game_over import GameOverView
from platformer.views.view_settings import SettingsView


class MainMenuView(arcade.View):
    def __init__(self):
        super().__init__()

        self.started = False

        # UI Manager to handle the GUI
        self.ui_manager = None

        # A Vertical BoxGroup to align Buttons
        self.v_box = None

    def setup(self):
        self.ui_manager = arcade.gui.UIManager()

        self.setup_buttons()

        self.ui_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.v_box
            )
        )

        self.started = True

    def on_show(self):
        if not self.started:
            self.setup()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.ALMOND)
        if self.ui_manager:
            self.ui_manager.enable()

    def on_hide_view(self):
        if self.ui_manager:
            self.ui_manager.disable()

    def setup_buttons(self):
        self.v_box = arcade.gui.UIBoxGroup()

        play_button = arcade.gui.UIFlatButton(text="Start Game", width=200)

        @play_button.event("on_click")
        def on_click_play(event):
            if "game" not in self.window.views:
                self.window.views["game"] = GameView()
                self.window.views["game_over"] = GameOverView()
            self.window.show_view(self.window.views["game"])

        self.v_box.add(play_button.with_space_around(bottom=20))

        settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)

        @settings_button.event("on_click")
        def on_click_settings(event):
            if "settings" not in self.window.views:
                self.window.views["settings"] = SettingsView()
            self.window.show_view(self.window.views["settings"])

        self.v_box.add(settings_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)

        @quit_button.event("on_click")
        def on_click_quit(event):
            arcade.exit()

        self.v_box.add(quit_button)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text(
            "Arcade Community Platformer",
            self.window.width / 2,
            self.window.height - 125,
            arcade.color.ALLOY_ORANGE,
            font_size=44,
            anchor_x="center",
            anchor_y="center",
        )

        self.ui_manager.draw()
