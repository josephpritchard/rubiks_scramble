import random

master_dict = {
        'Right': ("R", "R'", "R2", "R2'"),
        'Left': ("L", "L'", "L2", "L2'"),
        'Up': ("U", "U'", "U2", "U2'"),
        'Down': ("D", "D'", "D2", "D2'"),
        'Front': ("F", "F'", "F2", "F2'"),
        'Back': ("B", "B'", "B2", "B2'")
        }

## Review Master Dictionary
## Update Current Options Dictionary (Make a list?)
## Choose random item from current options
## Add item to Scramble List
## Make sure list stops at certain length (15?)
## Print list

options_list = []
previous_turn = None
scramble_list = []

# for loop function for appending values to the options list
# options list append
def ola():
    for value in v:
        options_list.append(value)

# new function, pt means previous_turn
def ol_fill(pt):
    pass
### START LOOP HERE ###
# Create options list with relevant data 
while len(scramble_list) < 26:
    if previous_turn == None:
        for k, v in master_dict.items():
            for value in v:
                options_list.append(value)
    elif 'R' in previous_turn:
        for k, v in master_dict.items():
            if k != 'Right':
                for value in v:
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

    # Choose next turn from options list
    # rn stands for random number
    range_end = len(options_list) - 1
    rn = random.randint(0, range_end)
    # random number boundaries
    if rn < 0:
        rn = 0
    if rn > range_end:
        rn = range_end
    next_turn = options_list[rn]
    scramble_list.append(next_turn)
    previous_turn = next_turn
    options_list = []
    range_end = None

print(f"Scramble list is: {scramble_list}")
