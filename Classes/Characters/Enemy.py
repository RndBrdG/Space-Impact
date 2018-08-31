from Classes.Characters.Character import Character


class Enemy(Character):
    """
    Classes that holds all the information about the enemy objects
    """

    def __init__(self, initial_position, hp, boss=False):
        """
        Constructor
        :param initial_position: Initial position
        :param hp: Amount of health points this character will start with
        """
        super().__init__(initial_position, hp, "Images/enemy_ship.png")
        self.boss = boss

    def update(self, mov):
        """
        Update Function that takes into consideration time lapsed.
        :param delta: Time elapsed. It is turned into negative, since enemies will travel in opposite ways
        """

        if isinstance(mov, float):
            return

        self.change_character_position(mov[0], mov[1])
