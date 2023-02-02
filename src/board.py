# Code related to the chessboard

from pieces import GamePiece
from util import Position


class Chessboard:
    def __init__(self) -> None:
        self.size = 8
        self.board = [["" for _ in range(self.size)] for _ in range(self.size)]
        self.pieces = []

    def add_piece(self, new_piece: GamePiece):
        """New pieces need to have a unique icon and a position that is not
        already taken."""

        for piece in self.pieces:
            if piece.icon == new_piece.icon:
                raise RuntimeError(
                    "Error: Piece icon '{}' already being used in chessboard."
                    .format(new_piece.icon)
                )
            elif self.board[new_piece.position.y][new_piece.position.x] != "":
                raise RuntimeError(
                    "Error: Piece position '({x}, {y})' already being used \
                            in chessboard."
                    .format(
                        x=new_piece.position.x,
                        y=new_piece.position.y
                    )
                )

        self.pieces.append(new_piece)
        self.board[new_piece.position.y][new_piece.position.x] = new_piece.icon

    def search_position(self, position: Position):
        return self.board[position.y][position.x]

    def print_chessboard(self):
        for row in range(len(self.board)):
            row_str = ""
            for col in range(len(self.board[row])):
                if col > 0:
                    row_str += "|"
                row_str += "{0:2}".format(self.board[row][col])
            print(row_str)

            if row < len(self.board) - 1:
                print("-" * len(row_str))