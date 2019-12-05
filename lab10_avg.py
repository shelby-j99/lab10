#!/usr/bin/python3

import sys

def main():
	nums = len(sys.argv) - 1
	i = 1
	sum = 0
	while (nums >= i):
		sum = sum + nums
		i = i + 1
	print("The average is ", sum)

main()
