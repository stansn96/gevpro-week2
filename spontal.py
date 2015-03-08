#!/usr/bin/env python

import xml.etree.ElementTree as ET
import sys

def main():
	
	tree = ET.parse('spontal.xml')
	root = tree.getroot()
	
	for point in root.findall('POINT'):
		end = float((point.find('F0_END').text))
		start = float((point.find('F0_START').text))
		bottom = int((point.find('BOTTOM_HZ').text))
		top = int((point.find('TOP_HZ').text))
		if (not bottom <= start <= top) or (not bottom <= end <= top):
			root.remove(point)
	
	tree.write('output1.xml')

if __name__ == '__main__':
	main()

