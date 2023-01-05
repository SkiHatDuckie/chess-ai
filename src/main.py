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


if __name__ == "__main__":
    chessboard = get_chessboard()
    # TODO:
    # player1 = get_player(player_num, player_type)
    # player2 = get_player(player_num, player_type)
    # curr_player = player1

    while True:
        print_chessboard(chessboard)
        break
        # TODO:
        # move = get_move(curr_player)
        # if ( is_legal_move(curr_player, move) ):
        #     move_piece(move)
        # if ( opponent_in_checkmate(curr_player, chessboard) ):
        #     print_checkmate_message(curr_player)
        #     end_game(winner)
        #     break
        # elif ( opponent_in_check(curr_player, chessboard) ):
        #     print_check_message(curr_player)
        # elif ( is_stalemate(curr_player, chessboard) ):
        #     print_stalemate_message()
        #     break