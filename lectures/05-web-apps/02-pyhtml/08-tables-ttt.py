from pyhtml import html, head, body, title, table, tr, td

BOARD_SIZE = 3

def main():
    board = []
    for i in range(BOARD_SIZE):
        row = []
        for j in range(BOARD_SIZE):
            row.append('-')
        board.append(row)

    board[1][1] = 'X'
    board[1][0] = 'O'

    my_html = html(
        table(
            tr(
                td(board[0][0]), td(board[0][1]), td(board[0][2])
            ),
            tr(
                td(board[1][0]), td(board[1][1]), td(board[1][2])
            ),
            tr(
                td(board[2][0]), td(board[2][1]), td(board[2][2])
            )
        )
    )

    print(my_html)



if __name__ == "__main__":
    main()