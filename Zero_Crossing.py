#Write a Python script that asks the user to enter a list of numbers 
input_list = list(input("Enter a list of numbers separated by spaces (can be positive or negative): ").split())

def zero_crossing(input_list):
    #split if were going from a positive to a negative number
    for i in range(0, len(input_list)):
        if float(input_list[i-1]) > 0 and float(input_list[i]) < 0:
            new_list = input_list[:i]
            return new_list
        elif float(input_list[i]) < 0 and float(input_list[i-1]) > 0:
            new_list = input_list[:i]
            return new_list

print(zero_crossing(input_list))
