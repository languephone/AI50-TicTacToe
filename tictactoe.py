"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    # Count number of plays for each player
    x_count = 0
    o_count = 0
    for row in board:
        for column in row:
            if column == "X":
                x_count += 1
            elif column == "O":
                o_count += 1
            else:
                pass
    if x_count > o_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    options = set()

    # Add each empty board position to the set of options
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                options.add((i, j))

    return options


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Raise error if action violates rules
    if board[action[0]][action[1]] != EMPTY:
        raise IndexError
    
    # Create deep copy of board
    new_board = copy.deepcopy(board)

    # Place player marker at action location
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # 8 ways to win: all in a row, all in a column or 2 diagonals

    players = [X, O]
    
    for player in players:
        # Check for completed row
        for i in range(len(board)):
            if (
                board[i][0] == player and
                board[i][1] == player and
                board[i][2] == player
                ):
                return player
        # Check for completed column
        for j in range(len(board[0])):
            if (
                board[0][j] == player and
                board[1][j] == player and
                board[2][j] == player
                ):
                return player
        # Check diagonals
        if (
            board[0][0] == player and
            board[1][1] == player and
            board[2][2] == player
            ):
            return player
        if (
            board[0][2] == player and
            board[1][1] == player and
            board[2][0] == player
            ):
            return player 

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if not winner(board):
        # If any cells in board are EMPTY, game is still in progress
        for row in board:
            for column in row:
                if column is None:
                    return False

    # If there's no winner and no spaces are empty, the game must be over
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if player(board) == X:
        return maxvalue(board):
    if player(board) == O:
        return minvalue(board):


def minvalue(board):
    """
    Returns the minimum utility from the available options.
    """

    if terminal(board):
        return utility(board)

    min_utility = 2

    for action in actions(board):
        min_utility = min(min_utility, maxvalue(result(board, action)))
    return min_utility


def maxvalue(board):
    """
    Returns the maximum utility from the available options.
    """

    if terminal(board):
        return utility(board)

    max_utility = -2

    for action in actions(board):
        max_utility = max(max_utility, minvalue(result(board, action)))
    return max_utility


