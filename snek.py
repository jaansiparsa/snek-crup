import curses
import random
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
        self.apple = None
        self._spawn_apple()

    def _spawn_apple(self):
        empty = [(y, x) for y in range(self.h) for x in range(self.w) if (y, x) not in self.body and (y, x) != self.apple]
        if empty:
            self.apple = random.choice(empty)

    def grid(self) -> list[list[str]]:
        out = []
        out.append(["+"] + ["-"] * self.w + ["+"])
        inner = [[" " for _ in range(self.w)] for _ in range(self.h)]
        for y, x in self.body:
            if 0 <= y < self.h and 0 <= x < self.w:
                inner[y][x] = "#"
        if self.apple:
            ay, ax = self.apple
            if 0 <= ay < self.h and 0 <= ax < self.w:
                inner[ay][ax] = "*"
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
        if self.apple and (ny, nx) == self.apple:
            self._spawn_apple()
        else:
            self.body.pop(0)
        return True


def game_loop(stdscr):
    game = SnakeGame(25, 15)
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(200)
    max_y, max_x = stdscr.getmaxyx()

    while True:
        key = stdscr.getch()
        key = chr(key) if 0 <= key < 256 else None

        game.set_direction(key)
        if not game.do_step():
            stdscr.clear()
            for y, row in enumerate(game.grid()):
                for x, char in enumerate(row):
                    if y < max_y and x < max_x:
                        stdscr.addch(y, x, ord(str(char)))
            gy, gx = game.h // 2 + 1, max(0, game.w // 2 - 4)
            if gy < max_y and gx + 9 < max_x:
                stdscr.addstr(gy, gx, "Game over!")
            stdscr.refresh()
            stdscr.nodelay(0)
            stdscr.getch()
            return

        stdscr.clear()
        for y, row in enumerate(game.grid()):
            for x, char in enumerate(row):
                if y < max_y and x < max_x:
                    stdscr.addch(y, x, ord(str(char)))
        stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(game_loop)
