import random

ROWS = ['A', 'B', 'C', 'D', 'E']
COLUMNS = ['1', '2', '3', '4', '5']
MAX_GUESSES = 10
NUM_SHIPS = 3

board = [[' ' for _ in COLUMNS] for _ in ROWS]
ship_locations = []
guessed_positions = set()

def print_board(reveal_ships=False):
    print("   " + " ".join(COLUMNS))
    for i, row in enumerate(board):
        row_label = ROWS[i]
        line = []
        for j, cell in enumerate(row):
            if reveal_ships and (i, j) in ship_locations and cell == ' ':
                line.append('S')
            else:
                line.append(cell)
        print(f"{row_label}  " + " ".join(line))

def place_ships():
    while len(ship_locations) < NUM_SHIPS:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if (row, col) not in ship_locations:
            ship_locations.append((row, col))

def parse_guess(guess):
    guess = guess.upper().strip()
    if guess == 'QUIT':
        return 'QUIT'
    if len(guess) < 2 or len(guess) > 3:
        return None
    row_char = guess[0]
    col_str = guess[1:]
    if row_char not in ROWS or col_str not in COLUMNS:
        return None
    row = ROWS.index(row_char)
    col = COLUMNS.index(col_str)
    return (row, col)

def check_guess(position):
    row, col = position
    if position in ship_locations:
        board[row][col] = 'X'
        return 'hit'
    else:
        board[row][col] = 'O'
        return 'miss'

def play_game():
    place_ships()
    guesses_remaining = MAX_GUESSES
    hits = 0

    print("Welcome to this Funny Game!")
    print("Enter coordinates (e.g., B3). Type 'quit' to exit.")
    print_board()

    while guesses_remaining > 0:
        guess_input = input(f"\nGuesses left: {guesses_remaining} > ")
        parsed = parse_guess(guess_input)
        if parsed == 'QUIT':
            print("\nYou quit the game.")
            break
        if parsed is None:
            print("Invalid input. Use A1 to E5.")
            continue
        if parsed in guessed_positions:
            print("You already guessed that spot.")
            continue
        guessed_positions.add(parsed)
        result = check_guess(parsed)
        if result == 'hit':
            hits += 1
            print("Hit!")
        else:
            print("Miss.")
        print_board()
        guesses_remaining -= 1
        if hits == NUM_SHIPS:
            print("Congratulations!\n")
            break
    else:
        print("Game Over. You've used all your guesses.")
    print("\nFinal board:")
    print_board(reveal_ships=True)

if __name__ == "__main__":
    play_game()
