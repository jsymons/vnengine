'''
Created on Feb 22, 2015

@author: Strag
'''

import xml.etree.ElementTree as ET
import os

location_file = "locations.xml"
event_file = "events.xml"

class Event(object):
  
  def __init__(self, days_of_week, time_of_day, location, requirement, filename):
    self.days_of_week = days_of_week
    self.time_of_day = time_of_day
    self.location = location
    self.requirement = requirement
    self.filename = filename
    
  def isOpen(self, day, time):
    if (self.days_of_week & (0b1 << (6 - (day % 7)))) > 0 and (self.time_of_day & (0b1 << (3 - time))) > 0:
      return True
    else:
      return False
    
class Location(object):
  
  def __init__(self, name, days_of_week, time_of_day, default_event):
    self.name = name
    self.days_of_week = days_of_week
    self.time_of_day = time_of_day
    self.occupant = ""
    self.event = ""
    self.default_event = default_event
    
  def isOpen(self, day, time):
    if (self.days_of_week & (0b1 << (6 - (day % 7)))) > 0 and (self.time_of_day & (0b1 << (3 - time))) > 0:
      return True
    else:
      return False

  
def importEvents():  
  tree = ET.parse(event_file)
  root = tree.getroot()
  all_events = []
  for event in root.findall('event'):
    days_of_week = int(event.find('days_of_week').text, 2)
    time_of_day = int(event.find('time_of_day').text, 2)
    location = event.find('location').text.upper()
    requirements = []
    for req in event.findall('requirement'):
      requirements.append([req.find('type').text, req.find('stat_to_check').text, req.find('min_value').text])
    filename = event.find('filename').text
    all_events.append(Event(days_of_week, time_of_day, location, requirements, filename))
  return all_events

def importLocations():
  tree = ET.parse(location_file)
  root = tree.getroot()
  all_locations = {}
  for location in root.findall('location'):
    name = location.get('name')
    days_of_week = int(location.find('days_of_week').text, 2)
    time_of_day = int(location.find('time_of_day').text, 2)
    if location.find('default_event') is None:
      default_event = ""
    else:
      default_event = location.find('default_event').text
    all_locations[name.upper()] = Location(name, days_of_week, time_of_day, default_event)
  return all_locations
  
def processEvent(event_file):
  f = open(os.path.join('events', event_file))
  for line in f:
    print(line)
  print("")
  