#!/usr/bin/python
import logging as log
import curses
import time

WALL = '\xe2'
FRAME_SLEEP = 5

log.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s', level=log.DEBUG, filename='maze_gen.log', datefmt='%Y-%m-%dT%H:%M:%S%z')

stdscr = curses.initscr()
pad = curses.newpad(100,100)

# Temp: Testing curses
m = []
for r in range(5):
	m.append([WALL for c in range(5)])

def draw(matrix):
	log.debug("Drawing to pad")
	for ri, rm in enumerate(matrix):
		for ci, cm in enumerate(matrix):
			pad.addch(ri, ci, matrix[ri][ci])

def func(scr):
	pad.erase()
	draw(m)
	pad.refresh(0,0, 0,0, curses.LINES-1,curses.COLS-1)
	time.sleep(FRAME_SLEEP)

if __name__ == "__main__":
	log.info("<<<Running maze generator independently.>>>")
	curses.wrapper(func)
