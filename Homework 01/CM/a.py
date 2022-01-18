#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
***************************************************************************
    guesswork.py

This is a small guessing game for your computer published at:
DXDOI:JourLaugh010422/0815/12345
    ---------------------
    Date                 : January 2022
    Copyright            : (C) 2022 by Christian Mielke
    Email                : christian.mielke@uba.de
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

import random


class guestimation:
    def __init__(self, start: int = 0, stop: int = 100):
        """
        Class that contains a number guessing game
        PC chooses integer between start and top range
        User needs to do the guessing.

        :inits guestimation object with start,stop and choice attributes
        :param start: Lowest possible integer for a random integer Defaults to 0
        :param stop: Highest possible integer for a random integer Defaults to 100
        :return: guestimation object
        """
        self.__choice = None
        self.start = start
        self.stop = stop
        self.__choice = random.randint(self.start, self.stop)

    def reset(self):
        """
        Classmethod for triggering a reset of the computers guestimation

        :inits reset of the initial choice
        :return: reseted guestimation.choice
        """
        self.__choice = random.randint(self.start, self.stop)

    @staticmethod
    def check_number(number: int, start: int, stop: int):
        """
        Classmethod for checking the user input with respect to the data range

        :param number: User input Number
        :param start: Lowest possible integer for a random integer Defaults to 0
        :param stop: Highest possible integer for a random integer Defaults to 100
        :return: -1 or None
        """
        if number < start or number > stop:
            print("Error! You have entered a value outside of the given range!")
            return -1

    def play(self):
        """
        Classmethod that runs the guestimation game in a loop.
        Exits loop if number guessed correctly
        """
        while (True):
            print(f'Please input an integer from {self.start} to {self.stop} to guess your PCs Random Choice!')
            guess = input()
            guess = int(guess)
            t_val = guestimation.check_number(guess, self.start, self.stop)
            if t_val == -1:
                print("Error was encoutered try again!")
                continue
            if guess == self.__choice:
                print(f'{guess} was the correct answer!')
                break
            elif guess < self.__choice:
                print(f'{guess} is smaller than your PCs choice')
            elif guess > self.__choice:
                print(f'{guess} is larger than your PCs choice')

if __name__ == "__main__":
    game = guestimation()
    game.play()
