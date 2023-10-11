if __name__ == '__main__':
    print("This is not intended to be run as main")
from numpy import random

# Function to create a checker board of a given size, occupying each space randomly as either red, black, or empty
def build_board(size):
    board = random.choice(['Empty', 'Red', 'Black'], size = (size,size))
    return board

# Function to count spaces on a given board of a given type
def get_count(board, color):
    return (board == color).sum()

