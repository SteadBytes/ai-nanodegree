from copy import deepcopy

width = 3
height = 2


class GameState:

    def __init__(self):
        self.board = [[0] * width for i in range(height)]
        # bottom right corner blocked
        self.board[-1][-1] = 1
        self.active_player = 0
        self.player_locs = [None, None]

    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.

        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
        """
        new_state = deepcopy(self)

        new_state.player_locs[self.active_player] = move
        new_state.board[move[1]][move[0]] = 1

        # change to other player
        new_state.active_player ^= 1
        return new_state

    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """
        player_pos = self.player_locs[self.active_player]
        empty_squares = [(x, y) for y in range(len(self.board))
                         for x in range(len(self.board[y])) if self.board[y][x] != 1]
        # first turn
        if player_pos is None:
            return empty_squares

        move_vectors = [(1, 0), (1, -1), (0, -1), (-1, -1),
                        (-1, 0), (-1, -1), (0, 1), (1, 1)]
        legal_moves = []
        for vx, vy in move_vectors:
            x = player_pos[0]
            y = player_pos[1]
            while 0 <= x + vx < width and 0 <= y + vy < height:
                x += vx
                y += vy
                if self.board[y][x] == 1:
                    break
                legal_moves.append((x, y))
        return legal_moves
