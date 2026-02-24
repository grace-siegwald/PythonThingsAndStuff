def CalculateFrequency(fund_frequency, num_harmonics):
    # Making an empty list to store the harmonics that we will return!
    harmonics = []
    for i in range(1, num_harmonics + 1):
        # Calculate the new frequency!
        new_freq = fund_frequency * i
        harmonics.append(new_freq)
    return harmonics

# take the user's input for both the frequency and number of harmonics to calculate!
input_freq = float(input("Enter the fundamental frequency: "))
input_harmonics = int(input("Enter the number of harmonics to calculate: "))

# this is where we actually call the function and print the result!
result = CalculateFrequency(input_freq, input_harmonics)
print("Harmonics:", result)