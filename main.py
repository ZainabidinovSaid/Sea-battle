import os
import random

class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0

class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[' ' for _ in range(7)] for _ in range(7)]
        self.ships = [Ship(3), Ship(2), Ship(2), Ship(1), Ship(1), Ship(1), Ship(1)]
        self.shots = set()        

def print_board(board):
    print("   A B C D E F G")
    print("  ----------------")
    for i in range(7):
        print(f"{i + 1}|", end=" ")
        for j in range(7):
            print(board[i][j], end=" ")
        print()  

def place_ship(board, ship):
    placed = False
    while not placed:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            start_col = random.randint(0, 6 - ship.size)
            start_row = random.randint(0, 6)
            if all(board[start_row][start_col + i] == ' ' for i in range(ship.size)):
                for i in range(ship.size):
                    board[start_row][start_col + i] = str(ship.size)
                placed = True
        else:
            start_col = random.randint(0, 6)
            start_row = random.randint(0, 6 - ship.size)
            if all(board[start_row + i][start_col] == ' ' for i in range(ship.size)):
                for i in range(ship.size):
                    board[start_row + i][start_col] = str(ship.size)
                placed = True              

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')        