nameList = ["Placeholder", "Jimmy", "Joe", "Jim", "James"]
nameList[0] = input("Please input the 1rst name\n")
gug = input("Please add a name to the list.\n")
nameList.append(gug)
print("There are" , len(nameList) , "names in nameList.")
print("The 3rd name is", nameList[2])
print("The last name is", nameList[-1])
print("The names from name #1 to name #3 are:", nameList[0:3]) 
print("The 4th name is", nameList[3])
print("The names from the beginning to the last name are:", nameList[:7])

print("Jimmy + James = " + (nameList[1] + nameList[4]))
nameList.pop(2)
print("Now the 3rd name is " + nameList[2])