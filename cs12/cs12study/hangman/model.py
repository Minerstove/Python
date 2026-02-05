class HangmanGameModel:
    lives: int
    word: str
    guess: str
    stage: list[str]
    dictionary: list[str]
    guessed_letters: list[str]
    game_over: bool
    game_state: str
    
    def __init__(self):
        pass

    def reset(self) -> None:
        self.lives = 5