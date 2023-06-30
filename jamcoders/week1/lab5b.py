EMPTY_TILE = 0
X_PIECE = 1
O_PIECE = 2
NO_WINNER = "NO_WINNER"

def make_check_winner(seq):
    def check_winner(board):
        height = len(board)
        if height == 0:
            return NO_WINNER
        width = len(board[0])

        for row in range(height):
            for col in range(width):
                start = get_piece(board, row, col)
                for dr, dc in seq:
                    if not (0 <= row + dr < height):
                        break
                    if not (0 <= col + dc < width):
                        break
                    if start != get_piece(board, row + dr, col + dc):
                        break
                else:
                    if start != EMPTY_TILE:
                        return start
        return NO_WINNER
    return check_winner

def get_piece(board, row, column):
    """
    Retrieves the piece at the given row and column in the board.

    Args:
        board (list of list of int): 
            A 2D list representing the board and the pieces on it.
        row (int): 
            The row index of the piece to retrieve.
        column (int): 
            The column index of the piece to retrieve.
    """
    # YOUR CODE HERE
    return board[-row-1][column]