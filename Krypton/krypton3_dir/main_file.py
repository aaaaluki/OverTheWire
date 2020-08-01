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

	freqs_file = open('freqs_encoded', 'w+')
	lang_file = open('freqs_lang', 'w+')

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

	pairs_file = open('pairs', 'w+')

	for k,v in encoding.items():
		pairs_file.write('{k}:{v}\n'.format(k=k, v=v))

	pairs_file.close()

	for filename in filenames:
		atbash.decode_file(filename, encoding)

	return 1


if __name__ == '__main__':
	main()
	