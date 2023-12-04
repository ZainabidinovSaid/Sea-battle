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
    ships = [(3, 's'), (2, 'm'), (2, 'm'), (1, 's'), (1, 's'), (1, 's'), (1, 's')]

    board = [['O' for _ in range(7)] for _ in range(7)]

    def is_valid_placement(x, y, size, orientation, board):
        def is_clear(x, y):
            if 0 <= x < 7 and 0 <= y < 7 and board[y][x] == 'O':
                return True
            return False 

        def is_clear_around(x, y):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < 7 and 0 <= y + j < 7:
                        if board[y + j][x + i] != 'O':
                            return False
            return True

        if orientation == 'horizontal':
            for i in range(size):
                if not is_clear(x + i, y) or not is_clear_around(x + i, y):
                    return False
        else:  # Vertical
            for i in range(size):
                if not is_clear(x, y + i) or not is_clear_around(x, y + i):
                    return False

        return True

    for size, symbol in ships:
        while True:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                x = random.randint(0, 6 - size)
                y = random.randint(0, 6)
            else:
                x = random.randint(0, 6)
                y = random.randint(0, 6 - size)

            if is_valid_placement(x, y, size, orientation, board):
                for i in range(size):
                    if orientation == 'horizontal':
                        board[y][x + i] = symbol
                    else:
                        board[y + i][x] = symbol
                break

    return board
            

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 

def main():
    clear_screen()
    
    player_name = input("Enter your name: ")
    shots = 0

    while True:
        clear_screen()
        print(f"Player: {player_name}\n")
        board = place_ships()
        hidden_board = [['O' for _ in range(7)] for _ in range(7)]

        while True:
            clear()
            print_board(hidden_board)
            row, col = get_shot()

            if hidden_board[row][col] != 'O':
                print("You've already shot at this location. Try again.")
                continue

            shots += 1

            if board[row][col] != 'O':
                print("Hit!")
                hidden_board[row][col] = 'X'
            else:
                print("Miss!")
                hidden_board[row][col] = 'L'

                

if __name__ == "__main__":
    main()