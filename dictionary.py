#dictionary = a collection of {key:value} pairs 
#ordered and changeable. No duplicates
capitals = {"USA":"Washington D.C.",
            "India":"New Delhi", 
            "China":"Beijing", 
            "Russia":"Moscow"}
#print(dir(capitals)) 
#print(help(capitals)) 
#print(capitals.get("USA"))
#print(capitals.get("China"))
#if capitals.get("USA"):
#   print("That capital exists")
#else:
#   print("That capital doesn't exist")

capitals.update({"Germany":"Berlin"})
#use the update function to update new values or already existing values to your list 
print(capitals)

capitals.update({"USA":"Detroit"})

capitals.pop("China")
#removes item from dictionary

capitals.popitem()
#removes specified item from the dictionary

capitals.clear()
keys = capitals.keys() 
print(keys)

values = capitals.values()
for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

    items = capitals.items()
    for key, value in capitals.items():
        print(f"{key}: {value}")