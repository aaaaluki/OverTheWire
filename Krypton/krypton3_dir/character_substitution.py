import os
from os.path import join
from aux_functions import flip_dicto, print_dict

def encode_file(filename, pairs):
	cwd = os.path.dirname(__file__)

	path_to_encode = join(cwd, 'to_encode', filename)
	path_encoded = join(cwd, 'encoded', filename)

	file = open(path_to_encode, 'r')
	write = open(path_encoded + '_encoded', 'w+')

	file_lines = file.readlines()

	for line in file_lines:
		line = line.upper()
		
		write.write(encode(line, pairs))

	write.write('\n')
	file.close()
	write.close

def decode_file(filename, pairs):
	cwd = os.path.dirname(__file__)

	path_to_decode = join(cwd, 'to_decode', filename)
	path_decoded = join(cwd, 'decoded', filename)

	file = open(path_to_decode, 'r')
	write = open(path_decoded + '_decoded', 'w+')

	decoded_pairs = flip_dicto(pairs)
	file_lines = file.readlines()

	for line in file_lines:
		line = line.upper()
		
		write.write(decode(line, decoded_pairs))

	write.write('\n')
	file.close()
	write.close

def encode(text, pairs):
	output = ''

	for char in text:
		if char.isalpha():
			output += pairs[char]

	return output

def decode(text, decoded_pairs):
	output = ''

	for char in text:
		if char.isalpha():
			output += decoded_pairs[char]

	return output
