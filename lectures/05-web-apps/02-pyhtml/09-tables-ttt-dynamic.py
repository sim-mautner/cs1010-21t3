from pyhtml import html, head, body, title, table, tr, td

BOARD_SIZE = 5
def main():
    board = []
    for i in range(BOARD_SIZE):
        row = []
        for j in range(BOARD_SIZE):
            row.append('-')
        board.append(row)

    board[1][1] = 'X'
    board[1][0] = 'O'

    board_pyhtml_rows = []
    for row in board:
        row_pyhtml = []
        for cell in row:
            row_pyhtml.append(td(cell))
        board_pyhtml_rows.append(tr(row_pyhtml))

    my_html = html(
        table(board_pyhtml_rows)
    )

    print(my_html)



if __name__ == "__main__":
    main()