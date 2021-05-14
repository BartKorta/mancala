from field import Board
import random


def run_test(amount):
    for i in range(amount):
        b = Board()
        randomize_board(b)
        b.print_board()
        b.ai_simulation(random.randint(2, 3), 1)
    print("Test passed.")


def randomize_board(board):
    for i in board.get_fields():
        i.stones = random.randint(0, 10)

