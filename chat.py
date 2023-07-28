#留言格式改寫

def read_file(filename):
	new = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			new.append(line.strip())
	print(new)	
	return new	

def convert(new_file):
	person = None
	new = []
	for line in new_file:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'	
			continue
		new.append(person + ': ' + line)
	return new

def	write_file(filename, new):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in new:
			f.write(line + '\n')		


def main():
	new_file = read_file('input.txt')
	new = convert(new_file)
	write_file('output.txt', new)

main()	