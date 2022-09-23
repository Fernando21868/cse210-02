import random


class Card:
    """A card whose values can vary between 1 and 13.

    The responsibility of Card is to keep track of the actual card and calculate the points for 
    it.

    Attributes:
        points (int): The score that the player will receive, depending on the play he has made.
        current_card (int) = The current card being played (1-13).
    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.current_card = 0
        self.points = 0

    def play_card(self, move, old_card):
        """Generates a score depending on whether the player was right or wrong in guessing if the next card will be higher or lower than the card played in the previous hand.

        Args:
            self (Card): An instance of Card.
            move (string): The player's move [h/l].
            old_card (int): The value of the card that was played in the previous hand.
        """
        if move == 'h':
            self.points = 100 if self.current_card > old_card else -75
        if move == 'l':
            self.points = 100 if self.current_card < old_card else -75

    def actual_card(self):
        """Generate a new card randomly, whose value is between 1-13.

        Args:
            self (Card): An instance of Card.
        """
        self.current_card = random.randint(1, 13)
