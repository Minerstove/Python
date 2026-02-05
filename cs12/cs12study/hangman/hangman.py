from model import HangmanGameModel
from view import HangmanGameView
from controller import HangmanGameController

def main() -> None:
    model: HangmanGameModel = HangmanGameModel()
    view: HangmanGameView = HangmanGameView()
    controller: HangmanGameController = HangmanGameController(model, view)
    controller.run()

if __name__ == "__main__":
    main()