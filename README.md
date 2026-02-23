# Snek — Assignment

Build a terminal Snake game in Python and practice Git workflow in **your own repo** (clone, commits, pull request, self-merge).

---

## Part 1: Git Workflow (Intro to Git)

As well as this being a great practical project, this assignment is also an introduction to Git. **Work in your own fork** (don’t push to the original assignment repo). Follow these steps:

1. **Fork the repo** (do this first):  
   On GitHub (or GitLab), fork this assignment repo to your account—or to your team’s org if you’re working as a group. All work (commits, branches, PRs) happens in **your fork**, not the original repo.

2. **Clone your fork**:
   ```bash
   git clone <your-fork-url>
   cd snek
   ```

3. **Make at least 3 commits** as you implement the game (or fix bugs, refactor, etc.).  
   - Use clear, descriptive commit messages (e.g. “Add snake movement and direction handling”, “Implement grid rendering”, “Handle game over on wall collision”).  
   - Commit logical units of work, not huge dumps of code.

4. **Good PR etiquette — open a Pull Request:**
   - Create a **branch** for your work (e.g. `git checkout -b feature/snake-game`).
   - Push your branch and open a **Pull Request** from your branch into `main` (or the default branch) **in your fork**.
   - Write a short PR description: what you implemented, any known limitations, and how to run the game.
   - Keep the PR focused (e.g. “Implement Snake game” or “Add game over logic”).

5. **Self-merge:**  
   Review your own PR (as if you were a teammate), then **merge** it yourself.  
   After merging, pull the latest `main` locally so your branch is up to date.

-- 

## Part 2: Implement the Snake Game

Complete the `SnakeGame` class in `snek.py` so that:

- **Initial state**
  - Snake has length 3.
  - Snake moves **right**.
  - Snake starts in the **center** of the grid.

- **Controls**  
  Use **W**, **A**, **S**, **D** to move up, left, down, and right.

- **Behavior**
  - `grid()` returns a 2D list of characters representing the current board (snake, walls, empty cells, etc.).
  - `set_direction(key_input)` updates direction from `w` / `a` / `s` / `d` (or `None` for no change).
  - `do_step()` advances the game by one tick. It should return `False` when the game ends (e.g. wall or self collision), and `True` otherwise.

The main loop in `game_loop()` is already set up: it creates a 25×15 game, reads keys, calls `set_direction` and `do_step`, and draws whatever `grid()` returns. Your job is to implement `SnakeGame` so the game runs correctly.

**Run the game:**

```bash
python snek.py
```
OR 

```bash
python3 snek.py
```

---

## Notes

- **Terminal size:** Make sure your terminal window is big enough to display the curses UI (the game uses a 25×15 grid; give it a bit of extra space so nothing gets clipped).
- **Rendering:** If the game shows garbled characters like `^^^^^^^^^$` in the **VSCode integrated terminal**, run `python snek.py` in a **regular terminal** (e.g. macOS Terminal, Windows Command Prompt, or Windows Terminal).
- **Dependencies:** Use only the Python standard library. No need to `pip install` anything for this assignment.
- **Windows:** If you’re on Windows, you may need to install `windows-curses` for the `curses` module:
  ```bash
  pip install windows-curses
  ```
- **Syntax / help:** Feel free to look up Python or `curses` syntax and examples online.
- **Working together:** You may work in a team. If you do: each team member must still make **at least 3 commits** and open their **own PR(s)**; and everyone must **review each teammate’s PR(s)** before they are merged.

---

## Summary Checklist

- [ ] Fork the assignment repo
- [ ] Clone **your fork**
- [ ] Implement `SnakeGame` so the game runs (initial state, controls, grid, step, game over)
- [ ] Make at least 3 commits with clear messages
- [ ] Create a branch and open a Pull Request (in your fork) with a short description
- [ ] Self-merge the PR and pull latest `main`
- [ ] Include a link to your repo in the .txt file you submit to Gradescope!

Happy coding!
