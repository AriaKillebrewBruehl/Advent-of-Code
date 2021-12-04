# Day 1 :chart_with_downwards_trend:

## Problem Overview

- Given a list of integers which represent the depth of the sea floor, count the number of times a depth measurement increases.
- Given a list of integers which represent the depth of the sea floor, count the number of times the depth measurement in a window of size 3 increases.

## Code Style

The code for part 1 is very straight forward and just runs through the list of integers, keeping track of the current and previous depth, and comparing the two.

For part 2 has a similar style except that the first value of the first window is compared to the last value of the second window (since all other values are shared between the two windows).