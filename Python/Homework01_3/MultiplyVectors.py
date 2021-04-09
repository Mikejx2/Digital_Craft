# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:

# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]

listA = [2, 4, 5]

listB = [2, 3, 6]

answer = [A*B for A,B in zip(listA,listB)]

print(listA, 'x', listB, '=', answer)

# print(list(zip(listA,listB)))