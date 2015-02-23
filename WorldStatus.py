'''
Created on Feb 15, 2015

@author: Strag
'''

from VNData import Player
from VNData import NPC
from VNData import Map
import sys

class WorldStatus(object):
    
    def __init__(self):
        self.player = Player.Player()
        self.npcs = []
        self.week = 0
        self.day = 0
        self.time_of_day = 0


game_ready = False

world = ""

while not game_ready:
  load_saved = input("Load saved game? [y/n] ")
  if load_saved == 'y' or load_saved =='Y':
    print("No save found, exiting")
    sys.exit()
  elif load_saved == 'n' or load_saved == 'N':
    print("Starting new game.")
    game_ready = True
    world = WorldStatus()
  else:
    print("Invalid input")
    


def generate_world():
  num_npcs = input("Number of NPCs to generate: ")

    
  for _ in range(int(num_npcs)):
    world.npcs.append(NPC.generate())
    
  
generate_world()

locations = Map.importLocations()
events = Map.importEvents()

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

while world.week < 2:
  
  print("Week " + str(world.week + 1))
  print("Day: " + str(world.day + 1) + " (" + weekdays[world.day % 7] + ")")
  #assign events to locations
  for event in events:
    # check if event is valid for current day and time
    if event.isOpen(world.day, world.time_of_day):
      #check to make sure no event currently assigned to location
      if locations[event.location].event == "":
        locations[event.location].event = event.filename
      
  for loc in locations:
    location = locations[loc]
    #check if location is open
    if location.isOpen(world.day, world.time_of_day):
      if location.event != "" :
        print(location.name + ": " + location.event)
      elif location.default_event != "":
        print(location.name + ": " + location.default_event + "(DEFAULT)")
      else:
        print(location.name + ": HIDDEN")
        
    else:
      print(location.name + ": Closed")
      
  valid_destination = False
  while not valid_destination:
    destination = input("Choose a destination: ").upper()
    if destination.upper() in locations:
      valid_destination = True
      if locations[destination].event != "":
        Map.processEvent(locations[destination].event)
      else:
        Map.processEvent(locations[destination].default_event)
    else:
      print("Not a valid destination")
    
  for location in locations:
    locations[location].event = ""
  
  # move time forward
  if world.time_of_day == 3:
    world.time_of_day = 0
    world.day += 1
    if world.day % 7 == 0:
      world.week += 1
  else:
    world.time_of_day += 1
    