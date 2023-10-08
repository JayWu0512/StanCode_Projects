"""
File: anagram.py
Name: Jay
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

d = []


def main():
    """
    1. input the word
    2. read the dictionary
    3. find anagrams
    """
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')

    # input the word to find
    s = input('Find anagram for: ')

    # read the word in the dictionary
    read_dictionary(s)

    # calculate the data running time
    start = time.time()

    # find anagrams
    if s == EXIT:
        pass
    else:
        find_anagrams(s)

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    # put all letter of s (inputted word), in order to search the first letter and put in dictionary
    dict_list = []
    for i in range(len(s)):
        dict_list.append(s[i])

    # read the file
    with open(FILE, 'r') as f:
        for line in f:
            # if start with the letter of s, then put all of the word into list
            for letter in dict_list:
                prefix = line.startswith(letter)
                if prefix:
                    tokens = line.strip()
                    d.append(tokens)


def find_anagrams(s):
    """
    :param s: inputted word
    :return: anagrams
    """
    find_anagrams_helper(s, '', [], [], [])


def find_anagrams_helper(s, current_s, ans_list, index_list, now_list):
    # create the index of word (ex. arm -> [('a', 0), ('r', 1), ('m', 2)]
    if not index_list:
        for i in range(len(s)):
            index_list.append((s[i], i))

    # if the current_s (1)is same length as s, (2)it is in dictionary, (3)and not in ans_list, put it in ans_list
    if len(s) == len(current_s) and current_s in d:
        if current_s not in ans_list:
            print('Searching...')
            print(f'Found: {current_s}')
            ans_list.append(current_s)

    else:
        for token, index in index_list:
            # to reduce the searching time
            if current_s in ans_list:
                pass

            # search the index, if index is not in now_list, it needs to be added.
            if index not in now_list:

                # choose, assemble the current_s and put index to now_list
                current_s += token
                now_list.append(index)

                # explore, if it has prefix word, then keep doing recursion
                prefix = has_prefix(current_s)
                if prefix is True:
                    find_anagrams_helper(s, current_s, ans_list, index_list, now_list)

                # un-explore, delete the last current_s and the index in now_list
                current_s = current_s[:-1]
                now_list.pop()

    # print the final answer
    if current_s == '':
        print(f'{len(ans_list)} anagrams: {ans_list}')


def has_prefix(sub_s):
    """
    :param sub_s: the word which need to be judge first
    :return: True or False
    """
    # if it start with sub_s, then it will keep searching
    for token in d:
        if token.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
