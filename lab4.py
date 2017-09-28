import re


myfile=open('mbox-short.txt', 'r')

with open("mbox-short.txt","r") as f:
	f= f.readlines()
	for line in f:
		if re.search('From', line):
			print(line)
			numbers = re.findall('[0-9]+',line)
			print (numbers)
			name = re.findall('(\5*)@',line)
			print(name)

