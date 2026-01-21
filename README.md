# Rock Paper Scissors (Python CLI Game)

A command-line Rock Paper Scissors game where the user plays against the computer, featuring **score tracking**, **input validation**, and a **replay loop**.

The project focuses on clean game logic, controlled user input, and maintaining game state across multiple rounds.

---

## Features
- User vs computer gameplay
- Random computer choice using Python’s `random` module
- **Score tracking** for both player and computer
- **Replay option** after each round
- Strict **input validation** (only valid choices allowed)
- Clear round-by-round result messages
- Final score summary on exit

---

## How the Game Works
1. The computer randomly selects Rock, Paper, or Scissors
2. The user inputs their choice:
   - `r` → Rock  
   - `p` → Paper  
   - `s` → Scissors
3. The program compares choices and decides the result
4. Scores are updated accordingly
5. The user can choose to:
   - Play another round (`y`)
   - Exit the game (`n`)
6. Final scores are displayed when the game ends

---

## Concepts Used
- Functions
- Loops
- Conditional logic
- Dictionaries for mapping inputs
- Randomization
- Input validation
- Game state management (scores)

---

## How to Run
```bash

python rock_paper_scissors.py
```
## Example Gameplay
```bash

r-Rock
p-Paper
s-Scissor

Enter ur input: r

You chose : Rock
Computer chose : Paper

You Lose!.·°՞(っ-ᯅ-ς)՞°·.
```
