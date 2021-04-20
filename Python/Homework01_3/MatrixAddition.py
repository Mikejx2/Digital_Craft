# Matrix Addition
# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is 
# represented as an list of lists:

# [ [2, -2], [5, 3] ]

# 1 3
# 2 4

# 5 2
# 1 0

# listA = [2, -2]

# listB = [5, 3]

# listC = [[],[]]

# # answer = [A*B for A,B in zip(listA,listB)]

# # print(listA, 
# #     listB, '=', answer)

# for i in range(len(listA)):
#     for j in range(len(listB)):
#         listC = [i+j]
#         print(listC)

# [ [2, -2],
#    [5, 3] ]
# Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices. Example: to add
list1 = [[2, 2], [5, 3]]  #[ [], []]
list2 = [[4, 7], [5, 2]]



for i in range(0,len(list1)): 
        for j in range(2): 
            print(f"[{i},{j}]")
        
    