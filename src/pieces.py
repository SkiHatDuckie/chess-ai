# Class definitions for chess pieces

from util import Position


class GamePiece:
    def __init__(self, position: Position, icon: str) -> None:
        self.position = position
        self.icon = icon

    #TODO!
    def can_move_to_postion(self, other_pieces: list, position: tuple) -> bool:
        pass

    # TODO!
    def move_piece(self, other_pieces: list) -> None:
        pass


class Pawn(GamePiece):
    def __init__(self, position: Position, icon: str) -> None:
        super().__init__(position, icon)

    def can_move_to_postion(self, other_pieces: list, position: tuple) -> bool:
        return super().can_move_to_postion(other_pieces, position)

    def move_piece(self, other_pieces: list) -> None:
        return super().move_piece(other_pieces)


class Knight(GamePiece):
    def __init__(self, position: Position, icon: str) -> None:
        super().__init__(position, icon)

    def can_move_to_postion(self, other_pieces: list, position: tuple) -> bool:
        return super().can_move_to_postion(other_pieces, position)

    def move_piece(self, other_pieces: list) -> None:
        return super().move_piece(other_pieces)


class Bishop(GamePiece):
    def __init__(self, position: Position, icon: str) -> None:
        super().__init__(position, icon)

    def can_move_to_postion(self, other_pieces: list, position: tuple) -> bool:
        return super().can_move_to_postion(other_pieces, position)

    def move_piece(self, other_pieces: list) -> None:
        return super().move_piece(other_pieces)


class Rook(GamePiece):
    def __init__(self, position: Position, icon: str) -> None:
        super().__init__(position, icon)

    def can_move_to_postion(self, other_pieces: list, position: tuple) -> bool:
        return super().can_move_to_postion(other_pieces, position)

    def move_piece(self, other_pieces: list) -> None:
        return super().move_piece(other_pieces)


class Queen(GamePiece):
    def __init__(self, position: Position, icon: str) -> None:
        super().__init__(position, icon)

    def can_move_to_postion(self, other_pieces: list, position: tuple) -> bool:
        return super().can_move_to_postion(other_pieces, position)

    def move_piece(self, other_pieces: list) -> None:
        return super().move_piece(other_pieces)


class King(GamePiece):
    def __init__(self, position: Position, icon: str) -> None:
        super().__init__(position, icon)

    def can_move_to_postion(self, other_pieces: list, position: tuple) -> bool:
        return super().can_move_to_postion(other_pieces, position)

    def move_piece(self, other_pieces: list) -> None:
        return super().move_piece(other_pieces)
