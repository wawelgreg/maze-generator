#!/usr/bin/python
import logging as log
import curses
import time

WALL = '\xe2'
DIG_GUY = 'O'
MAZE_WIDTH = -1
MAZE_HEIGHT = -1
FRAME_SLEEP = 5

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
                rows_l = 3
        elif rows_l % 2 == 0:
                rows_l += 1

        if cols_l < 3:
                cols_l = 3
        elif cols_l % 2 == 0:
                cols_l += 1

	# Fill maze with walls
	maze_matrix = []
	for r in range(rows_l):
		maze_matrix.append([wall for c in range(cols_l)])

	# Draw maze to pad
	pad.erase()
	draw(maze_matrix)
	pad.refresh(0,0, 0,0, curses.LINES-1,curses.COLS-1)
	time.sleep(FRAME_SLEEP)


def func(scr):
	maze_generation(MAZE_HEIGHT, MAZE_WIDTH, WALL)

if __name__ == "__main__":
	log.info("<<<Running maze generator independently.>>>")
	curses.wrapper(func)
