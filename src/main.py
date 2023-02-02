# Entrypoint of the program

from board import *
from pieces import *
from player import *


if __name__ == "__main__":
    chessboard = Chessboard()
    chessboard.add_piece(King(Position(4, 7), "K"))
    chessboard.add_piece(King(Position(4, 0), "k"))
    chessboard.add_piece(Queen(Position(3, 7), "Q"))
    chessboard.add_piece(Queen(Position(3, 0), "q"))
    for i in range(2):
        chessboard.add_piece(Bishop(
            Position(2 + i * 3, 7),
            "B{}".format(i + 1)
        ))
        chessboard.add_piece(Bishop(
            Position(2 + i * 3, 0),
            "b{}".format(i + 1)
        ))
        chessboard.add_piece(Knight(
            Position(1 + i * 5, 7),
            "N{}".format(i + 1)
        ))
        chessboard.add_piece(Knight(
            Position(1 + i * 5, 0),
            "n{}".format(i + 1)
        ))
        chessboard.add_piece(Rook(
            Position(i * 7, 7),
            "R{}".format(i + 1)
        ))
        chessboard.add_piece(Rook(
            Position(i * 7, 0),
            "r{}".format(i + 1)
        ))
    for i in range(8):
        chessboard.add_piece(Pawn(Position(i, 6), "P{}".format(i + 1)))
        chessboard.add_piece(Pawn(Position(i, 1), "p{}".format(i + 1)))

    # TODO:
    # player1 = get_player(player_num, player_type)
    # player2 = get_player(player_num, player_type)
    # curr_player = player1

    while True:
        chessboard.print_chessboard()
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