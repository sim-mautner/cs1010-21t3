# Put your imports here

# Put your constants here

# Functions
def print_board(board):
    for row in board:
        #print(row)
        for cell in row:
            print(cell + ' ', end='')
        print('\n')

# Main function
def main():
   board = [['-','-','-'],
            ['-','-','-'],
            ['-','-','-']]

   player = 'X'
   while True:
      print_board(board)
      row = int(input("Enter row: "))
      col = int(input("Enter col: "))
      board[row][col] = player
      if player == 'X':
         player = 'O'
      else:
         player = 'X'


# Code which gets executed at the start
if __name__ == '__main__':
   main()