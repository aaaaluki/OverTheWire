import aux_functions as aux

filenames = ['krypton4']

letter_frequency = {'E' : 12.0,
'T' : 9.10,
'A' : 8.12,
'O' : 7.68,
'I' : 7.31,
'N' : 6.95,
'S' : 6.28,
'R' : 6.02,
'H' : 5.92,
'D' : 4.32,
'L' : 3.98,
'U' : 2.88,
'C' : 2.71,
'M' : 2.61,
'F' : 2.30,
'Y' : 2.11,
'W' : 2.09,
'G' : 2.03,
'P' : 1.82,
'B' : 1.49,
'V' : 1.11,
'K' : 0.69,
'X' : 0.17,
'Q' : 0.11,
'J' : 0.10,
'Z' : 0.07 }

def setup(N0, NX, filename_format):
	for i in range(N0, NX+1):
		filenames.append(filename_format + str(i))

def char_counter(file):
	freqs = letter_frequency.copy()
	freqs = dict.fromkeys(freqs, 0.00)
	num = 0

	file_lines = file.readlines()

	for line in file_lines:
		line  = line.upper()
		for char in line:
			if not char.isalpha():
				continue
			else:
				freqs[char] += 1
				num += 1

	if num == 0:
		return -1
	else:
		return freqs, num

def main(show_results=False):
	if show_results:
		print('Letter frequency: English')
		aux.print_dict(letter_frequency)

	count = 0
	freqs_count = {}

	for filename in filenames:
		file = open(filename, 'r')

		freqs_temp, num = char_counter(file)

		if show_results:
			print(filename)
			aux.print_dict(aux.normalize_dict(freqs_temp, num))

		count += num
		freqs_count = aux.add_dicts(freqs_count, freqs_temp)

		file.close()

	return aux.normalize_dict(freqs_count, count)


if __name__ == '__main__':
	main()
