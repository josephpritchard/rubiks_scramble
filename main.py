import random

master_dict = {
        'Right': ["R", "R'", "R2", "R2'"],
        'Left': ["L", "L'", "L2", "L2'"],
        'Up': ["U", "U'", "U2", "U2'"],
        'Down': ["D", "D'", "D2", "D2'"],
        'Front': ["F", "F'", "F2", "F2'"],
        'Back': ["B", "B'", "B2", "B2'"]
        }

## Review Master Dictionary
## Update Current Options Dictionary (Make a list?)
## Choose random item from current options
## Add item to Scramble List
## Make sure list stops at certain length (15?)
## Print list

options_list = []
previous_turn = "Start"
scramble_list = []

# new function, pt means previous_turn
# compares first letter of pt and value before adding the value to the options list
# this matches any letter move with any of its own letter moves (R R' R2 R2')
def ol_fill(pt):
    for k, v in master_dict.items():
        for value in v:
            if pt[0] != value[0]:
                options_list.append(value)

'''
# The following was replaced with ol_fill() function
# I'm leaving it here so I can remember my learning process

### START LOOP HERE ###
# Create options list with relevant data 
while len(scramble_list) < 26:
    if previous_turn == None:
        for k, v in master_dict.items():
            for value in v:
                options_list.append(value)
    elif 'R' in previous_turn:
        for k, v in master_dict.items():
            for value in v:
                if 'R' not in value:
                    options_list.append(value)
    elif 'L' in previous_turn:
        for k, v in master_dict.items():
            if k != 'Left':
                for value in v:
                    options_list.append(value)
    elif 'F' in previous_turn or 'B' in previous_turn:
        for k, v in master_dict.items():
            if k != 'Front' and k != 'Back':
                for value in v:
                    options_list.append(value)
    elif 'U' in previous_turn or 'D' in previous_turn:
        for k, v in master_dict.items():
            if k != 'Up' and k != 'Down':
                for value in v:
                    options_list.append(value)
'''

while len(scramble_list) < 26:
    ol_fill(previous_turn)
    # Choose next turn from options list
    # rn stands for random number
    range_end = len(options_list) - 1
    rn = random.randint(0, range_end)
    # random number boundaries
    if rn < 0:
        rn = 0
    if rn > range_end:
        rn = range_end
    # choose next turn with rn and add to scramble list
    next_turn = options_list[rn]
    scramble_list.append(next_turn)
    # make pt equal to next_turn for the next loop cycle
    previous_turn = next_turn
    # reset options list and range end
    options_list = []
    range_end = None

print(*scramble_list)
