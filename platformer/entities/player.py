from platformer.constants import LEFT_FACING, RIGHT_FACING
from platformer.entities.entity import Entity


class Player(Entity):
    """Player Sprite"""

    def __init__(self, character_number):

        if character_number == 1:
            folder = "assets/images/sprites/players/person_female"
            file_prefix = "character_femalePerson"
        elif character_number == 2:
            folder = "assets/images/sprites/players/adventurer_male"
            file_prefix = "character_maleAdventurer"
        elif character_number == 3:
            folder = "assets/images/sprites/players/adventurer_female"
            file_prefix = "character_femaleAdventurer"
        elif character_number == 4:
            folder = "assets/images/sprites/players/person_male"
            file_prefix = "character_malePerson"
        else:
            raise ValueError(f"Unknown character number {character_number}")

        # Set up parent class
        super().__init__(folder, file_prefix)

        # Track our state
        self.jumping = False
        self.climbing = False
        self.is_on_ladder = False

    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.facing_direction == RIGHT_FACING:
            self.facing_direction = LEFT_FACING
        elif self.change_x > 0 and self.facing_direction == LEFT_FACING:
            self.facing_direction = RIGHT_FACING

        # Climbing animation
        if self.is_on_ladder:
            self.climbing = True
        if not self.is_on_ladder and self.climbing:
            self.climbing = False
        if self.climbing and abs(self.change_y) > 1:
            self.cur_texture += 1
            if self.cur_texture > 7:
                self.cur_texture = 0
        if self.climbing:
            self.texture = self.climbing_textures[self.cur_texture // 4]
            return

        # Jumping animation
        if self.change_y > 0 and not self.is_on_ladder:
            self.texture = self.jump_texture_pair[self.facing_direction]
            return
        elif self.change_y < 0 and not self.is_on_ladder:
            self.texture = self.fall_texture_pair[self.facing_direction]
            return

        # Idle animation
        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.facing_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture][self.facing_direction]
