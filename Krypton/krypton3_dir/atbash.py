def encode_file(filename, pairs):
	file = open(filename, 'r')
	write = open(filename + '.decoded', 'w+')

	file_lines = file.readlines()

	for line in file_lines:
		line = line.upper()
		
		write.write(encode(line, pairs))

	write.write('')
	file.close()
	write.close


def encode(text, pairs):
	output = ''

	for char in text:
		if char.isalpha():
			output += pairs[char]

	return output