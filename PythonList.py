""" Author @MEET MEHTA """
#In this program we will see about list() function and its different attributes.
List=['Maths','Physics',20,80,1010,12,'MEET','MEHTA']
List1=[1,2,3,4,5]
List2=[6,7,8,9,10,6,6,7,6,7,6,7]
List.append(2020) # 2020 will be added to the list
print(List)
List.insert(2,'MEHTA') #MEHTA will be added at position 2 in the list
print(List)
List1.extend(List2) #List2 will be append to List1
print(List1)
print(sum(List1)) # prints the sum of all the values of List1, if string iss present in the list, it will show an error.(TypeError)
print(len(List2)) # prints the length of the specified list
print(List2.index(6)) # Returns the occurence of the specified number
print(min(List2)) #prints the minimum value of the specified list
print(max(List2)) #prints the maximum of the list
sorted(List1)
print(List1)# prints the list in ascending order
print(List1.pop())# prints the last element of the list
print(List1.pop(0))# prints the specific indexed element of the list
del List1[2]# deletes the specific indexed value from the list
print(List1)
List1.remove(3)# removes the specific element from the list
print(List1)
