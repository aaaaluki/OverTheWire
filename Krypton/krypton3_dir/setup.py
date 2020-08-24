#!/usr/bin/python
import os
import sys

dir_to_create = ['encoded', 'decoded', 'data', 'to_decode', 'to_encode']
verbose = False


def check_dir(dir_name):
	cwd = os.path.dirname(__file__)

	dirc = os.path.join(cwd, dir_name)
	if os.path.exists(dirc):
		if not os.path.isdir(dirc):
			so.remove(dirc)
			os.mkdir(dirc)
	else:
		os.mkdir(dirc)


def main():
	try:
		if sys.argv[1] == '-v' or sys.argv[1] == '--verbosity':
			verbose = True
	except IndexError:
		pass

	for dirc in dir_to_create:
		check_dir(dirc)


if __name__ == '__main__':
	main()