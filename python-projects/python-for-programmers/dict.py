# Dictionaries

dogs = {"Fido": 8, "Sean": 17, "Jane": 4}

print(dogs)

del(dogs["Sean"])  # delete an item from dictionary

for dog in dogs.keys():
    print(dog)

for dog in dogs.values():
    print(dog)

for dog in dogs.items():
    print(dog)
