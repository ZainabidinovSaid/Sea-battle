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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')        