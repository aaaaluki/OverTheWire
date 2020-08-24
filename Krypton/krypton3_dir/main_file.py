#!/usr/bin/python
import os
import aux_functions as aux
import character_substitution as charsub
from freq_analysis import Freq_analysis


XGRAM = 1
show_fa_results = False


def main():
	fa = Freq_analysis()
	freqs = fa.main(show_fa_results)
	freqs_lang = fa.letter_frequency

	folder_data = os.path.join(fa.cwd, 'data')
	freqs_file = open(os.path.join(folder_data, 'freqs_encoded'), 'w+')
	lang_file = open(os.path.join(folder_data, 'freqs_lang'), 'w+')

	sorted_text_freqs = aux.get_sorted_dicto(freqs)
	sorted_lang_freqs = aux.get_sorted_dicto(freqs_lang)

	# Saving lang freqs
	for i in sorted_lang_freqs:
		lang_file.write('{k};{v:.2f}\n'.format(k=i[0], v=i[1]))

	lang_file.close()		

	# Saving sorted freqs
	for i in sorted_text_freqs:
		freqs_file.write('{k};{v:.11f}\n'.format(k=i[0], v=i[1]))

	freqs_file.close()

	encoding = {}

	for i in range(len(sorted_text_freqs)):
		encoding[sorted_lang_freqs[i][0]] = sorted_text_freqs[i][0]

	print('Pairs:')
	aux.print_dict(encoding)

	pairs_file = open(os.path.join(folder_data, 'pairs'), 'w+')

	for k,v in encoding.items():
		pairs_file.write('{k}:{v}\n'.format(k=k, v=v))

	pairs_file.close()

	for filename in fa.filenames:
		charsub.decode_file(filename, encoding)


if __name__ == '__main__':
	main()
	