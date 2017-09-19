#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

secret = (random.randint(0, 100))
guess = None
count = 0
'''
for i in range(10):
    guess = int(raw_input("Guess the number: "))
    if (secret < guess):
        print "Number is less than " + str(guess)
    elif (secret > guess):
        print "Number is greater than " + str(guess)
    elif (secret == guess):
        print "Congratulations you guessed the number " + str(i + 1)

        break
'''

print "while loop"
guess = None
while (secret != guess):
    count += 1
    guess = int(raw_input("Guess the number: "))
    if (secret == guess):
        print "Congratulations you guesses the secret number"
        print "Number of attempts: " + str(count)
        break
    elif (secret < guess):
        print "Secret number is less than " + str(guess)
    elif (secret > guess):
        print "Secret number is greater than " + str(guess)

    if (count >= 8):
        print "You lose - too many attempts"
        break