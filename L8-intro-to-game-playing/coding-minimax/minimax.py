def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    return len(gameState.get_legal_moves()) == 0


def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return 1
    min_child = float("inf")
    for move in gameState.get_legal_moves():
        # use max_value as next move will be other player
        min_child = min(min_child, max_value(gameState.forecast_move(move)))
    return min_child


def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return -1
    max_child = float("-inf")
    for move in gameState.get_legal_moves():
        # use min_value as next move will be other player
        max_child = max(max_child, min_value(gameState.forecast_move(move)))
    return max_child


def minimax_decision(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.

    You can ignore the special case of calling this function
    from a terminal state.
    """
    max_score = float("-inf")
    best_move = None
    for move in gameState.get_legal_moves():
        score = min_value(gameState.forecast_move(move))
        if score > max_score:
            max_score = score
            best_move = move
    return best_move
#    return max(gameState.get_legal_moves(),
#                key=lambda m: min_value(gameState.forecast_move(m)))
