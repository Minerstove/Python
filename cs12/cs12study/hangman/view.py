from typing import Iterable

class HangmanGameView:

    def show_welcome(self, max_wrong: int) -> None:
        print("🎯 Welcome to Hangman!")
        print(f"You have {max_wrong} incorrect guesses allowed.\n")

    def show_game_state(
        self,
        masked_word: str,
        wrong_letters: Iterable[str],
        remaining_attempts: int
    ) -> None:
        print("\nWord: ", masked_word)
        print("Wrong guesses:", ", ".join(wrong_letters) if wrong_letters else "None")
        print(f"Remaining attempts: {remaining_attempts}")

    def show_result(self, outcome: str) -> None:
        if outcome == "correct":
            print("✅ Correct!")
        elif outcome == "wrong":
            print("❌ Wrong guess.")
        elif outcome == "repeat":
            print("⚠️ You already guessed that letter.")
        elif outcome == "invalid":
            print("⚠️ Invalid guess. Enter a single letter.")

    def show_win(self, word: str) -> None:
        print(f"\n🎉 You won! The word was '{word}'.")

    def show_loss(self, word: str) -> None:
        print(f"\n💀 You lost. The word was '{word}'.")

    def show_goodbye(self) -> None:
        print("\nThanks for playing!")
