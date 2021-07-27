from typing import Dict, Iterable, List, Set, Tuple

WHITE, BLACK, NONE = 'W', 'B', ' '


class Board:
    """
    Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board: List[str]):
        self.board = [list(row) for row in board]
        assert all(len(row) == len(self.board[0]) for row in self.board)

    def stone(self, point: Tuple[int]) -> str:
        '''Find stone (or lack thereof) at coordinates of point'''
        return self.board[point[1]][point[0]]

    def territory(self, x: int, y: int) -> Tuple[str, Set[Tuple[int]]]:
        """
        Find the owner and the territories given a coordinate on
        the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """

        def valid(point: Tuple[int]) -> bool:
            '''Check if given coordinates correspond to valid point on board'''
            return (0 <= point[0] < len(self.board[0])
                    and 0 <= point[1] < len(self.board))

        def neighbours(x: int, y: int) -> Iterable[Tuple[int]]:
            '''Return all valid surrounding points of point (x, y)'''
            neighbours = ((x, y+1),
                          (x, y-1),
                          (x+1, y),
                          (x-1, y))
            return (point for point in neighbours if valid(point))

        point = (x, y)
        if not valid(point):
            raise ValueError("Point must be on the board.")
        if self.stone(point) != NONE:
            return NONE, set()

        ownership, stack, territory = set(), [point], {point}
        while stack:
            x, y = stack.pop()
            for point in neighbours(x, y):
                if (stone := self.stone(point)) in (BLACK, WHITE):
                    ownership.add(stone)
                elif point not in territory:
                    stack.append(point)
                    territory.add(point)

        return ownership.pop() if len(ownership) == 1 else NONE, territory

    def territories(self) -> Dict[str, Set[Tuple[int]]]:
        """
        Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        territories = {owner: set() for owner in (BLACK, WHITE, NONE)}
        for y, row in enumerate(self.board):
            for x, _ in enumerate(row):
                if self.board[y][x] == NONE:
                    owner, territory = self.territory(x, y)
                    territories[owner].update(territory)
        return territories
