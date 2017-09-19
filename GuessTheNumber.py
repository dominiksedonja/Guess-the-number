#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def check_num(guess, secret, less, greater):
    if secret == guess:
        return True
    elif (secret < guess):
        return less
    elif (secret > guess):
        return greater

def main():
    less = "less"
    greater = "greater"
    guess = None
    count = 0
    secret = (random.randint(0, 100))

    while (secret != guess):
        count += 1
        guess = int(raw_input("Guess the number: "))
        if check_num(guess, secret, less, greater) == True:
            print "Congratulations you guessed the secret number"
            print "Number of attempts: " + str(count)
            break
        elif check_num(guess, secret, less, greater) == less:
            print "Secret number is less than " + str(guess)
        elif check_num(guess, secret, less, greater) == greater:
            print "Secret number is greater than " + str(guess)

        if (count >= 8):
            print "You lose - too many attempts"
            break

if __name__ == "__main__":
    main()