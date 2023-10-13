#Taking input size of the list from the user
n = int(input("Enter the size of the list: "))
li = [] #Creating an empty list
print("Enter the elements in the list:")
for i in range(n):
 x = int(input())
 li.append(x) #Entering elements in the list
print("List entered by the user is:\n",li)
st = set(li) #Converting list to set for removing all duplicate items
li = list(st) #Converting set back to list
#List containing no duplicate items is displayed
print("List containing no duplicate items is:\n",li)