"""
Main Menu
"""
import arcade
import arcade.gui

from platformer.views import CharacterSelectView, SettingsView, View


class MainMenuView(View):
    def __init__(self):
        super().__init__()

        # A Vertical BoxGroup to align Buttons
        self.v_box = None

    def setup(self):
        super().setup()
        self.ui_manager = arcade.gui.UIManager()

        self.setup_buttons()

        self.ui_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.v_box
            )
        )

    def on_show_view(self):
        arcade.set_background_color(arcade.color.ALMOND)

    def setup_buttons(self):
        self.v_box = arcade.gui.UIBoxLayout()

        play_button = arcade.gui.UIFlatButton(text="Start Game", width=200)

        @play_button.event("on_click")
        def on_click_play(event):
            if "character_select" not in self.window.views:
                self.window.views["character_select"] = CharacterSelectView()
            self.window.show_view(self.window.views["character_select"])

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
