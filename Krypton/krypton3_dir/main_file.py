import aux_functions as aux
import atbash
import freq_analysis as fa
from freq_analysis import letter_frequency, filenames


NO = 1
NX = 3
filename_format = 'found'
show_fa_results = False
freqs_lang = letter_frequency


def main():
	fa.setup(NO, NX, filename_format)
	freqs = fa.main(show_fa_results)

#	print('Test')
#	aux.print_dict(freqs)

	sorted_text_freqs = aux.get_sorted_dicto(freqs)
	sorted_lang_freqs = aux.get_sorted_dicto(freqs_lang)

	encoding = {}

	for i in range(len(sorted_text_freqs)):
		encoding[sorted_text_freqs[i][0]] = sorted_lang_freqs[i][0]

	print('Pairs:')
	aux.print_dict(encoding)

	pairs_file = 

	for filename in filenames:
		atbash.encode_file(filename, encoding)

	return 1


if __name__ == '__main__':
	main()