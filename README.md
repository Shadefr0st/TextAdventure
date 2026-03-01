Thanks for trying my game! I have all of the controls mostly implemented every stage besides the final stage is present.
I still need to add the rest of the floors and the "flavor" of the game (ie. lore and other details).
So far, it's started just by running main.py. I'll add a better introduction with directions on how to
play later, but for now I'll just list the controls below. 

Movement and interaction is achieved with a command followed by the direction or what you want to interact with.

Go: the 'go' command followed by a cardinal direction will move you from room to room, assuming there is a room in
    that direction and the door is unlocked.

Look: the 'look' command followed by something in the room will give you a detail about that thing (there's currently
    a lot of placeholders).

Take: the 'take' command will add eligible items to your inventory.

Use: the 'use' command will use an item from your inventory. Currently, the only usable items are keys.

Exit: Exits the game.

As far as I know, these all work as intended and I've done my best to prevent errors (I fixed an error caused by 
using 'go' on an item and it causing the game to crash). I will later add a 'help' command that will provide the
player with the controls.