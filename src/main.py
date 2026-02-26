from player import Player
import os
from maps import ground_floor, second_floor

def start():
    name = input("Welcome! What's your name?\n")
    player = Player(name)
    print(f"Nice to meet you {player.get_name()}!")
    begin = input("I could use your help. Are you ready to begin? (y/n)\n")
    if begin.lower() == "y":
        print(f"Great! I'm looking forward to working with you.")
        print(f"-" * 27)
        input("Press enter to continue.....")
        return player
    else:
        exit()

def clear():
    os.system('clear')


def main(player):
    current_room = 'Entryway'
    current_floor = ground_floor
    while True:
        clear()
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
        action = action.split(" ", 1)
        if len(action) < 2:
            print("Action must be paired with a target")
            input("press enter to continue.....")
            continue
        match(action[0]):
            case "go":
                if action[1] in current_floor[current_room]:
                    if (current_floor[current_room][action[1]] == "Safe Room" and current_floor["Study"]["locked"] == True):
                        print("The room is locked")
                        input("press enter to continue.....")
                    elif (current_floor[current_room][action[1]] == "Staircase" and current_floor["Hallway"]["locked"] == True):
                        print("The door is locked")
                        input("press enter to continue.....")
                    elif (current_floor[current_room][action[1]] == "Staircase" and current_floor["Hallway"]["locked"] == False):
                        print(f"{current_floor["Staircase"]["description"]}")
                        current_floor = current_floor["Staircase"]["next_floor"]
                        current_room = "Landing"
                        input("press enter to continue.....")
                    else:
                        current_room = current_floor[current_room][action[1]]
                else:
                    print("You can't go that way!")
                    input("press enter to continue.....")
            case "look":
                if action[1] in current_floor[current_room]:
                    print(current_floor[current_room][action[1]])
                    if current_room == "Study":
                        if action[1] == "red":
                            ground_floor["Study"]["locked"] = False
                    input("press enter to continue.....")
                else:
                    print("Nothing to see here")
                    input("press enter to continue.....")
            case "take":
                if "item" not in current_floor[current_room]:
                    print("There's nothing to take")
                    input("press enter to continue.....")
                else:
                    if action[1] in current_floor[current_room]["item"]:
                        player.add_inventory(action[1])
                        input("press enter to continue.....")
                    else:
                        print("I can't take that")
                        input("press enter to continue.....")
            case "use":
                if action[1] == "key":
                    if current_room == "Hallway":
                        if current_floor["Hallway"]["locked"] == True:
                            if "key" in player.get_inventory():
                                print("The door to the staircase unlocks")
                                current_floor["Hallway"]["locked"] = False
                                player.remove_inventory("key")
                                input("press enter to continue.....")
                            else:
                                print("I don't have the key")
                                input("press enter to continue.....")
                        else:
                            print("The door isn't locked")
                            input("press enter to continue.....")
                    else:
                        print("I can't use that here")
                        input("press enter to continue.....")
                elif action[1] not in player.get_inventory():
                    print("I don't have that")
                    input("press enter to continue.....")
                else:
                    print("I can't use that here")
                    input("press enter to continue.....")
            case _:
                print("invalid input")
                input("press enter to continue.....")


clear()
player = start()
main(player)