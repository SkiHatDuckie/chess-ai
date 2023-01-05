# Code related to the chessboard

def get_fen(fen):
    return fen.split("/")


def get_chessboard():
    fen = get_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBKQBNR")
    fen_length = len(fen)

    chessboard = []
    for line in range(0, fen_length):
        if fen[line].isdigit():
            chessboard.append(list(iter(" " * int(fen[line]))))
        else:
            chessboard.append(list(iter(fen[line])))

    return chessboard


def print_chessboard(chessboard):
    for row in range(len(chessboard)):
        row_str = ""
        for col in range(len(chessboard[row])):
            if col > 0:
                row_str += "|"
            row_str += chessboard[row][col]
        print(row_str)

        if row < len(chessboard - 1):
            print("-" * (len(chessboard[row]) * 2 - 1))


def search_position(pos, chessboard):
    pos = list(pos)
    cols = "abcdefgh"
    rows = "87654321"
    x = pos[0] in cols
    y = pos[1] in rows

    return chessboard[y][x]