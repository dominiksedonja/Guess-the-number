#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

secret=(random.randint(0,100))
guess = 0
count = 0

while (secret != guess):
    count = count + 1
    guess = int(raw_input("Vnesi skrito številko!"))
    if (secret < guess):
        print "Iskano število je manjše"
    elif (secret > guess):
        print "Iskano število je večje"
    elif (secret == guess):
        print "Čestitek zadeli ste pravo število"
        print "Potrebovali ste"
        print count
        print "poskusov"

