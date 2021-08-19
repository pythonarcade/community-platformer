from platformer.entities.enemy import Enemy


class Robot(Enemy):
    def __init__(self):

        # Set up parent class
        super().__init__("assets/images/sprites/enemies/robot", "character_robot")

        self.health = 100
