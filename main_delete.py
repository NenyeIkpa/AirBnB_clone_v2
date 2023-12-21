#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City

fs = FileStorage()

all_states = fs.all()
print(all_states)

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create another State
another_state = State()
another_state.name = "Nevada"
fs.new(another_state)
fs.save()
print("Another State: {}".format(another_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new City
new_city = City()
new_city.name = "New_York"
fs.new(new_city)
fs.save()
print("New City: {}".format(new_city))

# Create a new City2
new_city2 = City()
fs.new(new_city2)
fs.save()
print("New City2: {}".format(new_city2))

# All(arg=None)
all_objs = fs.all()
print("All: {}".format(len(all_objs.keys())))
for key in all_objs.keys():
    print(all_objs[key])

# arg = State
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Delete(no args)
fs.delete()

# All States
all_states = fs.all(State)
print("All States after del without arg: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Delete the new State
fs.delete(new_state)

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Delete(args does not exist)
some_state = {}
fs.delete(some_state)

# All States
all_states = fs.all(State)
print("All States after empty obj arg: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])
