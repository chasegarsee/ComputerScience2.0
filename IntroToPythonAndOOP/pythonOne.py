# Collections

# __ __ __LISTS // Arrays __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
# group of items we reference by Index                                    __
# Mutable - YES (we can change it :)                                      __
# Duplicate Items - YES                                                   __
#                                                                         __
colors = ["red", "orange", "yellow"]
#                                                                         __
# Add vs Insert                                                           __
colors.append("green")  # Adds to the end                                 __
colors.insert(2, "blue")  # Adds at Index                                 __
#                                                                         __
# Remove vs Pop vs Del                                                    __
colors.remove("orange")  # Removes item specified                         __
colors.pop()  # Removes last index                                        __
del colors[1]  # Removes item at Index                                    __
#                                                                         __
# Traversal                                                               __
#                                                                         __
for i in range(0, len(colors)):
    print(colors[i])
#                                                                         __
# Slices                                                                  __
primary_colors = colors[0:2]  # [keeps first: deletes second and beyond]
less_colors = colors[1:]  # [keeps first: deletes the rest]
few_colors = colors[:2]  # [first item you dont want: starts here]
#                                                                         __
# List Comprehentions                                                     __
new_colors = [c for c in colors if len(c) <= 5]
print(new_colors)
#                                                                         __
# __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
# __ __ __TUPLES __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
# group of items we reference by Index                                    __
# Mutable - NO (we can't change it :)                                     __
# Duplicate Items - YES                                                   __
#                                                                         __
animals = ("dog", "cat", "zebra")
# Cant ADD                                                                __
# Cant DELETE                                                             __
# CANT REMOVE                                                             __
# CANT CHANGE                                                             __
#                                                                         __
# Traversal
for animal in animals:
    print(animal)
#                                                                         __
# __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __

# __ __ __ SETS  __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
# Underscored Group of items                                              __
# Mutable - YES (CANNOT CHANGE, Only ADD)                                 __
# Duplicate Items - NO                                                    __
#                                                                         __
cities = {"Dallas", "Boston", "Austin", "Nashville"}
#                                                                         __
# ADD                                                                     __
cities.add("Denver")
cities.update(["New York", "San Fransico"])
#                                                                         __
# Traversal
for city in cities:
    print(city)
#                                                                         __
#                                                                         __
# __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __

# __ __ __ DICTIONARIES __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
# A Group of values we reference through their keys (JS OBJECT)            __
# Mutable - YES                                                            __
# Duplicate Items - YES                                                    __
grades = {
    # "key": "value"                                                       __
    "Math": 88,
    "Science": 33,
    "English": 44,
    "History": 99
}
#                                                                         __
# ACCESS                                                                  __
print(grades.get("History"))
#                                                                         __
# ADD                                                                     __
grades["Art"] = 81  # If NEW KEY creates new KVPair
#                                                                         __
# CHANGE / UPDATE                                                         __
grades["History"] = 89
#                                                                         __
# REMOVE
grades.pop("Science")  # removes KVPair specified
grades.popitem()  # Removes last item in list
#                                                                         __
# Traversal                                                               __
print(len(grades))
#                                                                         __
# __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
