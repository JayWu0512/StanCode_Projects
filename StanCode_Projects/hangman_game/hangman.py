"""
File: hangman.py
Name: Jay
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Step 1 : ask a question with '-' on every words
    Step 2 : set a win or loss condition
    Step 3 : set illegal format condition (type number or double words)
    Step 4 : if guess the wrong answer, lose one life
    Step 5 : if guess the correct answer, show the correct letter in words.
    """
    final_answer = random_word()
    life = N_TURNS
    length = ''
    # put '-' on every words
    for i in range(len(final_answer)):
        length += '-'
    print('The word looks like ' + str(length))
    # assign 'ans' to collect every correct answer
    ans = length
    while True:
        # win condition
        if ans == final_answer:
            print('You win!!')
            print('The word was: ' + str(final_answer))
            break
        # loss condition
        if life == 0:
            print('You are completely hung : (')
            print('The word was: ' + str(final_answer))
            break
        # type words in loop until win or loss
        guess = input('Your guess: ')
        guess = guess.upper()
        # avoid inputting numbers, like 1,2,3
        if not guess.isalpha():
            print('Illegal format.')
        # avoid inputting double words, like aa, ee,
        elif len(guess) > 1:
            print('Illegal format.')
        # wrong answer
        elif guess not in final_answer:
            print('There is no ' + str(guess) + '\'s in the word.')
            print('The word looks like ' + str(ans))
            life -= 1
            print('You have ' + str(life) + ' wrong guesses left.')
        # correct answer
        else:
            for i in range(len(final_answer)):
                j = final_answer[i]
                if j == guess:
                    ans = ans[:i] + guess + ans[i+1:]
                # reassemble correct answer without messing up
            print('You are correct!')
            print('The word looks like ' + str(ans))
            print('You have ' + str(life) + ' wrong guesses left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
