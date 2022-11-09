# Dictionaries


# adds a stored dictionary item to a stored dictionary.
# joins 2 stored dictionaries
# Output all the contents of a stored dictionary

states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY"
}

states["WY"] = "Wyoming"

more_states = {
    "Alabama": "AL",
    "Alaska": "AK"
}

print(states)

states.update(more_states)

print(states)

# removes a dictionary item from a stored dictionary

print("\n Deleting entry from a dictionary")
# initialise dictionary 1 and 2
city_dict1 = {"AKL":"Auckland", "CHC":"Christchurch", "DUD":"Dunedin", "WLG":"Wellington"}
print("\nCity Dictionary 1:", city_dict1)
# remove the dictionary entry for Dunedin
del(city_dict1["DUD"])

print("\nUpdated city dictionary")
print(city_dict1)