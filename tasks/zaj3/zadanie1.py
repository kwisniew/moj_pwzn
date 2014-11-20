# -*- coding: utf-8 -*-

import csv
from collections import defaultdict
import operator

def load_data(path):

	with open(path, 'r') as f:
		r = csv.reader(f, dialect=csv.unix_dialect)
		for line in r:
			yield line[0], int(line[1])

def suggester(input, data):

	counter = defaultdict(lambda : 0)
	sum=0
	lis = []
	for i in data:
		if i[0][0:len(input)]==input:
			counter[i[0][len(input)]]+=i[1]

	dit = dict(counter)
	for key, value in dit.items():
		sum+=value
	for key, value in dit.items():
		dit[key]=value/sum

	lis = sorted(dit.items(), key=operator.itemgetter(1), reverse=True)
	return lis
		
			

lista = list(load_data('/opt/pwzn/zaj3/enwiki-20140903-pages-articles_part_0.xmlascii1000.csv'))
print(suggester('ala ', lista))
