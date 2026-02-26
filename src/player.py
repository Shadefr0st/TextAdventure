class Player:
    def __init__(self, name):
        self.__name = name
        self.__health = 100
        self.__inventory = []
    
    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    
    def get_inventory(self):
        return self.__inventory
    
    def add_inventory(self, item):
        if item in self.__inventory:
            print("I already have that item!")
        else:
            self.__inventory.append(item)
            print(f"I have aquired the {item}")

    def remove_inventory(self, item):
        if item in self.__inventory:
            self.__inventory.remove(item)
        else:
            print("I don't have the {item}!")