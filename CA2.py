typesList = ["int", "str", "bool", "float"] 
def DataEval():
    for item in typesList:
        if item == "int":
            if isinstance(eval(input(f"Enter a {item}: ")), int) == True:
                print("int")
            else:
                print("thats not a integer silly!")
        if item == "str":
            if isinstance(eval(input(f"Enter a {item}: ")), str) == True:
                print("str")
            else:
                print("thats not a string silly!")
        if item == "bool":
            if isinstance(eval(input(f"Enter a {item}: ")), bool) == True:
                print("bool")
            else:
                print("thats not a bool silly!")
        if item == "float":
            if isinstance(eval(input(f"Enter a {item}: ")), float) == True:
                print("float")
            else:
                print("thats not a float silly!")

DataEval()



input_tuple = tuple(input("Enter a list of numbers separated by spaces: ").split())
def odds(input_tuple):
    oddsList = []
    output = f"Your list contains {len(input_tuple)} items"
    for num in input_tuple:
        if eval(num) % 2 != 0:
            oddsList.append(num)
    output += f" and {len(oddsList)} odd numbers"
    return output

print(odds(input_tuple))


input_string = input("Enter a string: ")
def StringEval(input_string):
    UpperList = []
    LowerList = []
    NonList = []
    for char in input_string:
        if char.isupper():
            UpperList.append(char)
        elif char.islower():
            LowerList.append(char)
        else:
            NonList.append(char)
    output = f"Uppercase: {len(UpperList)}, Lowercase: {len(LowerList)}, Characters: {len(NonList)}"
    return output

print(StringEval(input_string))


input_string = input("Enter a string: ")
def StringEvalPrecentage(input_string):
    UpperList = []
    LowerList = []
    NonList = []
    for char in input_string:
        if char.isupper():
            UpperList.append(char)
        elif char.islower():
            LowerList.append(char)
        else:
            NonList.append(char)
    output = f"Uppercase: {len(UpperList)} ({len(UpperList)/len(input_string)*100}%), Lowercase: {len(LowerList)} ({len(LowerList)/len(input_string)*100}%), Characters: {len(NonList)} ({len(NonList)/len(input_string)*100}%)"
    return output

print(StringEvalPrecentage(input_string))

