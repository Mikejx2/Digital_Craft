# De-dup
# Given a list of numbers or strings, create a new list containing the 
# same elements as the first list, except with any duplicate values removed. 
# Print the list.

listA = [2, 4, 2, 6, 6, 10, 15, 10]

finalList = []

for i in listA:
    if i not in finalList:
        finalList.append(i)
print(finalList)