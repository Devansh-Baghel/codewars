def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"
    return name

print(are_you_playing_banjo("rudrick"))
print(are_you_playing_banjo("Rudrick"))
print(are_you_playing_banjo("skal"))
print(are_you_playing_banjo("asdg"))