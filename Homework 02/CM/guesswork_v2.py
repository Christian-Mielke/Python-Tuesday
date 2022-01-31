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

import numpy


class Guestimation:
    def __init__(self, start: int = 0, stop: int = 100):
        """
        Class that contains a number guessing game
        PC or Human chooses integer between start and top range
        User or PC needs to do the guessing.

        :inits guestimation object with start,stop and choice attributes
        :param start: Lowest possible integer for a random integer Defaults to 0
        :param stop: Highest possible integer for a random integer Defaults to 100
        :return: options guestimation object
        """
        print(
            f'Welcome to the guessing game either you or your computer needs to guess which number has been chosen out of a randint({start},{stop})')
        print('\n')
        self.__choice = None
        self.start: int = start
        self.stop: int = stop
        options: list = ['P', 'H']
    while self.gametype not in options:
            self.gametype = input('Please input P for PC guestimation or H for Human guestimation!')
            print('Please input P for PC guestimation or H for Human guestimation!')
            self.gametype = input()
            if self.gametype in options:
                break
            else:
                print('Error! Please input P for PC guestimation or H for Human guestimation!')

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

    @staticmethod
    def check_int(guess:str):
        try:
            guess = int(guess)
        except ValueError:
            print(f"{guess} is not an integer or integer convertible string. Try again!")
            return -1
        return guess

    @staticmethod
    def check_checkmate(inputt: str)->str:
        if inputt in ["0", "-1", "1"]:
            return inputt
        else:
            print("Not a valid inputt only choose from [-1,0,1]")
            return "Error"

    def play_human(self):
        """
        Classmethod that runs the human guestimation game in a loop.
        Exits loop if number guessed correctly
        """
        print("I will pick my number now!")
        self.__choice = random.randint(self.start, self.stop)
        while True:
            print(f'Please input an integer from {self.start} to {self.stop} to guess your PCs Random Choice!')
            guess = input()
            guess = Guestimation.check_int(guess)
            if guess == -1:
                print("Error was encoutered try to punch in integer only again!")
                continue
            t_val = Guestimation.check_number(guess, self.start, self.stop)
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

    def play_pc(self):
        print(f"Please think of a number between {self.start} and {self.stop}")
        print(f"and give me hints for smaller=-1,larger=1 and match=0 to guess your number!")
        while True:
            datarange = numpy.arange(self.start, self.stop + 1, 1)
            guessidx = len(datarange) // 2
            if guessidx == 1:
                print(f"Is your number {datarange[0]}? [0] Or is it smaller=[-1] or larger[1]")
                checkmate = input()
                checkmate_aux = Guestimation.check_checkmate(checkmate)
                if checkmate_aux == "Error":
                    continue
                if checkmate_aux == "0":
                    print(f"I won your number was {datarange[0]}")
                    break
                else:
                    print(f"I won your number was {datarange[1]}")
                    break
            print(f"Is your number {datarange[guessidx]}? [0] Or is it smaller=[-1] or larger[1]")
            checkmate = input()
            checkmate_aux = Guestimation.check_checkmate(checkmate)
            if checkmate_aux == "Error":
                continue
            if checkmate == "0":
                print(f"I won your number was {datarange[guessidx]}")
                break
            elif checkmate == "-1":
                self.stop = datarange[guessidx]
            elif checkmate == "1":
                self.start = datarange[guessidx]

    def run(self):
        if self.gametype == "H":
            self.play_human()
        elif self.gametype == "P":
            self.play_pc()


if __name__ == "__main__":
    game = Guestimation()
    game.run()
