import collections

def add_dicts(dicto_list):
	Cdict = None
	for dicto in dicto_list:
		Cdict += collections.Counter(dicto)

	return dict(Cdict)

def add_dicts(dict1, dict2):
	Cdict = collections.Counter(dict1) + collections.Counter(dict2)

	return dict(Cdict)

def print_dict(dicto):
	for k,v in dicto.items():
		print('\t{k} -> {v:.2f}'.format(k=k, v=v))

def print_dict(dicto):
	for k,v in dicto.items():
		print('\t{k} -> {v}'.format(k=k, v=v))

def get_sorted_dicto(dicto):
	return sorted(dicto.items(), key=lambda x: x[1], reverse=True)

def normalize_dict(dicto, num):
	for k in dicto:
		dicto[k] = 100*dicto[k]/num

	return dicto

def flip_dicto(dicto):
	output = {}
	for k, v in dicto.items():
		output[v] = k

	return output
	