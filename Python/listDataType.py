""" list1 = [1,'h', 'Python', 2]
print(list1) #printing the given list
print(id(list1)) #memory location of the list
print(type(list1)) #type of given list
print(list1[2:]) #list slicing
print(list1[0:2]) #list slicing
print(list1 + list1) #list concatenation using + operator
print(list1*3) #List repeation using * operator """


#List add element
from re import L


list2 = [10, 20, 30, 40, 50]
print(list2)
print(id(list2))
list2.append(60)#[add an element into the list2]
print(list2)
list2.extend([70, 80, 90])#[add multiple elements into the list2]
print(list2)
list2.append([70, 80, 90])
print(list2)
list2.extend("PYTHON")#extend method traverse through the string
print(list2)
list2.append("PYTHON")
print(list2)
list2.insert(1,10000)#add element into exact index of list
print(list2)
print(id(list2))

list3 = list2.copy()##copy() ->different memory location
print(id(list3))


for i in list2[::2]:
    print(i) 



#update of list
list4 = [10, 20, 30, 40, 50]
list4[3] = 333
print(list4)


#delete from list
#pop
#remove
#clear
#del
list5 = [10,20,30,40,50]
print(list5)
r = list5.pop()#last index item of the list just popped and stored in variable r

print(list5)
print("Popped element -> ", r)


r1 = list5.pop(1)#index one item popped
print(list5)
print("Popped element -> ", r1)

x = 10
print(list5)
list5.remove(x)#remove perticular element from the list
print(list5)
print("Removed element -> ", x)
print(list5)

#clear
list5.clear() # To clear the elements of the list
print(list5)

#del
del list5 #to delete a list completely from the memory
#print(list5) #nameError


l = [50, 20, 30, 10, 40]
print(l)

l. sort() # To sort the elements of a list #return none
print(l)
print(l.sort()) #return none
print(l)
print(l[::-1]) #sort descending
print(l)
l.sort()
print(l)
l.reverse()
print(l)

#sorted()

l2 = sorted(l)#return the sorted list
print(l2)
 
#index()
print(l2.index(30))#return the index of element in a list

#count()
l2.append(30)
print(l2)
print(l2.count(30))#return the count od element 30 in a list
