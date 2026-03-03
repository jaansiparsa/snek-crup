import curses
from typing import Optional


class SnakeGame:
    def __init__(self, width: int, height: int):
        """
        Game should be initialized according to width
        and height. The game is played using wasd keys.

        The initial state should be:
        - Snake of length 3
        - Snake moving right
        - Snake in the center
        """
        self.width = width
        self.height = height

        self.direction = (1, 0)

        center_x = width // 2
        center_y = height // 2

        self.snake = [
            (center_x - 2, center_y),
            (center_x - 1, center_y),
            (center_x, center_y),
        ]

        self.alive = True

    def grid(self) -> list[list[str]]:
        """
        Handles the display of the grid
        Should return a 2D list of characters
        """
        board = []

        for y in range(self.height):
            row = []
            for x in range(self.width):
                if (x, y) in self.snake:
                    row.append("O")
                else:
                    row.append(" ")
            board.append(row)

        return board

    def set_direction(self, key_input: Optional[str]):
        """
        Set the direction.
        Assume input will either be w, a, s, d, or None
        """
        if key_input is None:
            return

        new_direction = None

        if key_input.lower() == "w":
            new_direction = (0, -1)
        elif key_input.lower() == "s":
            new_direction = (0, 1)
        elif key_input.lower() == "a":
            new_direction = (-1, 0)
        elif key_input.lower() == "d":
            new_direction = (1, 0)

        if new_direction is None:
            return

        # Prevent reversing direction
        dx, dy = self.direction
        ndx, ndy = new_direction

        if (dx + ndx, dy + ndy) != (0, 0):
            self.direction = new_direction

    def do_step(self) -> bool:
        """
        Performs a single step during 1 tick
        Return False if the game should end
        """

        if not self.alive:
            return False

        head_x, head_y = self.snake[-1]
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)

        # Check wall collisio
        if (
            new_head[0] < 0
            or new_head[0] >= self.width
            or new_head[1] < 0
            or new_head[1] >= self.height
        ):
            self.alive = False
            return False

        if new_head in self.snake:
            self.alive = False
            return False

        self.snake.append(new_head)
        self.snake.pop(0)

        return True


def game_loop(stdscr):
    """
    Main game loop that manages game setup and execution.
    """
    game = SnakeGame(25, 15)

    # Game setup
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(400)

    # Game loop
    while True:
        key = stdscr.getch()
        key = chr(key) if 0 <= key < 256 else None

        game.set_direction(key)
        if not game.do_step():
            print("Game over!")
            return

        stdscr.clear()

        # Draw grid
        for y, row in enumerate(game.grid()):
            for x, char in enumerate(row):
                stdscr.addch(y, x, ord(str(char)))

        # Refresh screen
        stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(game_loop)
