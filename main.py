first_and_last_name = "Esrom Abraham"
nickname = "Esrominus"
age = 17
has_used_python = True

hobbies = [
    "sports",
    "playing instruments",
    "going to church",
    "enjoying tv shows/movie",
    "hanging out with friends",
    "eating food",
]

fav_things = {
    "movie": "Shrek",
    "hobby": hobbies[1],
    "show/anime": "Naruto",
    "food": "fata (it's an eritrean dish that has spicy tomato sauce, bread, and sometimes yogurt all mixed together. Very amazing 🤤)",
    "number": 7
}

print("Hello world! My name is " + str(first_and_last_name) +
      ", but many of my friends call me by my first name or my gamer name: " +
      str(nickname) + ". I am " + str(age) + " years old.")

print("Has Python Experience: " + str(has_used_python))

for key in fav_things.keys():
    print(f"My favorite {key} is {fav_things[key]}.")

print("Here are some of my other hobbies: ")
print(*hobbies, sep=", ")

all_vars = dict(vars())
