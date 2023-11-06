import random

def play_game(player_move):
    moves = ["rock", "paper", "scissors"]
    opponent_move = random.choice(moves)

    result = determine_result(player_move, opponent_move)

    print(f"You chose {player_move}. Opponent chose {opponent_move}. {result}")

def determine_result(player_move, opponent_move):
    if player_move == opponent_move:
        return "It's a tie!"
    elif (player_move == "rock" and opponent_move == "scissors") or \
         (player_move == "paper" and opponent_move == "rock") or \
         (player_move == "scissors" and opponent_move == "paper"):
        return "You win!"
    else:
        return "You lose!"

# Prompt the player for their move
player_input = input("Choose your move (rock, paper, or scissors): ").lower()

# Validate the player's input
valid_moves = ["rock", "paper", "scissors"]
if player_input not in valid_moves:
    print("Invalid move. Please choose rock, paper, or scissors.")
else:
    # Play the game
    play_game(player_input)