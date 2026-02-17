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



if len(scramble_list) < 15:
    if previous_turn == None:
        for k, v in master_dict.items():
            for values in v:
                options_list.append(values)

print(f"options_list is {options_list}")
print(f"len(options_list) is {len(options_list)}")
