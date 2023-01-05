# Entrypoint of the program

from board import *
from pieces import *
from player import *


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