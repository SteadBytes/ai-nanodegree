"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random
import math


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def heuristic_decorator(func):
    """ Checks if a game has been won or lost for the given state and returns
    +inf/-inf accordingly before using a heuristic function as heuristic not
    used on terminal game states.
    Args:
        func: Heuristic in form heuristic_func(game,player,*args,**kwargs)
    """
    # Would use functools.wraps but imports not allowed in project grading
    def wrapper(game, player, *args, ** kwargs):
        win_loss_utility = game.utility(player)
        # game.utility() returns 0 if game is not won or lost
        if win_loss_utility != 0:
            return win_loss_utility
        else:
            # game still in progress -> use heuristic to determine value
            return func(game, player, *args, **kwargs)
    return wrapper


@heuristic_decorator
def moves_difference_score(game, player):
    """ Value of game board = difference between number of moves for each player
    More moves current player has, the better.

    Args:
        game (obj:`isolation.Board`): An instance of `isolation.Board` encoding
        the current state of the game (e.g.player locations and blocked cells).

        player (obj):
            A player instance in the current game (one of the player objects
            `game.__player_1__` or `game.__player_2__`.)
    Returns:
        float : Heuristic value of current game state to the specified player.
    """
    own_moves = game.get_legal_moves(player)
    opp_moves = game.get_legal_moves(game.get_opponent(player))

    return float(len(own_moves) - len(opp_moves))


@heuristic_decorator
def chase_opponent_score(game, player):
    """ Rewards moves which minimize the distance between the current player
    and their opponent

    Returns the negation of the distance between players -> closer distance =
    higher value

    Args:
        game (obj:`isolation.Board`): An instance of `isolation.Board` encoding
        the current state of the game (e.g.player locations and blocked cells).

        player (obj):
            A player instance in the current game (one of the player objects
            `game.__player_1__` or `game.__player_2__`.)
    Returns:
        float : Heuristic value of current game state to the specified player.
    """
    own_loc = game.get_player_location(player)
    opp_loc = game.get_player_location(game.get_opponent(player))

    # first ply -> players not on board yet
    if own_loc is None or opp_loc is None:
        return 0

    dist = math.sqrt(pow(own_loc[0] + opp_loc[0], 2) +
                     pow(own_loc[1] + opp_loc[1], 2))
    return -dist


@heuristic_decorator
def weighted_chase_opponent_score(game, player):
    """ Rewards moves which minimize the distance between the current player
        and their opponent. Weighted more heavily towards the end of the game.

        Returns the negation of the distance between players:
        closer distance = higher value
    Args:
        game (obj:`isolation.Board`): An instance of `isolation.Board` encoding
        the current state of the game (e.g.player locations and blocked cells).

        player (obj):
            A player instance in the current game (one of the player objects
            `game.__player_1__` or `game.__player_2__`.)
    Returns:
        float : Heuristic value of current game state to the specified player.
    """
    weight = 1.0

    own_loc = game.get_player_location(player)
    opp_loc = game.get_player_location(game.get_opponent(player))

    # first ply -> players not on board yet
    if own_loc is None or opp_loc is None:
        return 0

    # < 1/4 blanks spaces = near end game
    if (len(game.get_blank_spaces()) / (game.width * game.height)) < 0.25:
        weight = 4

    dist = math.sqrt(pow(own_loc[0] + opp_loc[0], 2) +
                     pow(own_loc[1] + opp_loc[1], 2))
    return float(-dist / weight)


def get_moves(game, loc):
    """ Generates list of possible L-shaped moves from a specific location in
        a game state.
        Similar to Board.__get_moves() private method.

    Args:
        game (obj:`isolation.Board`): An instance of `isolation.Board` encoding
        the current state of the game (e.g.player locations and blocked cells).

        player (obj):
            A player instance in the current game (one of the player objects
            `game.__player_1__` or `game.__player_2__`.)
    Returns:
        list of `tuples`: (x,y) tuples of board positions
    """
    r, c = loc
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                  (1, -2), (1, 2), (2, -1), (2, 1)]
    valid_moves = [(r + dr, c + dc) for dr, dc in directions
                   if game.move_is_legal((r + dr, c + dc))]
    return valid_moves


