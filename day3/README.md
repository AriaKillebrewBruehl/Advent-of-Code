# Day 3 :ledger:

## Problem Overview

### Part 1
 Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.) Each bit in the gamma/epsilon rate can be determined by finding the most common bit (or least common bit for the epsilon rate) in the corresponding position of all numbers in the diagnostic report.

## Code Style

### Part 1
The input of binary numbers is parsed then passed to `getCounts(lines)`
which  updates an array to keep track of the number of 1s seen in each
position of each line with the last element of the array corresponding to the total number of lines. This array is passed to `getGamma(gamma)`
which builds a string corresponding to the gamma/epsilon rate in binary based on the method described above. This number is converted to binary and returned.

