from aux_functions import flip_dicto, print_dict

def encode_file(filename, pairs):
	file = open(filename, 'r')
	write = open(filename + '_atbash_encoded', 'w+')

	file_lines = file.readlines()

	for line in file_lines:
		line = line.upper()
		
		write.write(encode(line, pairs))

	write.write('\n')
	file.close()
	write.close

def decode_file(filename, pairs):
	file = open(filename, 'r')
	write = open(filename + '_atbash_decoded', 'w+')
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
