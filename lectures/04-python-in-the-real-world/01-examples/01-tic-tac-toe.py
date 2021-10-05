# Put your imports here

# Put your constants here
PLAYER_0 = 'X'
PLAYER_1 = 'O'
BOARD_SIZE = 5

# Functions
def print_board(board):
    for row in board:
        #print(row)
        for cell in row:
            print(cell + ' ', end='')
        print('\n')

def create_board():
   board = []
   for row in range(BOARD_SIZE):
      board.append(['-']*BOARD_SIZE)
   return board

# Main function
def main():

   board = create_board()

   player = PLAYER_0

   while True:
      print_board(board)
      row = int(input("Enter row: "))
      col = int(input("Enter col: "))
      board[row][col] = player
      if player == PLAYER_0:
         player = PLAYER_1
      else:
         player = PLAYER_0

# Code which gets executed at the start
if __name__ == '__main__':
   main()
