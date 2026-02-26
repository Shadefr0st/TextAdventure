


second_floor = {
    "Landing" : {
        "description" : "A small landing with a single door to the east",
        "east" : "Hallway",
    },
    "Hallway" : {
        "locked" : True,
        "description" : "A long hallway with pictures lining the walls. There's a green door at the east end.\n"
                        "There are two bedroom doors along the north wall (Northwest and Northeast)\n"
                        "as well as doors to the Master Bedroom and Bathroom along the south wall (Southwest and Southeast).",
        "west" : "Landing",
        "east" : "Staircase",
    }
}


ground_floor = {
    "Entryway": {
        "description" : "The entryway is pretty basic with nothing of note besides doors to the north and west",
        "north" : "Hallway",
        "west" : "Closet",
    },
    "Closet" : {
        "description" : "A standard coat closet with a single coat inside",
        "east" : "Entryway",
        "coat" : "A long heavy coat with large pockets",
        "pockets" : "Inside one of the pockets is a keycard",
        "item" : ["keycard"],
    },
    "Hallway" : {
        "locked" : True,
        "description" : "A large hallway with pictures along the walls and doors in every direction.\n"
                        "The doors to the north and west are normal but the door to the east is yellow.",
        "north" : "Dining Room",
        "west" : "Study",
        "east" : "Staircase",
        "south" : "Entryway",
        "pictures" : "insert lore here",
    },
    "Study" : {
        "locked" : True,
        "description" : "A simple study with a desk and a bookshelf",
        "west" : "Safe Room",
        "east" : "Hallway",
        "desk" : "On the desk is a framed picture and a file folder with a document inside",
        "picture" : "insert lore here",
        "document" : "insert lore here",
        "bookshelf" : "A large bookshelf with many generic books. Three books stand out, one blue, one green, and one red",
        "blue" : "An encyclopedia on ocean creatures",
        "green" : "An album of family photos",
        "red" : "I heard a click on the west side of the room",
    },
    "Safe Room" : {
        "description" : "A small hidden room. Inside is a collection of pictures and a revolver",
        "east" : "Study",
        "item" : ["revolver"],
        "pictures" : "insert lore here",
    },
    "Dining Room" : {
        "description" : "A large dining room with a table and an old wooden hutch. The kitchen is to the east",
        "east" : "Kitchen",
        "south" : "Hallway",
        "table" : "A dining room table set for a family of four",
        "hutch" : "An old wooden hutch with two drawers with brass handles",
        "drawers" : "Inside one of the drawers there is a yellow key",
        "item" : ["key"],
    },
    "Kitchen" : {
        "description" : "A modest kitchen with an old refrigerator and a decent amount of counter space",
        "west" : "Dining Room",
        "counter" : "On the counter there's a protein bar",
        "refrigerator" : "Inside the fridge there's a can of soda",
        "item" : ["protein bar", "soda"]
    },
    "Staircase" : {
        "description" : "Up we go to the second floor...",
        "next_floor" : second_floor,
    }
}