@heuristic_decorator
def next_moves_score(game, player):
    """ Measures utility by difference in number of moves between the players
    weighted by the number of possible moves available in the next turn after
    making a move.

    Number of opponent moves = penalty
    Number of own moves = reward

    Args:
        game (obj:`isolation.Board`): An instance of `isolation.Board` encoding
        the current state of the game (e.g.player locations and blocked cells).

        player (obj):
            A player instance in the current game (one of the player objects
            `game.__player_1__` or `game.__player_2__`.)
    Returns:
        float : Heuristic value of current game state to the specified player.
    """
    own_moves = game.get_legal_moves(player)
    opp_moves = game.get_legal_moves(game.get_opponent(player))

    own_next_moves = set(
        [_m for move in own_moves for _m in get_moves(game, move)])
    opp_next_moves = set(
        [_m for move in opp_moves for _m in get_moves(game, move)])
    return float(len(own_next_moves) - len(opp_next_moves) +
                 len(own_moves) - len(opp_moves))


@heuristic_decorator
def avoid_corners_score(game, player):
    """ Same as moves_difference but penalises moves that put current player in
    the corners of the board and reward for moves that put opponent in corner

    Args:
        game (obj:`isolation.Board`): An instance of `isolation.Board` encoding
        the current state of the game (e.g.player locations and blocked cells).

        player (obj):
            A player instance in the current game (one of the player objects
            `game.__player_1__` or `game.__player_2__`.)
    Returns:
        float : Heuristic value of current game state to the specified player.
    """
    weight = 1.0
    own_loc = game.get_player_location(player)
    opp_loc = game.get_player_location(game.get_opponent(player))

    # first ply -> players not on board yet
    if own_loc is None or opp_loc is None:
        return 0

    own_moves = game.get_legal_moves(player)
    opp_moves = game.get_legal_moves(game.get_opponent(player))

    corners = [(0, 0), (0, game.width - 1), (game.height - 1, 0),
               (game.height - 1, game.width - 1)]
    own_corner_moves = [move for move in own_moves if move in corners]
    opp_corner_moves = [move for move in opp_moves if move in corners]

    total_penalty = len(own_corner_moves) * weight
    total_reward = len(opp_corner_moves) * weight

    return float((len(own_moves) - total_penalty) -
                 (len(opp_moves) + total_reward))


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    return avoid_corners_score(game, player)


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    return next_moves_score(game, player)


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    return weighted_chase_opponent_score(game, player)


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        moves = game.get_legal_moves()
        if len(moves) == 0:
            return (-1, -1)
        else:
            best_move = moves[0]

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        moves = game.get_legal_moves()

        if len(moves) == 0:
            return (-1, -1)
        else:
            best_move = moves[0]

        max_util = float("-inf")
        for move in moves:
            v = self.min_value(game.forecast_move(move), depth - 1)
            if v >= max_util:
                max_util = v
                best_move = move
        return best_move

    def min_value(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        moves = game.get_legal_moves()
        if depth == 0 or len(moves) == 0:
            return self.score(game, self)
        v = float("inf")
        for move in moves:
            v = min(v, self.max_value(game.forecast_move(move), depth - 1))
        return v

    def max_value(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        moves = game.get_legal_moves()
        if depth == 0 or len(moves) == 0:
            return self.score(game, self)
        v = float("-inf")
        for move in moves:
            v = max(v, self.min_value(game.forecast_move(move), depth - 1))
        return v


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        moves = game.get_legal_moves()
        if len(moves) == 0:
            return (-1, -1)
        else:
            best_move = moves[0]

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            d = 1
            while True:
                best_move = self.alphabeta(game, d)
                d += 1

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        moves = game.get_legal_moves()

        if len(moves) == 0:
            return (-1, -1)
        else:
            best_move = moves[0]

        max_util = float("-inf")
        for move in moves:
            v = self.min_value(game.forecast_move(move),
                               depth - 1, alpha, beta)
            if v > max_util:
                best_move = move
                max_util = v
            if v >= beta:
                return best_move
            alpha = max(alpha, v)
        return best_move

    def min_value(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        moves = game.get_legal_moves()
        if depth == 0 or len(moves) == 0:
            return self.score(game, self)

        v = float("inf")
        for move in moves:
            v = min(v, self.max_value(
                game.forecast_move(move), depth - 1, alpha, beta))

            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def max_value(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        moves = game.get_legal_moves()
        if depth == 0 or len(moves) == 0:
            return self.score(game, self)

        v = float("-inf")
        for move in moves:
            v = max(v, self.min_value(
                game.forecast_move(move), depth - 1, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
