from player import Player

attic = {
    "Landing" : {
        "description" : "A small landing with a single door to the east. After all this climbing, I'm feeling\n"
                        "peckish and a bit parched.",
        "east" : "Attic",
    },
    "Attic" : {
        "dark" : True,
        "still_dark" : True,
        "description" : "It's pitch black in here. On the wall next to me is a light switch and I can see a faint\n"
                        "light coming from under the door on the east end of the room.",
        "west" : "Landing",
        "east" : "Ending",
        "light switch" : "I flip the switch and illuminate the room.",
        "corner" : "I think there's something over there, but it's too dark to see.",
        "doll" : "A soft cloth doll with its torso flayed open.",
        "snow globe" : "Nothing to see here.",
        "orb" : "Nothing to see here.",
    },
    "Ending" : {
        "description" : "Placeholder for the ending. Enter the command 'exit' to exit the game."
    }
}


fifth_floor = {
    "Landing" : {
        "description" : "A small landing with a single door to the east.",
        "east" : "Hallway",
    },
    "Hallway" : {
        "locked" : True,
        "nlocked" : True,
        "description" : "A long dilapidated hallway with askew pictures lining the walls. There's a white door\n"
                        "at the east end. There is a locked door with a keypad and a bedroom door along the\n"
                        "north wall (Northwest and Northeast) as well as a bedroom door and bathroom door along\n"
                        "the south wall (Southwest and Southeast).",
        "west" : "Landing",
        "east" : "Staircase",
        "northwest" : "Kid's Room",
        "northeast" : "Master Bedroom",
        "southwest" : "Office",
        "southeast" : "Bathroom",
        "pictures" : "Torn family photos. I'm in most of them.",
    },
    "Kid's Room" : {
        "description" : "A young child's bedroom. There's a classic wooden wardrobe, a twin sized bed, and\n"
                        "a toy box.",
        "south" : "Hallway",
        "wardrobe" : "It's empty.",
        "bed" : "A neatly made twin sized bed with a duvet covered in cartoon characters.",
        "toy box" : "A beat up plastic toy box. On top of the closed lid is a line of three toy soldiers with\n"
                    "a gap between the first two.",
    },
    "Office" : {
        "description" : "An old bedroom converted into an office. There's a classic wooden wardrobe, a twin\n"
                        "sized bed, and an old desk.",
        "north" : "Hallway",
        "wardrobe" : "It's empty.",
        "bed" : "A neatly made twin sized bed with a beige duvet.",
        "desk" : "An old ornate wooden desk. It's bare except for a leather-bound journal.",
        "journal" : "It sits open on an entry for December 2nd. It just says 'I'm sorry' over and over.\nDid I write this?",
    },
    "Master Bedroom" : {
        "description" : "A large bedroom with a large classic wooden wardrobe and a queen sized bed\n"
                        "with a night stand. There's also a window opposite the door.",
        "south" : "Hallway",
        "wardrobe" : "The wardrobe is filled with dress shirts.",
        "bed" : "The bed was slopily made. It looks like whoever sleeps here sleeps on top of the white duvet.",
        "night stand" : "It's empty.",
        "window" : "From the second floor, I can see the whole back yard from this window. A rotted wooden\n"
                   "fence surrounds an overgrown lawn. There's a divot in the yard where a tree used to stand.\n"
                   "Towards the back of the yard is a rusted old swing set and in the corner is the remnants\n"
                   "of a shed that has burned down.",
    },
    "Bathroom" : {
        "description" : "A standard bathroom with a bathtub, toilet, sink, and medicine cabinet.",
        "north" : "Hallway",
        "bathtub" : "Yup, that's a bathtub.",
        "toilet" : "Yup, that's a toilet.",
        "sink" : "Yup, that's a sink.",
        "cabinet" : "There's a white key in the cabinet.",
        "item" : ["key"],
    },
    "Staircase" : {
        "description" : "Up we go to the final floor.....",
        "next_floor" : attic,
    },
}


