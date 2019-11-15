'''
Author: c17hawke
Name: Sunny Bhaveen Chandra
Date: Nov 15 2019
Time: 1351 hrs IST
Problem Statement:-

	Given a list of numbers and a number k, 
	return whether any two numbers from the list 
	add up to k.
	For example, given [10, 15, 3, 7] and k of 17, 
	return true since 10 + 7 is 17.
'''
import numpy as np 

def getResults(randomList, guess):
	'''
	figures out whether any two nos. in the list sum to
	our guessed no.
	'''
	for num in randomList:
		no_A = num
		no_B = guess - no_A
		if (no_A in randomList) and (no_B in randomList):
			return True
	return False

def main():
	# generating some random integre list of 20 nos.
	randomList = np.random.randint(1,100,20)
	print("random list: ",randomList)

	guess = int(input("Enter you choice of no.\n>> "))

	result = getResults(randomList, guess)
	#print the results
	print("Found two nos." if result else "Nos not found")


if __name__ == '__main__':
	main()
