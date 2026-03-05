from player import Player
import os
from maps import ground_floor, second_floor, third_floor, fourth_floor, fifth_floor, attic
from help import controls
from endings import endings, ending_checks



compass = ["north", "south", "east", "west", "northwest", "northeast", "southwest", "southeast"]

def start():
    print("I wake up on a porch in the dark of night. I can't remember a thing. There's an ID in my pocket.")
    name = input("What does it say? ")
    player = Player(name)
    while True:
        clear()
        print(f"So my name is {player.get_name()}. Is this my house?")
        begin = input("There's only one way to find out. Should I go inside? (y/n)")
        clear()
        if begin.lower() == "y":
            print(f"I need to figure out what's going on here.")
            input("press enter to continue.....")
            return player
        elif begin.lower() == "n":
            print("What a shame.")
            input("press enter to continue.....")
            exit()
        else:
            print("Invalid input")
            input("press enter to continue.....")
            continue


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main(player):
    current_room = 'Entryway'
    current_floor = ground_floor
    while True:
        clear()
        if current_room == "Ending":
            ending()
        print(f"I am in the {current_room}")
        print(current_floor[current_room]["description"])
        print(f"-" * 27)
        print(f"Inventory: {player.get_inventory()}")
        print(f"-" * 27)

        action = input("What should I do?: ")
        action = action.lower()
        if action == "exit":
            clear()
            break
        if action == "help":
            print(controls)
            input("press enter to continue.....")
            continue
        action = action.split(" ", 1)
        if len(action) < 2:
            print("Action must be paired with a target.")
            input("press enter to continue.....")
            continue
        match(action[0]):
            case "go":
                if action[1] not in compass:
                    print("That's not a direction!")
                    input("press enter to continue.....")
                    continue
                if action[1] in current_floor[current_room] and action[1]:
                    if (current_floor[current_room][action[1]] == "Safe Room" and current_floor["Study"]["locked"] == True):
                        print("The room is locked.")
                        input("press enter to continue.....")
                    elif (current_floor[current_room][action[1]] == "Staircase" and current_floor["Hallway"]["locked"] == True):
                        print("The door is locked.")
                        input("press enter to continue.....")
                    elif (current_floor[current_room][action[1]] == "Staircase" and current_floor["Hallway"]["locked"] == False):
                        print(f"{current_floor["Staircase"]["description"]}")
                        current_floor = current_floor["Staircase"]["next_floor"]
                        current_room = "Landing"
                        input("press enter to continue.....")
                    elif (current_floor[current_room][action[1]] == "Kid's Room" and current_floor == fifth_floor and fifth_floor["Hallway"]["nlocked"] == True):
                        print("The room is locked.")
                        input("press enter to continue.....")
                    else:
                        current_room = current_floor[current_room][action[1]]
                else:
                    print("I can't go that way!")
                    input("press enter to continue.....")
            case "look":
                if current_room == "Attic":
                    if attic["Attic"]["dark"] == True and action[1] != "light switch":
                        print("It's too dark to see.")
                        input("press enter to continue.....")
                        continue
                if action[1] in current_floor[current_room]:
                    print(current_floor[current_room][action[1]])
                    if current_room == "Study":
                        if action[1] == "red":
                            ground_floor["Study"]["locked"] = False
                            ground_floor["Study"]["red"] = "Pulling on this book opened something on the west side of the room."
                    if current_room == "Attic":
                        if action[1] == "light switch" and attic["Attic"]["dark"] == True:
                            attic["Attic"]["dark"] = False
                            attic["Attic"]["description"] = "The attic is now illuminated except for a dark spot in the corner. There's a doll\nin the middle of the room and a door on the east end."
                            attic["Attic"]["light switch"] = "I already turned the lights on."
                    input("press enter to continue.....")
                else:
                    print("Nothing to see here.")
                    input("press enter to continue.....")
            case "take":
                if "item" not in current_floor[current_room]:
                    print("There's nothing to take.")
                    input("press enter to continue.....")
                else:
                    if action[1] in current_floor[current_room]["item"]:
                        player.add_inventory(action[1])
                        input("press enter to continue.....")
                    else:
                        print("I can't take that")
                        input("press enter to continue.....")
            case "use":
                if action[1] not in player.get_inventory():
                    print("I don't have that.")
                    input("press enter to continue.....")
                elif action[1] == "key" and current_room == "Hallway":
                    print("The door to the staircase unlocks.")
                    current_floor["Hallway"]["locked"] = False
                    player.remove_inventory("key")
                    input("press enter to continue.....")
                elif action[1] == "keycard" and current_floor == fifth_floor and current_room == "Hallway":
                    print("The bedroom to the Northwest unlocks.")
                    fifth_floor["Hallway"]["nlocked"] = False
                    player.remove_inventory("keycard")
                    input("press enter to continue.....")
                elif action[1] == "toy soldier" and current_floor == fifth_floor and current_room == "Kid's Room":
                    print("I place the toy soldier in line with the others.")
                    player.remove_inventory("toy soldier")
                    ending_checks["soldiers"] = True
                    fifth_floor["Kid's Room"]["toy box"] = "Four toy soldiers all in a row."
                    input("press enter to continue.....")
                elif current_floor == attic:
                    if current_room == "Landing":
                        if action[1] == "protein bar":
                            player.remove_inventory("protein bar")
                            print("A nice snack.")
                            ending_checks["eat"] = True
                            if ending_checks["drink"] == False:
                                attic["Landing"]["description"] = "A small landing with a single door to the east. After all this climbing, I'm feeling\na bit parched."
                            else:
                                attic["Landing"]["description"] = "A small landing with a single door to the east."
                            input("press enter to continue.....")
                        elif action[1] == "soda":
                            player.remove_inventory("soda")
                            print("Refreshing!")
                            ending_checks["drink"] = True
                            if ending_checks["eat"] == False:
                                attic["Landing"]["description"] = "A small landing with a single door to the east. After all this climbing, I'm feeling\na bit peckish."
                            else:
                                attic["Landing"]["description"] = "A small landing with a single door to the east."
                            input("press enter to continue.....")
                    elif current_room == "Attic":
                        if attic["Attic"]["dark"] == True:
                            print("It's too dark to see.")
                            input("press enter to continue.....")
                            continue
                        else:
                            if action[1] == "first aid kit":
                                player.remove_inventory("first aid kit")
                                print("I use the first aid kit to sew up the doll. She's good as new.")
                                attic["Attic"]["doll"] = "A soft cloth doll. She's in recovery."
                                ending_checks["fix_doll"] = True
                                input("press enter to continue.....")
                            elif action[1] == "flashlight":
                                player.remove_inventory("flashlight")
                                print("I illuminate the dark corner of the room.")
                                attic["Attic"]["still_dark"] = False
                                attic["Attic"]["description"] = "The attic is now fully illuminated. There's a doll in the middle of the\nroom and a snow globe in the corner where my flashlight is pointing. There's\nalso a door at the east end of the room."
                                attic["Attic"]["snow globe"] = "Inside the globe is a perfect recreation of this house."
                                input("press enter to continue.....")
                            elif action[1] == "revolver" and attic["Attic"]["still_dark"] == False:
                                if "bullets" in player.get_inventory():
                                    player.remove_inventory("bullets")
                                    print("I fire at the snow globe and it shatters. What remains is a glowing white orb where the globe once was.")
                                    attic["Attic"]["description"] = "The attic is now fully illuminated. There's a doll in the middle of the\nroom and a white orb in the corner where my flashlight is pointing."
                                    attic["Attic"]["snow globe"] = "It's been destoryed."
                                    attic["Attic"]["orb"] = "A glowing white orb where the snow globe once was."
                                    ending_checks["shoot_globe"] = True
                                    input("press enter to continue.....")
                                else:
                                    print("The gun clicks. It's empty.")
                                    input("press enter to continue.....")
                else:
                    print("I can't use that here.")
                    input("press enter to continue.....")
            case _:
                print("invalid input")
                input("press enter to continue.....")

def ending():
    ending_check_count = 0
    for checks in ending_checks:
        if ending_checks[checks] == True:
            ending_check_count += 1
    if ending_check_count == 0:
        print(endings["bad ending"])
        input("press enter to continue.....")
    elif ending_check_count == 5:
        print(endings["good ending"])
        input("press enter to continue.....")
    else:
        print(endings["neutral ending"])
        input("press enter to continue.....")
    clear()
    print("Thanks for playing! This was one of three endings. Play again to try for a different ending!")
    exit()

clear()
player = start()
main(player)