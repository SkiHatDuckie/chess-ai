class Position:
    def __init__(self, x: int, y: int) -> None:
        """Defines a position on the chessboard. Where (0,0) points to the
        top left."""
        self.x = x
        self.y = y