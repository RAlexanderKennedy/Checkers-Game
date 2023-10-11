import checkers


def game():
    try:
        current_size= int(input("What size would you like the board to be?"))
        current_board = checkers.build_board(current_size)
        print(current_board)
        print(f'There are {checkers.get_count(current_board, "Red")} red spaces')
        print(f'There are {checkers.get_count(current_board, "Black")} black spaces')
        print(f'There are {checkers.get_count(current_board, "Empty")} empty spaces')

    except ValueError:
        print("Invalid input. Please enter a valid board size (an integer).")


if __name__ == "__main__":
    game()
