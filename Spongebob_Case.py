# Converts given string into Spongebob case because typing it by hand is not fun.
def spongebob_case():
    string = input("Please enter desired text to be converted into Spongebob case.\n")
    length = len(string)
    newstring = ""
    previous = ""
    for i in range(0, length):
        if string[i] == " " or string[i] in {"/", "'", ".", ",", "?", "!"}:
            temp = string[i].upper()
            newstring = newstring + temp
        elif i == 0 or previous == "lower":
            temp = string[i].upper()
            newstring = newstring + temp
            previous = "upper"
        else:
            temp = string[i].lower()
            newstring = newstring + temp
            previous = "lower"

    print(newstring)
