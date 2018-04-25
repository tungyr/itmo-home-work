def camel_to_snake(name):
	name2 = ''
	for i in name:
		if i.isupper():
			name2 += '_' + i.lower()
		else: name2 += i
	if name2[0] == '_':
		name2 = name2[1:]
	return name2


def snake_to_camel(name):
	name = name.title().replace('_', '')
	return name

camel_to_snake('CamelCase')
