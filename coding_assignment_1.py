
print('hello person, input some Midi numbers please!')

frequencies = []

input = input()
input = int(input)
midiNums = [input]

for m in midiNums:
    m = 440*(2**((m-69)/12))
    frequencies.append(m)

for f in frequencies:
    print(f)


