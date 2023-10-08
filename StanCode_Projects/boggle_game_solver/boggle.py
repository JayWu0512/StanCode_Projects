"""
File: boggle.py
Name: Jay
----------------------------------------
TODO: find letters
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	1. input words and put them in a list
	2. read dictionary
	3. recursion (assemble words in list, and print them if they are in dictionary)
	"""
	# set a list and put all words into it
	boggle_list = []

	# if boggle_list doesn't have anything
	while not boggle_list:
		# set the first low, and put inputted words inside
		input1_list = []
		# case-insensitive
		input1 = input('1 row of letters: ').lower()
		# it must has seven words(include a space), and the first, third, fifth word is space
		if len(input1) == 7 and input1[1].isspace() and input1[3].isspace() and input1[5].isspace():
			# ignore space
			input1 = input1.split()
			# put the word into the list(input1)
			for i in range(len(input1)):
				input1_list.append(input1[i])
			# put the input1_list into boggle list
			boggle_list.append(input1_list)
		else:
			print('Illegal input')
			break

		# set the second low, and put inputted words inside
		input2_list = []
		# case-insensitive
		input2 = input('2 row of letters: ').lower()
		# it must has seven words(include a space), and the first, third, fifth word is space
		if len(input2) == 7  and input2[1].isspace() and input2[3].isspace() and input2[5].isspace():
			# ignore space
			input2 = input2.split()
			# put the word into the list(input2)
			for i in range(len(input2)):
				input2_list.append(input2[i])
			# put the input1_list into boggle list
			boggle_list.append(input2_list)
		else:
			print('Illegal input')
			break

		# set the third low, and put inputted words inside
		input3_list = []
		# case-insensitive
		input3 = input('3 row of letters: ').lower()
		# it must has seven words(include a space), and the first, third, fifth word is space
		if len(input3) == 7 and input3[1].isspace() and input3[3].isspace() and input3[5].isspace():
			# ignore space
			input3 = input3.split()
			# put the word into the list(input3)
			for i in range(len(input3)):
				input3_list.append(input3[i])
			# put the input1_list into boggle list
			boggle_list.append(input3_list)
		else:
			print('Illegal input')
			break

		# set the forth low, and put inputted words inside
		input4_list = []
		# case-insensitive
		input4 = input('4 row of letters: ').lower()
		# it must has seven words(include a space), and the first, third, fifth word is space
		if len(input4) == 7 and input4[1].isspace() and input4[3].isspace() and input4[5].isspace():
			# ignore space
			input4 = input4.split()
			# put the word into the list(input4)
			for i in range(len(input4)):
				input4_list.append(input4[i])
			# put the input1_list into boggle list
			boggle_list.append(input4_list)
		else:
			# if input wrong type, print 'illegal input'
			print('Illegal input')
			break

		# read dictionary
		d = read_dictionary()

		# count the searching time
		start = time.time()

		# recursion(assemble words in list, and print them if they are in dictionary)
		for i in range(0, 4):
			for j in range(0, 4):
				find_words(i, j, boggle_list, [], d, '', [])

		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	# put the word in dictionary into a list
	d = []
	with open(FILE, 'r') as f:
		for line in f:
			tokens = line.strip()
			d.append(tokens)
	return d


def has_prefix(sub_s, d):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	# if a word start with sub_s, then it will keep searching
	for token in d:
		if token.startswith(sub_s):
			return True
	return False


def find_words(i, j, boggle_list, current_list, d, current_s, ans_list):
	"""
	: param i: boggle_list[i][j], to check the letter in boggle list
	: param j: boggle_list[i][j], to check the letter in boggle list
	: param boggle_list: the inputted words
	: param current_list: (i, j) inside it, to check whether the word has be assembled or not
	: param d: dictionary
	: param current_s: assembled words
	: param ans_list: the words which are printed
	"""

	# print the word if
	# (1) the word is in dictionary
	# (2) the word is not in ans_list (avoid printing twice)
	# (3) the length of word is more than 4
	if current_s in d and current_s not in ans_list and len(current_s) >= 4:
		print(f'Found "{current_s}"')
		ans_list.append(current_s)

	# over the boundary, it won't keep searching
	if i < 0 or i > 3 or j < 0 or j > 3:
		return
	else:
		# if the word (which is placed in (i,j)) is not assembled yet, then add it
		if (i, j) not in current_list:

			# choose, add to current_s and record (i,j)
			current_s += boggle_list[i][j]
			current_list.append((i, j))

			# explore, if the word start in current_s, then keep searching
			# the next letter will be at 8 places
			prefix = has_prefix(current_s, d)
			if prefix:
				# left-down
				find_words(i - 1, j - 1, boggle_list, current_list, d, current_s, ans_list)
				# down
				find_words(i - 1, j, boggle_list, current_list, d, current_s, ans_list)
				# right-down
				find_words(i - 1, j + 1, boggle_list, current_list, d, current_s, ans_list)
				# left
				find_words(i, j - 1, boggle_list, current_list, d, current_s, ans_list)
				# right
				find_words(i, j + 1, boggle_list, current_list, d, current_s, ans_list)
				# left-up
				find_words(i + 1, j - 1, boggle_list, current_list, d, current_s, ans_list)
				# up
				find_words(i + 1, j, boggle_list, current_list, d, current_s, ans_list)
				# right-up
				find_words(i + 1, j + 1, boggle_list, current_list, d, current_s, ans_list)

			# un-choose, pop the (i,j) last time we stored
			current_list.pop()


if __name__ == '__main__':
	main()
