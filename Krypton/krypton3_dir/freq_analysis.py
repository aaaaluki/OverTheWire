import os
import aux_functions as aux

class Freq_analysis:
	filenames = []
	cwd = ''
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

	def __init__(self):
		Freq_analysis.cwd = os.path.dirname(__file__)
		path = os.path.join(Freq_analysis.cwd, 'to_decode')
		for file in os.listdir(path):
			if os.path.isfile(os.path.join(path, file)):
				Freq_analysis.filenames.append(file)

	def ngram_counter(self, file, N):
		freqs = {}
		num = 0

		for line in file.readlines():
			line.upper()
			for i in range(len(line)+1-N):
				gram = line[i:i+N]
				if gram.isalpha():
					if gram in freqs:
						freqs[gram] += 1
					else:
						freqs[gram] = 1

					num += 1

		return freqs, num

	def main(self, show_results=False, N=1):
		if show_results:
			print('Letter frequency: English')
			aux.print_dict(Freq_analysis.letter_frequency)

		count = 0
		freqs_count = {}
		folder = os.path.join(Freq_analysis.cwd, 'to_decode')

		for filename in Freq_analysis.filenames:
			filename = os.path.join(folder, filename)
			with open(filename, 'r') as file:

				freqs_temp, num = self.ngram_counter(file, N)

				if show_results:
					print(filename)
					aux.print_dict(aux.normalize_dict(freqs_temp, num))

				count += num
				freqs_count = aux.add_dicts(freqs_count, freqs_temp)

		return aux.normalize_dict(freqs_count, count)
