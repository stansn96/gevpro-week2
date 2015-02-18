#!/usr/bin/env python

class Country():
	
	def __init__(self, land):
		self.land = land
		
	def __str__(self):
		return("Hello from {}!".format(self.land))
		
def main():
	
	i = Country("Rusland")
	print(i)
	p = Country("China")
	print(p)
	q = Country("Zuid-Korea")
	print (q)
	
if __name__ == '__main__':
	main()
		
