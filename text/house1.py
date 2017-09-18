# Copyright 2017, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General
# Public License

"""A text adventure.

A demonstrator program for learners of Python that is both
absorbing to play and has code that's easy to understand.
(What's the simplest/shortish program that acheives this?)

TO DO:
1. Decide on a mission
2. Add more places to visit
3. Add "give" or "drop" commands
4. Remove duplicate code by adding functions, e.g. for take()
5. ...
N. Replace all these functions with data structures instead.

"""

import sys

def command():
    "Get the next command from the user."
    while True:
        c = input("What do you want to do? ").lower()
        words = c.split()
        fw = words[0]
        if fw == "help":
            print("Commands: go <direction>, look, take <thing>, bag, ")

        # We can handle these commands right here:
        elif fw == "bag":
            print(world["bag"])

        # These are the only 
        elif fw in ["go", "look", "take"]:
            return c

        else:
            print("Sorry I don't understand that, try again: ")

def start():
    while True:
        print("\nYou are on a street in a small village. The road runs north to south.")
        c = command()

        if c == "go north":
            north_village()
        elif c == "go south":
            south_village()
        elif c == "look":
            print("Not much")
            
def north_village():
    while True:
        print("\nYou are in the north of the village, there are some fields on your east, and an old police house to the west.")
        c = command()
        if c == "go back":
            return
        elif c == "go east":
            north_east_fields()
        elif c == "go west":
            police_house()
        elif c == "look":
            print("Some old tins of paint")
        elif c == "take tin":
            world["bag"].append("tin")
            print("You put the tin in your bag")
        
def north_east_fields():
    while True:
        print("\nYou are in a field to the north east of the village, surrounded by a high, prickly hawthorn hedge. The road is behind you.")
        c = command()
        if c == "go back":
            return
        elif c == "look":
            print("Some mushrooms.")
        elif c.startswith("take mushroom"):
            world["bag"].append("mushroom")
        
def police_house():
    print("\nYou enter the police station, and bizarrely you are arrested. Sorry, that's the end of your game!")
    sys.exit()

def south_village():
    while True:
        print("\nYou are at the south of the village, there is a village store to the west, and a pub opposite to the east.")
        c = command()
        if c == "go back":
            return
        elif c == "look":
            print("Some flowers outside the store, some empty beer glasses outside the pub.")
        elif c == "take flowers":
            world["bag"].append("flowers")
            print("You take the flowers, but the shop keeper comes out and threatens to call the police!")
            world["criminal"] = True
        elif c.startswith("take glass"):
            world["bag"].append("glass")            
            print("You take a glass.")
            
# Everything in the world - a dictionary
world = {}

# What's in our bag? Nothing to start with
world["bag"] = []

start()
