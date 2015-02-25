#!/usr/bin/env python

import xml.etree.ElementTree as ET
tree = ET.parse('spontal.xml')
root = tree.getroot()
import sys

def main():
	
	for point in root.findall('POINT'):
		end = (point.find('F0_END').text)
		start = (point.find('F0_START').text)
		bottom = (point.find('BOTTOM_HZ').text)
		top = (point.find('TOP_HZ').text)
		if end < bottom or end > top:
			root.remove(point[12])
		if start < bottom or start > top:
			root.remove(point[13])

	tree.write('output.xml')

if __name__ == '__main__':
	main()

