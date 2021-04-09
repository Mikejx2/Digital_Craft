# Matrix Addition
# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is 
# represented as an list of lists:

[ [2, -2], [5, 3] ]

1 3
2 4

5 2
1 0

listA = [2, -2]

listB = [5, 3]

answer = [A*B for A,B in zip(listA,listB)]

print(listA, 
    listB, '=', answer)
