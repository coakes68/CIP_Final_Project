# CIP_Final_Project
Code In Place Final Project - Rock-Paper-Scissors-Lizard-Spock

This is my take on the old Rock, Paper, Scissors game.

The game will use a text-based interface, be lightweight (no external dependencies), and include error handling for invalid inputs (e.g., handling EOFError and environment-specific input issues).

# The game features the following:
<dl>
<b>Multiplayer Mode:</b>
  <dd>Option to choose single-player (vs. computer) or multiplayer (player vs. player).</dd>
  <dd>In multiplayer, both players input choices (with input masking for fairness).</dd>
  <dd>In single player mode, Player 1 enters name and Computer is assigned a "special" name.</dd>
  <dd>In multiplayer mode, both Player 1 and Player 2 enter their names.</dd>
</dl>
<dl>Flexible Input: Accepts full choice names or single-letter shortcuts for convenience.</dl>
<dl>
<b>Clear win/loss rules:</b>
  <dd>Rock crushes Scissors and Lizard.</dd>
  <dd>Paper covers Rock and disproves Spock.</dd>
  <dd>Scissors cuts Paper and decapitates Lizard.</dd>
  <dd>Lizard poisons Spock and eats Paper.</dd>
  <dd>Spock smashes Scissors and vaporizes Rock.</dd>
</dl>
<dl>
<b>Difficulty Levels:</b>
  <dd>Easy: Random computer choices (as in the original).</dd>
  <dd>Medium: Tracks player’s last 3 choices and biases toward counters.</dd>
  <dd>Hard: Uses a simple Markov chain to predict based on choice history.</dd>
</dl>
<dl>Score Tracking: Keeps track of player and computer scores across rounds.</dl>
<dl>Multiple Rounds: Option to play multiple rounds.</dl>
<dl>Quit Anytime: Players can exit via quit/q or after any round.</dl>
<dl>Input validation with error handling.</dl>
<dl>
<b>Error Handling:</b>
  <dd>Handles invalid inputs</dd>
  <dd>EOFError</dd>
  <dd>KeyboardInterrupt</dd>
  <dd>unexpected exceptions</dd>
  <dd>5-attempt limit and retry option.</dd>
</dl>
<dl>Random Computer Choice: Ensures fair gameplay with random.choice.</dl>
<dl>Safe First Move: No board setup needed, so no first-move issues.</dl>
<dl>
<b>Custom Choices:</b>
  <dd>Players can define custom choices and win conditions (e.g., "fire" beats "ice") or use default RPSLS.</dd>
  <dd>Input via a setup phase, validated for consistency (each choice beats exactly two others).</dd>
</dl>
<dl>
<b>Visual Features:</b>
  <dd>Display ASCII art for each choice (rock, paper, scissors, lizard, or spock).</dd>
  <dd>Clear Display shows round number, current score, and game results with a clean console layout.</dd>
</dl>

# How to Play the game:

<dl>
<dd>Run the script: python RPSLSgame.py.
<dd>Read the rules displayed at the start, which explain how each choice beats two others.
<dd>Enter your choice when prompted:
<dd>Full names: rock, paper, scissors, lizard, spock or Shortcuts: r, p, s, l, k.
<dd>Quit: quit or q.
<dd>The computer randomly chooses.
<dd>The game shows both choices, the result (win, loss, or tie), and updates the score.
<dd>After each round, choose to play again (yes/y) or exit (any other input).
<dd>On quit or exit, the final score is displayed.
</dd>
</dl>
