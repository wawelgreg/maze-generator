# Maze Generator

Simple visualized maze generation program.

![Screenshot 2024-03-19 213021](https://github.com/wawelgreg/maze-generator/assets/141285799/4e23b6e8-3f2f-486b-8a17-8dd2ac0c69f4)

## Info

- Meant to be run in shell/terminal.
- Uses Python [Curses](https://docs.python.org/3/howto/curses.html).

## Background

This maze generator utilizes an iterative version of the recursive backtracker
algorithm, which is a randomized version of the depth-first search algorithm.
Originally deveoloped with recursion, the program would reach max depth of recursion, therefore,
the *maze_generation()* function had to be implemented with a stack.

The steps of the *maze_generation()* function are as follows:
- Start at the initial cell (designated by R_START, C_START)
- Push these coordinates to the stack
  - While length of stack is not empty
      - Pop coordinates from stack
      - For each direction 2 units from the coordinate:
          - If coordinate found is in the maze and WALL exists:
              - Push the previously popped coordinates to stack
              - Bore hole between previous coordinate and new found coordinate
              - Push new found coordinate to stack
              - Break

## Usage

To run, call the executable python file from the command line:
```
./maze_generator.py
```

The constants at the top of the file can be modified as you please:

```python
WALL = '\xe2'
DIG_GUY = 'O'
MAZE_WIDTH, MAZE_HEIGHT = 50, 25
FRAME_SLEEP, END_SLEEP = 0.1, 2
R_START, C_START = 1, 1
```

*WALL*: char: This variable is what fills the pathless maze matrix before
            any actual maze path generation takes place.

*DIG_GUY*: char: This is the visual marker of the current location on the
            path stack in the maze matrix.

*MAZE_WIDTH, MAZE_HEIGHT*: int: These integers (corresponding to the maze
            matrix row and column dimensions) should be less than the
            *curses.newpad(nlines, ncols)* data structure dimensions.

*FRAME_SLEEP*: float: This number value corresponds to the wait time between
            frame. Pretty much a tickrate of sorts. A higher value
            will result in slower progression of maze generation.
            (1 = One second)      

*END_SLEEP*: float: This number value corresponds to the duration of display of
            the final resulting generated maze before automatic closing of
            the curses wrapper() function and program closing.
            (1 = One second)

*R_START, C_START*: int: These two integers correspond to the row and column
            coordinates of the start of the maze path generation. These
            values should be 0 or positive and less than the set maze width
            and height.
