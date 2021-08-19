from platformer.entities.enemy import Enemy


class Zombie(Enemy):
    def __init__(self):

        # Set up parent class
        super().__init__("assets/images/sprites/enemies/zombie", "character_zombie")

        self.health = 50
