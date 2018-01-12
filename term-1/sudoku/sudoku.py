
unsolved = ('..3.2.6..9..3.5..1..18.64....81.29..7' +
            '.......8..67.82....26.95..8..2.3..9..5.1.3..')
solved = ('483921657967345821251876493548132976729564' +
          '138136798245372689514814253769695417382')


def cross(A, B):
    """Cross product of elements in A and B
    """
    return [a + b for a in A for b in B]


empty_squares = [(x, y) for y in range(len(self.board))
                 for x in range(len(self.board[y])) if self.board[y][x] != 1]

digits = '123456789'
rows = 'ABCDEFGHI'
boxes = cross(rows, digits)
cols = digits

row_units = [cross(r, cols) for r in rows]
col_units = [cross(rows, c) for c in cols]
sq_unit = [cross(r_grp, c_grp) for r_grp in ('ABC', 'DEF', 'GHI')
           for c_grp in ('123', '456', '789')]
unit_list = row_units + col_units + sq_unit

units = {s: [unit for unit in unit_list if s in unit] for s in boxes}

peers = {s: set(sum(units[s], [])) - set([s]) for s in boxes}


def grid_values(grid_str):
    """Convert grid string into {<box>: <value>} dict with '123456789' value
    for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if empty
    """
    # values = []
    # all_digits = '123456789'
    # for c in grid:
    #     if c == '.':
    #         values.append(all_digits)
    #     elif c in all_digits:
    #         values.append(c)
    # assert len(values) == 81
    # return dict(zip(boxes, values))
    return {s: v if v != '.' else digits for s, v in zip(boxes, grid_str)}


def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    solved = [b for b in boxes if len(values[b]) == 1]
    print(solved)
    for b in solved:
        for p in peers[b]:
            values[p] = values[p].replace(values[b], '')
    return values


def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for unit in unit_list:
        for d in '123456789':
            possible_boxes = [b for b in unit if d in values[b]]
            if len(possible_boxes) == 1:
                print(possible_boxes)
                values[possible_boxes[0]] = d
    return values


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len(
            [box for box in values.keys() if len(values[box]) == 1])

        values = eliminate(values)
        values = only_choice(values)
        # Check how many boxes have a determined value
        solved_values_after = len(
            [box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    max_box_width = max(len(values[b]) for b in boxes) + 1
    for i in range(len(row_units)):
        row = ''.join(values[b].center(max_box_width) for b in row_units[i])
        row = ' | '.join(row[i:i + max_box_width * 3]
                         for i in range(0, len(row), max_box_width * 3))
        if i > 0 and i % 3 == 0:
            print('-' * len(row))

        print(row)


def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    values = reduce_puzzle(values)
    if values is False:
        return False  # Failed in reduce_puzzle
    if all(len(values[s]) == 1 for s in boxes):
        return values  # Solved
    # Square (not already determined) with fewest possibilities
    s = None
    for b in boxes:
        length = len(values[b])
        if length > 1:
            if s is None or length < len(values[s]):
                s = b

    for value in values[s]:
        new_grid = values.copy()
        new_grid[s] = value
        result = search(new_grid)
        if result:  # returns False unless solved
            return result


import json
import os
path = os.path.join(os.path.dirname(__file__), 'data.json')
inp = {'G7': '2345678', 'G6': '1236789', 'G5': '23456789', 'G4': '345678', 'G3': '1234569', 'G2': '12345678', 'G1': '23456789', 'G9': '24578', 'G8': '345678', 'C9': '124578', 'C8': '3456789', 'C3': '1234569', 'C2': '1234568', 'C1': '2345689', 'C7': '2345678', 'C6': '236789', 'C5': '23456789', 'C4': '345678', 'E5': '68', 'E4': '2', 'F1': '1', 'F2': '24', 'F3': '24', 'F4': '9', 'F5': '37', 'F6': '37', 'F7': '58', 'F8': '58', 'F9': '6', 'B4': '345678', 'B5': '23456789', 'B6': '236789', 'B7': '2345678', 'B1': '2345689', 'B2': '1234568', 'B3': '1234569', 'B8': '3456789', 'B9': '124578', 'I9': '9',
       'I8': '345678', 'I1': '2345678', 'I3': '23456', 'I2': '2345678', 'I5': '2345678', 'I4': '345678', 'I7': '1', 'I6': '23678', 'A1': '2345689', 'A3': '7', 'A2': '234568', 'E9': '3', 'A4': '34568', 'A7': '234568', 'A6': '23689', 'A9': '2458', 'A8': '345689', 'E7': '9', 'E6': '4', 'E1': '567', 'E3': '56', 'E2': '567', 'E8': '1', 'A5': '1', 'H8': '345678', 'H9': '24578', 'H2': '12345678', 'H3': '1234569', 'H1': '23456789', 'H6': '1236789', 'H7': '2345678', 'H4': '345678', 'H5': '23456789', 'D8': '2', 'D9': '47', 'D6': '5', 'D7': '47', 'D4': '1', 'D5': '36', 'D2': '9', 'D3': '8', 'D1': '36'}
out = {'G7': '2345678', 'G6': '1236789', 'G5': '23456789', 'G4': '345678', 'G3': '1234569', 'G2': '12345678', 'G1': '23456789', 'G9': '24578', 'G8': '345678', 'C9': '124578', 'C8': '3456789', 'C3': '1234569', 'C2': '1234568', 'C1': '2345689', 'C7': '2345678', 'C6': '236789', 'C5': '23456789', 'C4': '345678', 'E5': '68', 'E4': '2', 'F1': '1', 'F2': '24', 'F3': '24', 'F4': '9', 'F5': '37', 'F6': '37', 'F7': '58', 'F8': '58', 'F9': '6', 'B4': '345678', 'B5': '23456789', 'B6': '236789', 'B7': '2345678', 'B1': '2345689', 'B2': '1234568', 'B3': '1234569', 'B8': '3456789', 'B9': '124578', 'I9': '9',
       'I8': '345678', 'I1': '2345678', 'I3': '23456', 'I2': '2345678', 'I5': '2345678', 'I4': '345678', 'I7': '1', 'I6': '23678', 'A1': '2345689', 'A3': '7', 'A2': '234568', 'E9': '3', 'A4': '34568', 'A7': '234568', 'A6': '23689', 'A9': '2458', 'A8': '345689', 'E7': '9', 'E6': '4', 'E1': '567', 'E3': '56', 'E2': '567', 'E8': '1', 'A5': '1', 'H8': '345678', 'H9': '24578', 'H2': '12345678', 'H3': '1234569', 'H1': '23456789', 'H6': '1236789', 'H7': '2345678', 'H4': '345678', 'H5': '23456789', 'D8': '2', 'D9': '47', 'D6': '5', 'D7': '47', 'D4': '1', 'D5': '36', 'D2': '9', 'D3': '8', 'D1': '36'}
display(inp)