fourth_floor = {
    "Landing" : {
        "description" : "A small landing with a single door to the east.",
        "east" : "Hallway",
    },
    "Hallway" : {
        "locked" : True,
        "description" : "A long hallway with pictures lining the walls. There's a red door at the east end.\n"
                        "There are two bedroom doors along the north wall (Northwest and Northeast)\n"
                        "as well as a bedroom door and bathroom door along the south wall (Southwest and Southeast).",
        "west" : "Landing",
        "east" : "Staircase",
        "northwest" : "Kid's Room",
        "northeast" : "Master Bedroom",
        "southwest" : "Teen's Room",
        "southeast" : "Bathroom",
        "pictures" : "Family pictures of a family of four; a married couple, a thirteen-year-old, and a four-year-old. I'm the husband in these.",
    },
    "Kid's Room" : {
        "description" : "A young child's bedroom. There's a classic wooden wardrobe, a twin sized bed, and\n"
                        "a toy box.",
        "south" : "Hallway",
        "wardrobe" : "The wardrobe is full of hand-me-downs.",
        "bed" : "A messy twin sized bed with a duvet covered in cartoon characters.",
        "toy box" : "A beat up plastic toy box. Action figures and other toys are scattered around it.",
    },
    "Teen's Room" : {
        "description" : "A neat bedroom with a classic wooden wardrobe, a twin sized bed, and an acoustic\n"
                        "guitar propped up on a stand.",
        "north" : "Hallway",
        "wardrobe" : "It's filled with polos of varying colors.",
        "bed" : "A made twin bed with a single stuffed animal on it.",
        "guitar" : "I think I used to play one of these. This one seems well loved. There's a red key taped\n"
                   "to the back of it.",
        "item" : ["key"],
    },
    "Master Bedroom" : {
        "description" : "A large bedroom with a large classic wooden wardrobe and a queen sized bed\n"
                        "with a night stand. There's also a window opposite the door.",
        "south" : "Hallway",
        "wardrobe" : "The wardrobe is half filled with blouses and half filled with dress shirts.",
        "bed" : "A queen sized bed that is neatly made with a red duvet.",
        "night stand" : "There's bullets here. Looks like they fit a revolver.",
        "window" : "From the second floor, I can see the whole back yard from this window. A wooden\n"
                   "privacy fence surrounds a slightly long lawn and a large tree stump. Towards the\n"
                   "back of the yard is a swing set, and in the back corner is a small shed.",
        "item" : ["bullets"],
    },
    "Bathroom" : {
        "description" : "A standard bathroom with a bathtub, toilet, sink, and medicine cabinet.",
        "north" : "Hallway",
        "bathtub" : "Yup, that's a bathtub.",
        "toilet" : "Yup, that's a toilet.",
        "sink" : "Yup, that's a sink.",
        "cabinet" : "There's a flashlight in the cabinet.",
        "item" : ["flashlight"],
    },
    "Staircase" : {
        "description" : "Up we go to the next floor.....",
        "next_floor" : fifth_floor,
    },
}


third_floor = {
    "Landing" : {
        "description" : "A small landing with a single door to the east.",
        "east" : "Hallway",
    },
    "Hallway" : {
        "locked" : True,
        "description" : "A long hallway with pictures lining the walls. There's a blue door at the east end.\n"
                        "There are two bedroom doors along the north wall (Northwest and Northeast)\n"
                        "as well as a bedroom door and bathroom door along the south wall (Southwest and Southeast).",
        "west" : "Landing",
        "east" : "Staircase",
        "northwest" : "Nursery",
        "northeast" : "Master Bedroom",
        "southwest" : "Bedroom",
        "southeast" : "Bathroom",
        "pictures" : "Family pictures of a family of four; a married couple, a ten-year-old, and an infant. I'm the husband in these.",
    },
    "Nursery" : {
        "description" : "A nursery with a classic wooden wardrobe and a crib.",
        "south" : "Hallway",
        "wardrobe" : "The wardrobe is filled with boxes of diapers and baby wipes.",
        "crib" : "A wooden crib. What's that on the mobile?",
        "mobile" : "Among the normal shapes hanging from the mobile is a blue key.",
        "item" : ["key"],
    },
    "Bedroom" : {
        "description" : "This appears to be an older child's bedroom. There's a classic wooden wardrobe, a\n"
                        "twin sized bed, and posters on the walls.",
        "north" : "Hallway",
        "wardrobe" : "Nothing but grapic tees in here.",
        "bed" : "A messy bed with several stuffed animals.",
        "posters" : "A collection of band posters for groups like 'Our Biological Allure' and 'Frantic! at the Party'.",
    },
    "Master Bedroom" : {
        "description" : "A large bedroom with a large classic wooden wardrobe and a queen sized bed\n"
                        "with a night stand. There's also a window opposite the door.",
        "south" : "Hallway",
        "wardrobe" : "The wardrobe is half filled with blouses and half filled with dress shirts.",
        "bed" : "A queen sized bed that is neatly made with a blue duvet.",
        "night stand" : "It's empty.",
        "window" : "From the second floor, I can see the whole back yard from this window. A wooden\n"
                   "privacy fence surrounds a green lawn and a large tree stump. At the far end of the\n"
                   "yard in the corner is a small painted shed.",
    },
    "Bathroom" : {
        "description" : "A standard bathroom with a bathtub, toilet, sink, and medicine cabinet.",
        "north" : "Hallway",
        "bathtub" : "Yup, that's a bathtub.",
        "toilet" : "Yup, that's a toilet.",
        "sink" : "Yup, that's a sink.",
        "cabinet" : "It's empty.",
    },
    "Staircase" : {
        "description" : "Up we go to the next floor.....",
        "next_floor" : fourth_floor,
    },
}


