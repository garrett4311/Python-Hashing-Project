# Garrett Morris
# Project 1: Hashing
# CMPS 5243: Advanced Algorithm Analysis
# March 26, 2020
#This program generates a file and stores random numbers to that file

from random import seed
from random import randint

seed(1) # seed the random number generator
randomNums = open("RandomNumberFile1.txt", "w+")
nums = [] # list to store values in to check if there are duplicates
while len(nums) < 250:
    num = randint(1,9000) # random number is chosen between 1 and 9000
    present = False # flag to check if value is present
    for val in nums: # loop through every value in nums
        if num == val:
            present == True
    if present == False:
        randomNums.write(str(num) + "\n") # write value to an output file
        nums.append(num) # store result in a list as well
    
