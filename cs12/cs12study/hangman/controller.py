from model import HangmanGameModel
from view import HangmanGameView

class HangmanGameController:
    model: HangmanGameModel
    view: HangmanGameView

    def __init__(self, model: HangmanGameModel, view: HangmanGameView) -> None:
        self.model = HangmanGameModel
        self.view = HangmanGameView

    def prompt_guess(self) -> str:
        return input("\nGuess a letter: ")
    
    def run(self) -> None:
        


        while True:
            