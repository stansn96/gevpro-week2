#!/usr/bin/python3

import sys
import json
from collections import namedtuple

def main():
	
	bestand = json.load(open('blood-die.json'))
	output = open('blood-die-result.json','w')
	paar = namedtuple('paar', ('taal', 'classificatie', 'bloed', 'sterven'))
	for taal in bestand:
		result = paar(taal[0],taal[1],taal[2],taal[3])
		bloed = result.bloed.split()
		sterven = result.sterven.split()
		[json.dump(taal,output) for i in bloed if i in sterven]
		

if __name__ == "__main__":
	main()
