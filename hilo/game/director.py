from game.card import Card


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (Card): An instance of Card class.
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): The score for the entire game start at 300.
        current_card (int): The card currently being played.
        old_card (int): The card that was previously played.
        move (string): The player's move, higher or lower [h,l].
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.card = Card()
        self.is_playing = True
        self.total_score = 300
        self.next_card = 9
        self.old_card = 0
        self.move = ""

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.show_card()
            self.get_card()
            self.do_updates()
            self.do_outputs()
            self.get_inputs()

    def show_card(self):
        """Print the actual card.

        Args:
            self (Director): an instance of Director.
        """
        next_card = self.next_card
        print(f"The card is: {next_card}")

    def get_card(self):
        """Ask for a higher or a lower card. Swap card values. The next card will have another value between (1-13), and the old card will have the value that the previous card had. Show the next card.

        Args:
            self (Director): An instance of Director.
        """
        while True:
            self.move = input("Higher or lower? [h/l] ")
            if (self.move == "h" or self.move == "l"):
                break
        self.old_card = self.next_card
        self.card.actual_card()
        self.next_card = self.card.current_card
        print(f"Next card was: {self.next_card}")

    def get_inputs(self):
        """Ask the user if they want to play another card.

        Args:
            self (Director): An instance of Director.
        """
        if not(self.is_playing):
            print("The game is over. You reached score 0")
        else:
            play_again = input("Play again? [y/n] ")
            self.is_playing = (play_again == "y")
            print()

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        card = self.card
        card.play_card(self.move, self.old_card)
        self.total_score += self.card.points

    def do_outputs(self):
        """Displays the total score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Your score is: {self.total_score}")
        self.is_playing = (self.total_score > 0)
