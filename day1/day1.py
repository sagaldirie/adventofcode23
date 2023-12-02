# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

# My strategy:
# - for each string, read forward and backwards, check if its in nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]). 
# - If in nums (which I'll make strings since the # will be a string in 1abc2), add to forward_nums = [], apply other func and add to (backward_nums = [])
# - add 1st forward_num to 1st backward_num as strings, for both dfs entire length. add these strings to "calibration_values" = []
# - convert to int and add it up

###################################################################################################################################################################

import pandas as pd

input_strings = pd.read_csv("day1_input.csv", header = None)

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


##### FIND FIRST NUMBER IN STRING, GOING FORWARD
def find_forward(row):
    forward_nums = []
    for char in row[0]:  # this line iterate through each char in the string from the FIRST COLUMN (df only has one col), aka the row
        if char in nums:
            forward_nums.append(char)
            break  # exit the inner loop if a match is found
    return forward_nums

all_rows_result_forward = input_strings.apply(find_forward, axis=1) # when axis=1, operation is applied along each row. axis=0 (or not specified/default), operation on column

forward_nums = [char for sublist in all_rows_result_forward for char in sublist]

print(forward_nums)
# print(len(forward_nums)) # sanity check, got correct # of chars


##### FIND FIRST NUMBER IN STRING, GOING BACKWARDS
def find_backwards(row):
    backward_nums = []
    for char in row[0][::-1]:
        if char in nums:
            backward_nums.append(char)
            break  
    return backward_nums

all_rows_result_backward = input_strings.apply(find_backwards, axis=1)
backward_nums = [char for sublist in all_rows_result_backward for char in sublist]

##### COMBINE 1ST STRING, 2ND STRING, ETC IN FORWARD AND BACKWARDS LISTS. 4413 2193
concatenated_list = [x + y for x, y in zip(forward_nums, backward_nums)]

##### CONVERT CHARS TO INTS
calibration_values = [int(x) for x in concatenated_list]

##### FIND SUM OF ALL CALIBRATION VALUES
answer = sum(calibration_values)
print(f"The sum of all the calibcation values is {answer}.")
