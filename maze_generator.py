#!/usr/bin/python
import logging as log
import curses

log.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s', level=log.DEBUG, filename='maze_gen.log', datefmt='%Y-%m-%dT%H:%M:%S%z')

log.info("----------RUNNING PROCESS----------")

if __name__ == "__main__":
	print "Hello, Vim. :)"
