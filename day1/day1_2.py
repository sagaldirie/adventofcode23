# My strategy:
# - replace all spelled out numbers with digits using dictionary digits_mapping
# - rerun functions from pt1 on new input strings

import pandas as pd

input_strings = pd.read_csv("day1_input.csv", header = None)

##### REPLACE SPELLED OUT NUMBERS WITH DIGITS. weird replcements because of overlapping:
# ex/ "eightwothree" using dictinary to replace would not result in 8, 3, since the "two" would be replaced first. would result in eigh23 which is incorrect.
digits_mapping = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine"
}

def get_nums(row):
    for word, digit in digits_mapping.items():
        row = row.replace(word, digit)
    return row

input_strings[0] = input_strings[0].apply(get_nums)

##### FIND FIRST NUMBER IN STRING, GOING FORWARD
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def find_forward(row):
    forward_nums = []
    for char in row[0]:  
        if char in nums:
            forward_nums.append(char)
            break 
    return forward_nums

all_rows_result_forward = input_strings.apply(find_forward, axis=1) 
forward_nums = [char for sublist in all_rows_result_forward for char in sublist]

##### FIND FIRST NUMBER IN STRING, GOING BACKWARDS
def find_backwards(row):
    backward_nums = []
    for char in row[0][::-1]:  # slice notation to reverse the order of chars in the string 
        if char in nums:
            backward_nums.append(char)
            break  # exit the inner loop if a match is found
    return backward_nums

all_rows_result_backward = input_strings.apply(find_backwards, axis=1)
backward_nums = [char for sublist in all_rows_result_backward for char in sublist]


##### COMBINE 1ST STRING, 2ND STRING, ETC IN FORWARD AND BACKWARDS LISTS. 4416, 5193
concatenated_list = [x + y for x, y in zip(forward_nums, backward_nums)]

##### CONVERT CHARS TO INTS
calibration_values = [int(x) for x in concatenated_list]

##### FIND SUM OF ALL CALIBRATION VALUES
answer = sum(calibration_values)
print(f"The sum of all the calibcation values is {answer}.")
