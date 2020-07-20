import numpy as np

width = 3
height = 5
input_count = width * height
unique_characters = 10

# Inputs
L0 = np.zeros([1, input_count], dtype=int)

# Outputs
L1 = np.zeros([1, unique_characters], dtype=int)

W = np.array([
    [1, 1, 1,   1, 0, 1,   1, 0, 1,   1, 0, 1,   1, 1, 1], #0
    [0, 1, 0,   1, 1, 0,   0, 1, 0,   0, 1, 0,   1, 1, 1], #1
    [1, 1, 1,   0, 0, 1,   0, 1, 0,   1, 0, 0,   1, 1, 1], #2
    [1, 1, 1,   0, 0, 1,   0, 1, 1,   0, 0, 1,   1, 1, 1], #3
    [1, 0, 1,   1, 0, 1,   1, 1, 1,   0, 0, 1,   0, 0, 1], #4
    [1, 1, 1,   1, 0, 0,   1, 1, 1,   0, 0, 1,   1, 1, 1], #5
    [1, 1, 1,   1, 0, 0,   1, 1, 1,   1, 0, 1,   1, 1, 1], #6
    [1, 1, 1,   0, 0, 1,   0, 1, 0,   0, 1, 0,   0, 1, 0], #7
    [1, 1, 1,   1, 0, 1,   1, 1, 1,   1, 0, 1,   1, 1, 1], #8
    [1, 1, 1,   1, 0, 1,   1, 1, 1,   0, 0, 1,   1, 1, 1] #9
])

data = open('input.txt', 'r').read().splitlines()
index = 0

# Set values of input
for i in range(height):
    for character in data[i]:
        if character == '*':
            L0[0][index] = 1
        else:
            L0[0][index] = -1

        index += 1

for output in range(unique_characters):
    acc = 0
    for input in range(input_count):
        acc += L0[0][input] * W[output][input]

    L1[0][output] = acc

# Print prediction
max = -100
for number in L1[0]:
    if number > max:
        max = number

predictions = []
for i in range(len(L1[0])):
    if L1[0][i] == max:
        predictions.append(i)

print('Predicted number(s): ', predictions)