from Class.Characters.Character import Character


class Player(Character):
    """
    Player class holds information about the player
    """

    def __init__(self, initial_position, health):
        """
        Constructor of the class
        """

        # Initializing Sprite related variables
        super().__init__(initial_position, health, "images/ship.png")

        # Initializing player's game variables
        self.points = 0
        self.double_guns = False
        self.shots = []
        self.enemies = []
        self.enemies_shots = []

    def update(self, delta):
        """
        Update function
        :param delta: Time lapse
        :return:
        """
        self.change_character_position(100 * delta, 0 * delta)
