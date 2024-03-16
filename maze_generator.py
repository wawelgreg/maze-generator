#!/usr/bin/python
import logging as log
import curses
import time

WALL = '\xe2'
DIG_GUY = 'O'
MAZE_WIDTH, MAZE_HEIGHT = 10, 5
FRAME_SLEEP = 5
R_START, C_START = 1, 1

log.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s', level=log.DEBUG, filename='maze_gen.log', datefmt='%Y-%m-%dT%H:%M:%S%z')

stdscr = curses.initscr()
pad = curses.newpad(100,100)

def draw(m):
	log.debug("Drawing to pad")
	for ri, crow in enumerate(m):
		for ci, ccol in enumerate(crow):
			pad.addch(ri, ci, m[ri][ci])


def maze_generation(rows_l, cols_l, wall):
	# For cases if width|height too small
	# or not odd in side length.	
	if rows_l < 3:
		log.error("Maze height %r too small: setting height to 3", rows_l)
                rows_l = 3
        elif rows_l % 2 == 0:
		log.error("Maze height %r is even: setting height to %r", rows_l, rows_l+1)
                rows_l += 1

        if cols_l < 3:
		log.error("Maze width %r too small: setting width to 3", cols_l)
                cols_l = 3
        elif cols_l % 2 == 0:
		log.error("Maze width %r is even: setting width to %r", cols_l, cols_l+1)
                cols_l += 1

	# Fill maze with walls
	log.info("Filling maze matrix size: %rx%r with wall: %r", rows_l, cols_l, wall)
	maze_matrix = []
	for r in range(rows_l):
		maze_matrix.append([wall for c in range(cols_l)])
	log.info("Filled maze matrix generation success")

	log.info("Starting maze generation")
	stack = []
	rc, cc = R_START, C_START
	log.debug("START: Appending (r:%r, c:%r) to stack", rc, cc)
	stack.append((rc, cc))

	while len(stack) > 0:
		r_coord, c_coord = stack.pop()	
		log.debug("Popped (r:%r,c:%c) from stack", r_coord, c_coord)
		maze_matrix[r_coord][c_coord] = DIG_GUY
		
		# Draw maze to pad
		pad.erase()
		draw(maze_matrix)
		# Display pad to terminal
		pad.refresh(0,0, 0,0, curses.LINES-1,curses.COLS-1)
		
		time.sleep(FRAME_SLEEP)


def func(scr):
	maze_generation(MAZE_HEIGHT, MAZE_WIDTH, WALL)

if __name__ == "__main__":
	log.info("<<<Running maze generator independently.>>>")
	curses.wrapper(func)
