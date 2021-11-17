class Board:
    def __init__(self, nrows, ncols):
        self._nrows = nrows
        self._ncols = ncols
        self._board = [' ' * self._ncols] * self._nrows
        self._winner = None

    def num_rows(self):
        return self._nrows

    def num_cols(self):
        return self._ncols

    def get_data(self):
        return self._board

    def drop_piece(self, col, piece):
        if col < 1 or col > self._ncols:
            return 'ERROR: Column number out of range'
        col -= 1
        for r in range(0, self._nrows):
            if self._board[r][col] == ' ':
                new_row = self._board[r][0:col] + piece + self._board[r][col+1:self._ncols]
                self._board[r] = new_row
                return None
        return 'ERROR: Column is full'

    def check_winner(self):
        if self._winner is not None:
            return self._winner
        for r0 in range(0, self._nrows):
            for c0 in range(0, self._ncols):
                piece = self._board[r0][c0]
                if piece == ' ':
                    continue
                flag1 = flag2 = flag3 = flag4 = True
                for d in range(1, 4):
                    if r0 + d < self._nrows:
                        if not (c0 - d >= 0 and self._board[r0 + d][c0 - d] == piece):
                            flag1 = False
                        if not self._board[r0 + d][c0] == piece:
                            flag2 = False
                        if not (c0 + d < self._ncols and self._board[r0 + d][c0 + d] == piece):
                            flag3 = False
                    else:
                        flag1 = flag2 = flag3 = False
                    if not (c0 + d < self._ncols and self._board[r0][c0 + d] == piece):
                        flag4 = False
                if flag1 or flag2 or flag3 or flag4:
                    self._winner = piece
                    return self._winner
        return self._winner


def show_board(board):
    nrows = board.num_rows()
    ncols = board.num_cols()
    board_data = board.get_data()
    head = ''
    for c in range(0, ncols):
        head += '  ' + str(c + 1) + ' '
    print(head)
    sep = '+' + '---+' * ncols
    for r in range(nrows - 1, -1, -1):
        print(sep)
        row = '|'
        for c in range(0, ncols):
            row += ' ' + board_data[r][c] + ' |'
        print(row)
    print(sep)


def main():
    board = Board(6, 7)
    player_symbols = "XO"
    player = 0
    while board.check_winner() is None:
        show_board(board)
        ch = input('Player ' + player_symbols[player] + '. Enter column number (or q to quit): ').lower()
        if ch[0] == 'q':
            return
        column = int(ch)
        err_msg = board.drop_piece(column, player_symbols[player])
        if err_msg is not None:
            print(err_msg)
        else:
            player = (player + 1) % 2
    if board.check_winner() is not None:
        show_board(board)
        print('Player ' + board.check_winner() + ' wins.')


if __name__ == '__main__':
    main()
