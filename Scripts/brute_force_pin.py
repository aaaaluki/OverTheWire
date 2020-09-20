import subprocess
import math

MAX_COMB = 9999
STEP = 100
CMD = '/home/leviathan6/leviathan6'
KEY_WORDS = ['Wrong']


def print_output(o, e):
	print('Output: ' + o.decode('ascii'))
	print('Error: '  + e.decode('ascii'))
	print('code: '   + str(proc.returncode))


if __name__ == '__main__':
	i = 0
	while i <= MAX_COMB:
		if i % STEP == 0:
			print(i)

		pin = str(i).zfill(int(math.log10(MAX_COMB)) + 1)


		cmd = [CMD, pin]
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		out, error = proc.communicate()

		if not any(key in out for key in KEY_WORDS):
			print('The pint is ' + pin)

		i += 1

#		print_output(out, error)
