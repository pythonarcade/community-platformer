"""
Main Menu
"""
import arcade
import arcade.gui

from platformer.views.view import View
from platformer.views.view_game import GameView
from platformer.views.view_game_over import GameOverView
from platformer.views.view_pause import PauseView


class UIInteractiveSpriteWidget(arcade.gui.UIInteractiveWidget):
    """Create a UI element with a sprite that controls what is displayed."""

    def __init__(
        self, *, x=0, y=0, width=100, height=100, sprite: arcade.Sprite = None
    ):
        super().__init__(x, y, width, height)
        self._sprite = sprite

    def on_update(self, dt):
        self._sprite.update()
        self._sprite.update_animation(dt)  # ?

    def render(self, surface: arcade.gui.Surface, force=False):
        surface.clear((0, 0, 0, 0))
        surface.draw_sprite(0, 0, self.width, self.height, self._sprite)


class CharacterSelectView(View):
    def __init__(self):
        super().__init__()

        # A Horizontal BoxGroup to align Buttons
        self.h_box_upper = None
        self.h_box_lower = None

        self.selected_player = None

    def setup(self):
        super().setup()
        self.ui_manager = arcade.gui.UIManager()

        self.setup_buttons()

        self.ui_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.h_box_upper
            )
        )
        self.ui_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                align_y=100,
                child=self.h_box_lower,
            )
        )

    def on_show_view(self):
        arcade.set_background_color(arcade.color.ALMOND)

    def setup_buttons(self):
        self.h_box_upper = arcade.gui.UIBoxGroup(vertical=False)
        self.h_box_lower = arcade.gui.UIBoxGroup(vertical=False)

        character_one_image = "assets/images/sprites/players/person_female/character_femalePerson_idle.png"
        character_one_sprite = arcade.Sprite(character_one_image)
        character_one_button = UIInteractiveSpriteWidget(
            sprite=character_one_sprite, width=192, height=192
        )

        @character_one_button.event("on_click")
        def on_click_character_one(event):
            self.selected_player = 1

        self.h_box_upper.add(character_one_button.with_space_around(right=20))

        character_two_image = "assets/images/sprites/players/adventurer_male/character_maleAdventurer_idle.png"
        character_two_sprite = arcade.Sprite(character_two_image)
        character_two_button = UIInteractiveSpriteWidget(
            sprite=character_two_sprite, width=192, height=192
        )

        @character_two_button.event("on_click")
        def on_click_character_two(event):
            self.selected_player = 2

        self.h_box_upper.add(character_two_button.with_space_around(right=20))

        character_three_image = "assets/images/sprites/players/adventurer_female/character_femaleAdventurer_idle.png"
        character_three_sprite = arcade.Sprite(character_three_image)
        character_three_button = UIInteractiveSpriteWidget(
            sprite=character_three_sprite, width=192, height=192
        )

        @character_three_button.event("on_click")
        def on_click_character_three(event):
            self.selected_player = 3

        self.h_box_upper.add(character_three_button.with_space_around(right=20))

        character_four_image = (
            "assets/images/sprites/players/person_male/character_malePerson_idle.png"
        )
        character_four_sprite = arcade.Sprite(character_four_image)
        character_four_button = UIInteractiveSpriteWidget(
            sprite=character_four_sprite, width=192, height=192
        )

        @character_four_button.event("on_click")
        def on_click_character_four(event):
            self.selected_player = 4

        self.h_box_upper.add(character_four_button)

        play_button = arcade.gui.UIFlatButton(text="Start Game", width=200)

        @play_button.event("on_click")
        def on_click_play(event):
            if self.selected_player:
                print(f"starting game with player {self.selected_player}")
                if "game" not in self.window.views:
                    self.window.views["game"] = GameView()
                    self.window.views["game_over"] = GameOverView()
                    self.window.views["pause"] = PauseView()
                self.window.views["game"].selected_player = self.selected_player
                self.selected_player = None
                self.window.show_view(self.window.views["game"])

        self.h_box_lower.add(play_button.with_space_around(right=20))

        back_button = arcade.gui.UIFlatButton(text="Back", width=200)

        @back_button.event("on_click")
        def on_click_back(event):
            self.window.show_view(self.window.views["main_menu"])

        self.h_box_lower.add(back_button)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text(
            "Select a Character",
            self.window.width / 2,
            self.window.height - 125,
            arcade.color.ALLOY_ORANGE,
            font_size=44,
            anchor_x="center",
            anchor_y="center",
        )

        arcade.draw_text(
            f"Selected Character: {self.selected_player}",
            self.window.width / 2,
            200,
            arcade.color.ALLOY_ORANGE,
            font_size=24,
            anchor_x="center",
            anchor_y="center",
        )

        self.ui_manager.draw()
