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
print(f"previous_turn is {previous_turn}")
print(f"options_list1 is {options_list}")

### START LOOP HERE ###
# Create options list with relevant data    
if len(scramble_list) < 15:
    if previous_turn == None:
        for k, v in master_dict.items():
            for value in v:
                options_list.append(value)
        print(f"options_list2 is {options_list}")
    elif 'R' in previous_turn or 'L' in previous_turn:
        for k, v in master_dict.items():
            if k != 'Right' and k != 'Left':
                for value in v:
                    options_list.append(value)
        print(f"options_list3 is {options_list}")
    elif 'F' in previous_turn or 'R' in previous_turn:
        for k, v in master_dict.items():
            if k != 'Front' and k != 'Back':
                for value in v:
                    options_list.append(value)
        print(f"options_list4 is {options_list}")
    elif 'U' in previous_turn or 'D' in previous_turn:
        for k, v in master_dict.items():
            if k != 'Up' and k != 'Down':
                for value in v:
                    options_list.append(value)
        print(f"options_list5 is {options_list}")

# if len(scramble_list) < 15:
    for k, v in master_dict.items():
        match previous_turn:
            case None:
                print("None is none.")
            case "R" | "L":
                print("R or L")
            case "F" | "B":
                print("F or B")
            case "U" | "D":
                print("U or D")

# Choose next turn from options list
# rn stands for random number
rn = random.randint(0, len(options_list))
next_turn = options_list[rn]
scramble_list.append(next_turn)
previous_turn = next_turn

print(f"options_list6 is {options_list}")
print(f"len(options_list) is {len(options_list)}")
print(f"next_turn is {next_turn}")
print(f"scramble_list is {scramble_list}")
print(f"previous_turn is {previous_turn}")
