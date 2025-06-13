# CIP_Final_Project
Code In Place Final Project
Rock-Paper-Scissors-Lizard-Spock

This is my take on the old Rock, Paper, Scissors game.

The game will use a text-based interface, be lightweight (no external dependencies), and include error handling for invalid inputs, drawing from lessons learned in previous games (e.g., handling EOFError and environment-specific input issues).

The game features the following:

Multiplayer Mode:

Option to choose single-player (vs. computer) or multiplayer (player vs. player).
In multiplayer, both players input choices (with input masking for fairness).
In single player mode, Player 1 enters name and Computer is assigned a "special" name.
In multiplayer mode, both Player 1 and Player 2 enter their names.

Flexible Input: Accepts full choice names or single-letter shortcuts for convenience.

Clear win/loss rules:
  Rock crushes Scissors and Lizard.
  Paper covers Rock and disproves Spock.
  Scissors cuts Paper and decapitates Lizard.
  Lizard poisons Spock and eats Paper.
  Spock smashes Scissors and vaporizes Rock.

Difficulty Levels:
Easy: Random computer choices (as in the original).
    Medium: Tracks player’s last 3 choices and biases toward counters.
    Hard: Uses a simple Markov chain to predict based on choice history.
Score Tracking: Keeps track of player and computer scores across rounds.
Multiple Rounds: Option to play multiple rounds.
Quit Anytime: Players can exit via quit/q or after any round.
Input validation with error handling.
Error Handling:
    Handles invalid inputs
    EOFError
    KeyboardInterrupt
    unexpected exceptions
    5-attempt limit and retry option.
Random Computer Choice: Ensures fair gameplay with random.choice.
Safe First Move: No board setup needed, so no first-move issues.
Custom Choices:
    Players can define custom choices and win conditions (e.g., "fire" beats "ice") or use default RPSLS.
    Input via a setup phase, validated for consistency (each choice beats exactly two others).
Visual Features:
    Display ASCII art for each choice (rock, paper, scissors, lizard, or spock).
    Clear Display shows round number, current score, and game results with a clean console layout.


How to Play the game:

Run the script: python RPSLSgame.py.
Read the rules displayed at the start, which explain how each choice beats two others.
Enter your choice when prompted:
Full names: rock, paper, scissors, lizard, spock.
Shortcuts: r, p, s, l, k.
Quit: quit or q.
The computer randomly chooses.
The game shows both choices, the result (win, loss, or tie), and updates the score.
After each round, choose to play again (yes/y) or exit (any other input).
On quit or exit, the final score is displayed.





