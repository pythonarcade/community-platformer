import arcade
import arcade.gui

from platformer.views import View


class GameOverView(View):
    def __init__(self):
        super().__init__()

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

    def setup_buttons(self):
        self.v_box = arcade.gui.UIBoxLayout()

        restart_button = arcade.gui.UIFlatButton(text="Restart", width=200)

        @restart_button.event("on_click")
        def on_click_restart(event):
            self.window.views["game"].setup()
            self.window.show_view(self.window.views["game"])

        self.v_box.add(restart_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)

        @quit_button.event("on_click")
        def on_click_quit(event):
            arcade.exit()

        self.v_box.add(quit_button)

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(
            "Game Over",
            self.window.width / 2,
            self.window.height / 2 + 100,
            arcade.color.WHITE,
            30,
            anchor_x="center",
            anchor_y="center",
        )
        self.ui_manager.draw()
