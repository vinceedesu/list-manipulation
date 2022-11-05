#random array
array = [29, 23, 47, 1, 8, 9, 17, 69, 420, 8008]

#Menu
print("Array:", array)
print("Menu: \n 1 -> Add an element \n 2 -> Insert an element \n 3 -> Modify an element \n 4 -> Delete an element \n 5 -> Arrange in ascending order \n 6 -> Arrange in descending order \n 7 -> Sum of all numbers \n 8 -> Know the Highest element \n 9 -> Know the lowest element")

#input for the user comand
command = int(input("What do you want to do? (1-9): "))

#Append input
if command == 1:
    addedElement = int(input("Enter the element to be added: "))
    array.append(addedElement)
    print("The new array is: ",array)
    
#insert
if command == 2:
    insertElement = int(input("Enter the element to be inserted: "))
    whereToInsert = int(input("Where would you like to insert it in the array?(0-9): "))
    array.insert(whereToInsert, insertElement)
    print("The new array is: ",array)

#modifying the said element with a new element
if command == 3:
    modifyElement = int(input("Enter the element to modify from ([29, 23, 47, 1, 8, 9, 17, 69, 420, 8008]): "))
    newElement = int(input("Enter the new element to replace: "))
    idx = array.index(modifyElement)
    array[idx] = newElement
    print("You modify element '",modifyElement,"' and change it to ", newElement,"\nThe new array now is: ", array)
    
#Deleting an element
if command == 4:
    deleteElement = int(input("Enter the element to delete([29, 23, 47, 1, 8, 9, 17, 69, 420, 8008]): "))
    array.remove(deleteElement)
    print("You removed ",deleteElement, "\nThe new array is: ", array)

#Sort accending
if command == 5:
    array.sort()
    print("The Ascending order is: ",array)

#Reversed sort
if command == 6:
    array.sort()
    array.reverse()
    print("The Decending order is: ",array)
    
#Sumation

if command == 7:
    total = sum(array)
    print("The total sum is ",total) 

#max value of array
if command == 8:
    maximum = max(array)
    print("The highest element in the array is ",maximum)

#min value of array
if command == 9:
    minimum = min(array)
    print("The lowest element in the array is ", minimum)
    