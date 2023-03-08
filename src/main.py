# Entrypoint of the program

import chess

WHITE = 1
BLACK = -1
PAWN_SCORE_TABLE = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0
]
KNIGHT_SCORE_TABLE = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]
BISHOP_SCORE_TABLE = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
]
ROOK_SCORE_TABLE = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0
]
QUEEN_SCORE_TABLE = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
]
KING_SCORE_TABLE = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
]


def evaluate_position(board: chess.Board) -> int:
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))

    material = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 \
               * (wr - br) + 900 * (wq - bq)
    pawnsq = sum(
        [PAWN_SCORE_TABLE[i]
         for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq = pawnsq + sum(
        [-PAWN_SCORE_TABLE[chess.square_mirror(i)]
         for i in board.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum(
        [KNIGHT_SCORE_TABLE[i]
         for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum(
        [-KNIGHT_SCORE_TABLE[chess.square_mirror(i)]
         for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq = sum(
        [BISHOP_SCORE_TABLE[i]
         for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq = bishopsq + sum(
        [-BISHOP_SCORE_TABLE[chess.square_mirror(i)]
         for i in board.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum(
        [ROOK_SCORE_TABLE[i] 
         for i in board.pieces(chess.ROOK, chess.WHITE)])
    rooksq = rooksq + sum(
        [-ROOK_SCORE_TABLE[chess.square_mirror(i)]
         for i in board.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum(
        [QUEEN_SCORE_TABLE[i]
         for i in board.pieces(chess.QUEEN, chess.WHITE)])
    queensq = queensq + sum(
        [-QUEEN_SCORE_TABLE[chess.square_mirror(i)]
         for i in board.pieces(chess.QUEEN, chess.BLACK)])
    kingsq = sum(
        [KING_SCORE_TABLE[i]
         for i in board.pieces(chess.KING, chess.WHITE)])
    kingsq = kingsq + sum(
        [-KING_SCORE_TABLE[chess.square_mirror(i)]
         for i in board.pieces(chess.KING, chess.BLACK)])

    score = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
    if board.turn:
        return score
    else:
        return -score


def quiesce(board, alpha, beta):
    stand_pat = evaluate_position(board)
    if (stand_pat >= beta):
        return beta
    if (alpha < stand_pat):
        alpha = stand_pat
    for move in board.legal_moves:
            if board.is_capture(move):
                board.push(move)
                score = -quiesce(board, -beta, -alpha)
                board.pop()
                if (score >= beta):
                    return beta
                if (score > alpha):
                    alpha = score
    return alpha
    

def alphabeta(board, alpha, beta, depth):
    bestscore = -9999
    if (depth == 0):
        return quiesce(board, alpha, beta)
    for move in board.legal_moves:
        board.push(move)
        score = -alphabeta(board, -beta, -alpha, depth - 1)
        board.pop()
        if (score >= beta):
            return score
        if (score > bestscore):
            bestscore = score
        if (score > alpha):
            alpha = score
    return bestscore


# Negamax is just different way of implementing minimax
def negamax(board: chess.Board, depth: int) -> chess.Move:
    bestMove = chess.Move.null()
    bestValue = -99999
    alpha = -100000
    beta = 100000
    for move in board.legal_moves:
        board.push(move)
        boardValue = -alphabeta(board, -beta, -alpha, depth - 1)
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        if (boardValue > alpha):
            alpha = boardValue
        board.pop()
    return bestMove


def get_human_player() -> bool:
    print("""Which piece would the human like to take?
For white press \"w\", for black press \"b\", then hit enter.""")

    choice = ""
    while True:
        choice = input("> ")
        if choice == "w":
            return 1
        elif choice == "b":
            return -1


def get_move(board: chess.Board) -> chess.Move:
    while True:
        try:
            move = board.parse_san(input("> "))
            return move
        except:
            print("Illeagal move!")


def check_outcome(board: chess.Board, who2move: int) -> int:
    if board.is_checkmate():
        return who2move
    elif board.is_stalemate() \
         or board.is_fivefold_repetition() \
         or board.is_seventyfive_moves():
        return 0
    else:
        return -2


if __name__ == "__main__":
    board = chess.Board()
    who2move = WHITE

    human_player = get_human_player()

    # -2 = not finished, -1 = win for black, 0 = draw, 1 = win for white
    outcome = -2
    while outcome == -2:
        print(board)
        if who2move == WHITE:
            print("White to move")
        else:
            print("Black to move")
        
        if who2move == human_player:
            move = get_move(board)
            print(move)
            board.push(move)
        else:
            move = negamax(board, 1)
            board.push(move)

        who2move = -who2move

        check_outcome(board, who2move)
