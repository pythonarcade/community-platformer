"""
Main Menu
"""
import arcade
import arcade.gui


class PauseView(arcade.View):
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
        arcade.set_background_color(arcade.color.ASH_GREY)
        if self.ui_manager:
            self.ui_manager.enable()

    def on_hide_view(self):
        if self.ui_manager:
            self.ui_manager.disable()

    def setup_buttons(self):
        self.v_box = arcade.gui.UIBoxGroup()

        resume_button = arcade.gui.UIFlatButton(text="Resume", width=200)

        @resume_button.event("on_click")
        def on_click_play(event):
            self.window.show_view(self.window.views["game"])

        self.v_box.add(resume_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)

        @quit_button.event("on_click")
        def on_click_quit(event):
            self.window.views["game"].started = False
            self.window.show_view(self.window.views["main_menu"])

        self.v_box.add(quit_button)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text(
            "Paused",
            self.window.width / 2,
            self.window.height - 125,
            arcade.color.ALLOY_ORANGE,
            font_size=44,
            anchor_x="center",
            anchor_y="center",
        )

        self.ui_manager.draw()
