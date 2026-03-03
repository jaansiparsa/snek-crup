import curses
from typing import Optional


class SnakeGame:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        cx = width // 2
        cy = height // 2
        self.body = [(cy, cx - 2), (cy, cx - 1), (cy, cx)]
        self.dx = 0
        self.dy = 0
        self.next_dx = 1
        self.next_dy = 0

    def grid(self) -> list[list[str]]:
        out = []
        out.append(["+"] + ["-"] * self.w + ["+"])
        inner = [[" " for _ in range(self.w)] for _ in range(self.h)]
        for y, x in self.body:
            if 0 <= y < self.h and 0 <= x < self.w:
                inner[y][x] = "#"
        for row in inner:
            out.append(["|"] + row + ["|"])
        out.append(["+"] + ["-"] * self.w + ["+"])
        return out

    def set_direction(self, key_input: Optional[str]):
        if key_input == "d":
            self.next_dx, self.next_dy = 1, 0
        elif key_input == "a":
            self.next_dx, self.next_dy = -1, 0
        elif key_input == "w":
            self.next_dx, self.next_dy = 0, -1
        elif key_input == "s":
            self.next_dx, self.next_dy = 0, 1

    def do_step(self) -> bool:
        if self.next_dx != 0 or self.next_dy != 0:
            self.dx = self.next_dx
            self.dy = self.next_dy
        head_y, head_x = self.body[-1]
        ny = head_y + self.dy
        nx = head_x + self.dx
        if ny < 0 or ny >= self.h or nx < 0 or nx >= self.w:
            return False
        if (ny, nx) in self.body:
            return False
        self.body.append((ny, nx))
        self.body.pop(0)
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