second_floor = {
    "Landing" : {
        "description" : "A small landing with a single door to the east.",
        "east" : "Hallway",
    },
    "Hallway" : {
        "locked" : True,
        "description" : "A long hallway with pictures lining the walls. There's a green door at the east end.\n"
                        "There are two bedroom doors along the north wall (Northwest and Northeast)\n"
                        "as well as a bedroom door and bathroom door along the south wall (Southwest and Southeast).",
        "west" : "Landing",
        "east" : "Staircase",
        "northwest" : "Guest Room",
        "southwest" : "Bedroom",
        "northeast" : "Master Bedroom",
        "southeast" : "Bathroom",
        "pictures" : "Family pictures of a family of three; a married couple and a seven-year-old. I'm the husband in these.",
    },
    "Guest Room" : {
        "description" : "An empty bedroom except for a classic wooden wardrobe and a twin sized bed.",
        "south" : "Hallway",
        "wardrobe" : "The wardrobe is empty.",
        "bed" : "A twin sized bed that is neatly made with a beige duvet.",
    },
    "Bedroom" : {
        "description" : "Clearly a child's bedroom. There's a classic wooden wardrobe, a twin sized bed\n"
                        "and a toy box.",
        "north" : "Hallway",
        "wardrobe" : "The wardrobe is filled with children's clothes.",
        "bed" : "An un-made twin sized bed with a duvet covered in cartoon characters.",
        "toy box" : "A plastic toy box filled with action figures. A small toy soldier catches my eye.",
        "toy soldier" : "Something about this seems familiar. Should I bring it with me?",
        "item" : ["toy soldier"],
    },
    "Master Bedroom" : {
        "description" : "A large bedroom with a large classic wooden wardrobe and a queen sized bed\n"
                        "with a night stand. There's also a window opposite the door.",
        "south" : "Hallway",
        "wardrobe" : "The wardrobe is half filled with blouses and half filled with dress shirts.",
        "bed" : "A queen sized bed that is neatly made with a green duvet.",
        "night stand" : "Inside the drawer of the night stand is a green key.",
        "window" : "From the second floor, I can see the whole back yard from this window. A wooden\n"
                   "privacy fence surrounds a fresh-cut lawn and a large oak tree. At the far end of\n"
                   "the yard in the corner is a small freshly-painted shed.",
        "item" : ["key"],
    },
    "Bathroom" : {
        "description" : "A standard bathroom with a bathtub, toilet, sink, and medicine cabinet.",
        "north" : "Hallway",
        "bathtub" : "Yup, that's a bathtub.",
        "toilet" : "Yup, that's a toilet.",
        "sink" : "Yup, that's a sink.",
        "cabinet" : "Inside the cabinet is a first aid kit.",
        "item" : ["first aid kit"],
    },
    "Staircase" : {
        "description" : "Up we go to the next floor.....",
        "next_floor" : third_floor,
    }
}


ground_floor = {
    "Entryway": {
        "description" : "The entryway is pretty basic with nothing of note besides doors to the north and west.",
        "north" : "Hallway",
        "west" : "Closet",
    },
    "Closet" : {
        "description" : "A standard coat closet with a single coat inside.",
        "east" : "Entryway",
        "coat" : "A long heavy coat with large pockets.",
        "pockets" : "Inside one of the pockets is a keycard.",
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
        "pictures" : "Family pictures of a family of four throughout the years. Wedding photos, baby pictures, etc.\nI appear to be the patriarch.",
    },
    "Study" : {
        "locked" : True,
        "description" : "A simple study with a desk and a bookshelf.",
        "west" : "Safe Room",
        "east" : "Hallway",
        "desk" : "On the desk is a framed picture and a file folder with a document inside.",
        "picture" : "Two young boys, they appear to be about four and thirteen.",
        "document" : "It's a legal document of some kind but most of it is redacted.",
        "bookshelf" : "A large bookshelf with many generic books. Three books stand out, one green, one blue, and one red.",
        "blue" : "An encyclopedia on ocean creatures.",
        "green" : "An album of family photos.",
        "red" : "I heard a click on the west side of the room.",
    },
    "Safe Room" : {
        "description" : "A small hidden room. Inside is a collection of pictures and a revolver.",
        "east" : "Study",
        "item" : ["revolver"],
        "revolver" : "A standard six-shooter.",
        "pictures" : "A collection of family photos, but all of the faces are blurred.",
    },
    "Dining Room" : {
        "description" : "A large dining room with a table and an old wooden hutch. The kitchen is to the east.",
        "east" : "Kitchen",
        "south" : "Hallway",
        "table" : "A dining room table set for a family of four.",
        "hutch" : "An old wooden hutch with two drawers with brass handles.",
        "drawers" : "Inside one of the drawers there is a yellow key.",
        "item" : ["key"],
    },
    "Kitchen" : {
        "description" : "A modest kitchen with an old refrigerator and a decent amount of counter space.",
        "west" : "Dining Room",
        "counter" : "On the counter there's a protein bar.",
        "refrigerator" : "Inside the fridge there's a case of soda.",
        "item" : ["protein bar", "soda"]
    },
    "Staircase" : {
        "description" : "Up we go to the second floor...",
        "next_floor" : second_floor,
    }
}

