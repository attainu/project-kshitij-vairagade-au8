import time
import random
import sys

SLEEP_BETWEEN_ACTIONS = 1
MAX_VAL = 100
DICE_FACE = 6

# s takes you down from 'key' to 'value'
s = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}

# l takes you up from 'key' to 'value'
l = {
    3: 20,
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}

turn_of_player = [
    "Your turn.",
    "Go.",
    "Please proceed.",
    "Lets win this.",
    "Are you ready?",
    "",
]

bite_of_snake = [
    "Yeah! I am a snake",
    "bummer",
    "snake bite",
    "you won't survive",
    "oh no",
    "dang"
]

jump_of_ladder = [
    "woohoo",
    "woww",
    "nailed it",
    "oh my God...",
    "yaayyy",
]


def welcome_msg():
    msg = """
    Welcome to Snake and Ladder Game --->
    Rules:
      1. The board will have 100 cells numbered from 1 to 100.
      2. The game will have a six sided dice numbered from 1 to 6 and will always give a random number on rolling it.
      3. Each player has a piece which is initially kept outside the board (i.e., at position 0).
      4. Each player rolls the dice when their turn comes.
      5. Based on the dice value, the player moves their piece forward that number of cells. Ex: If the dice value is 5 and the piece is at position 21, the player will put their piece at position 26 now (21+5).
      6. A player wins if it exactly reaches the position 100 and the game ends there.
      7. After the dice roll, if a piece is supposed to move outside position 100, it does not move.
      8. The board also contains some snakes and ladders.
      9. Each snake will have its head at some number and its tail at a smaller number.
      10. Whenever a piece ends up at a position with the head of the snake, the piece should go down to the position of the tail of that snake.
      11. Each ladder will have its start position at some number and end position at a larger number.
      12. Whenever a piece ends up at a position with the start of the ladder, the piece should go up to the position of the end of that ladder.
      13. There could be another snake/ladder at the tail of the snake or the end position of the ladder and the piece should go up/down accordingly.
    """
    print(msg)


def player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter a name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter a name for second player: ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name


def get_dice_value():
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    dice_value = random.randint(1, DICE_FACE)
    print("Its a " + str(dice_value))
    return dice_value


def got_bite_of_snake(old_value, present_value, player_name):
    print("\n" + random.choice(bite_of_snake).upper() + " ~~~~~~~~?")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(present_value))


def lad_jump(old_value, present_value, player_name):
    print("\n" + random.choice(jump_of_ladder).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(present_value))


def snake_ladder(player_name, present_value, dice_value):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    old_value = present_value
    present_value = present_value + dice_value

    if present_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(present_value))
    if present_value in s:
        final_value = s.get(present_value)
        got_bite_of_snake(present_value, final_value, player_name)

    elif present_value in l:
        final_value = l.get(present_value)
        lad_jump(present_value, final_value, player_name)

    else:
        final_value = present_value

    return final_value


def check_win(player_name, position):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game.\n")
        sys.exit(1)


def start():
    welcome_msg()
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    player1_name, player2_name = player_names()
    time.sleep(SLEEP_BETWEEN_ACTIONS)

    player1_current_position = 0
    player2_current_position = 0

    while True:
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        input_1 = input("\n" + player1_name + ": " + random.choice(turn_of_player) + " Hit enter to roll the dice: ")
        print("\nDice is Rolling...")
        dice_value = get_dice_value()
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        print(player1_name + " is moving....")
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

        check_win(player1_name, player1_current_position)

        input_2 = input("\n" + player2_name + ": " + random.choice(turn_of_player) + " Hit enter to roll the dice: ")
        print("\nDice is Rolling...")
        dice_value = get_dice_value()
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        print(player2_name + " is moving....")
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

        check_win(player2_name, player2_current_position)


if __name__ == "__main__":
    start()