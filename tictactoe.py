"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def flatten(array):
    """
    This function is used to flatten the array.
    :param array: 
    :return: 
    """
    out = []
    for i in array:
        out.extend(i)
    return out
    

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
    # I guess we just check who has more of things on the board. So if it is X then O will take
    # the turn else X wll take the turn.

    # if it is the initial state return X
    if board == initial_state():
        return X
    # else check who has played more turns
    flattened = flatten(board)
    if flattened.count(X) > flattened.count(O):
        return O
    return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                actions.add((i, j))
    return actions
                

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # making a deep copy of the board so that the recursive MiniMax does not harm the board.
    board_copy = copy.deepcopy(board)
    # now we need to check, whose turn it actually is.
    # and then we will simply make that move!
    board_copy[action[0]][action[1]] = player(board_copy)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # this has to be done the long way I guess. But that is fine!
    # check for winning of X
    if (
            board[0][0] == X and board[0][1] == X and board[0][2] == X) or (
            board[1][0] == X and board[1][1] == X and board[1][2] == X) or (
            board[2][0] == X and board[2][1] == X and board[2][2] == X) or (

            board[0][0] == X and board[1][0] == X and board[2][0] == X) or (
            board[0][1] == X and board[1][1] == X and board[2][1] == X) or (
            board[0][2] == X and board[1][2] == X and board[2][2] == X) or (

            board[0][0] == X and board[1][1] == X and board[2][2] == X) or (
            board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    elif (
            board[0][0] == O and board[0][1] == O and board[0][2] == O) or (
            board[1][0] == O and board[1][1] == O and board[1][2] == O) or (
            board[2][0] == O and board[2][1] == O and board[2][2] == O) or (

            board[0][0] == O and board[1][0] == O and board[2][0] == O) or (
            board[0][1] == O and board[1][1] == O and board[2][1] == O) or (
            board[0][2] == O and board[1][2] == O and board[2][2] == O) or (

            board[0][0] == O and board[1][1] == O and board[2][2] == O) or (
            board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # so basically first you have to check if someone has won or not.
    if winner(board) in (X, O):
        return True
    # or else you return True if there are no empty cells which are left on the board which is still a terminal state
    return flatten(board).count(EMPTY) == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) == X else -1 if winner(board) == O else 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # if the board is in the terminal state which means either player has won or it is a tie return none
    if terminal(board):
        return None

    def max_value(board):
        v = -math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        v = math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    # from what i can understand X is the maximising player.
    # if it is the maximising players turn
    if player(board) == X:
        # The maximizing player picks action a in Actions(s) that produces the highest value of Min-Value(Result(s, a)).
        outputs = {
            min_value(result(board, action)): action
            for action in actions(board)
        }
        maximum = max(outputs.keys())
        return outputs[maximum]
    else:
        # The minimizing player picks action a in Actions(s) that produces the lowest value of Max-Value(Result(s, a)).
        outputs = {
            max_value(result(board, action)): action
            for action in actions(board)
        }
        minimum = min(outputs.keys())
        return outputs[minimum]
