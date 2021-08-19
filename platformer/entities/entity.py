import arcade

from platformer.constants import CHARACTER_SCALING, RIGHT_FACING


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True),
    ]


class Entity(arcade.Sprite):
    def __init__(self, folder, file_prefix):
        super().__init__()

        # Default to facing right
        self.facing_direction = RIGHT_FACING

        # Used for image sequences
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING

        self.animations = {}

        self.idle_texture_pair = load_texture_pair(f"{folder}/{file_prefix}_idle.png")
        self.jump_texture_pair = load_texture_pair(f"{folder}/{file_prefix}_jump.png")
        self.fall_texture_pair = load_texture_pair(f"{folder}/{file_prefix}_fall.png")

        # Load textures for walking
        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{folder}/{file_prefix}_walk{i}.png")
            self.walk_textures.append(texture)

        # Load textures for climbing
        self.climbing_textures = []
        texture = arcade.load_texture(f"{folder}/{file_prefix}_climb0.png")
        self.climbing_textures.append(texture)
        texture = arcade.load_texture(f"{folder}/{file_prefix}_climb1.png")
        self.climbing_textures.append(texture)

        # Set the initial texture
        self.texture = self.idle_texture_pair[0]

        # Hit box will be set based on the first image used. If you want to specify
        # a different hit box, you can do it like the code below.
        # self.set_hit_box([[-22, -64], [22, -64], [22, 28], [-22, 28]])
        self.set_hit_box(self.texture.hit_box_points)
