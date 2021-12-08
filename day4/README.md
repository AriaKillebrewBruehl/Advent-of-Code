# Day 04 :x:

## Problem Overview

### Part 1

Given a list of numbers to be called and a set of bingo boards, find that first winning board (a board where a row or column has all its entries marked off). Calculate the score of the board as the winning number times the sum of the remaining numbers on that board.

### Part 2

Instead of finding the first winning board, find that last winning board.

## Code style

### Part 1

The input is parsed into a list that contains the numbers to be drawn and a list of boards. Each board in the list of board is represented as a list of rows where each row is a list of the elements of that row. `drawNumbers()` find the winning board by going through the list of numbers and checking if that number is present in each board. If it is, the number is marked off by replacing that entry with `'-1'`. `hasWin()` is called to check if that board has a winning row or column. If it does the sum of the unmarked numbers on that board is calculated with `computeRemaining()` and that sum and the winning number is returned.

### Part 2

The input is parsed in the same manner as part