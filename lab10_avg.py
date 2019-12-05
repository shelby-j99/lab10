#!/usr/bin/python3

import sys

def main():
	
	length = len(sys.argv) - 1
	total = 0
	
	for arg in sys.argv[1:]:
		total += int(arg)

	print("The average is", total // length)

main()
