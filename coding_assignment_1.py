# def CalculateFrequency(fund_frequency, num_harmonics):
#     # Making an empty list to store the harmonics that we will return!
#     harmonics = []
#     for i in range(1, num_harmonics + 1):
#         # Calculate the new frequency!
#         new_freq = fund_frequency * i
#         harmonics.append(new_freq)
#     return harmonics


n= int(input("Enter a number "))
for i in range(1, n):
    print(i*(n-1))