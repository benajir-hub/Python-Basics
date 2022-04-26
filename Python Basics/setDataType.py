#Set
#1. Set are mutable
#2. All the elements should be unique
#3. Immutable elements in the set - int, float, tuple, str
#4. Unordered


from typing import Set


set1 = set()#empty set creation

print(set1)

set2 = {'James', 2, 45, 'Python', 'k'}
print(set2)
print(type(set2))

set2.add(100)#Adding element to the set
print(set2)

set2.remove(2)#Removing element from the set
print(set2)

#union()
#intersaction()
#difference()
#update()
#intersaction_update()


s1 = {10, 20, 30, 40, 50}
s2 = {40, 50, 60, 70, 80}

s3 = s1.union(s2)
print("Union of S1 and S2 is ", s3)

s4 = s1.intersection(s2)
print("Intersection of S1 and S2 is ", s4)

s5 = s1.difference(s2)#Elements that're not present in the S2 but are in the S1
print("Elements that're not present in the S2 but in the S1: ", s5)

s6 = s1.symmetric_difference(s2)#All the elements are present in s1 and s2 except the common elements
print("Elements that're uncommon in the S1 and S2: ", s6)

print(s1)
s1.update(s2)#update() automatically perform the union operation #update() returns none
print("Updated s1: ", s1)

s1.intersection_update(s2)#perform the intersaction operation between s1 and s2 and assign the value into s1
print("Latest s1 set after intersaction_update(): ", s1)

s1.difference_update(s2)#perform the difference operation between s1 and s2 and assign the value into s1
print("Latest s1 set after difference_update(): ", s1)



#issubset()

setOne = {100, 200, 300, 400, 500}
setTwo = {100, 200, 300}

print(setTwo.issubset(setOne)) # returns true if elements of setTwo is present in setTwo
print(setOne.issuperset(setTwo)) # returns true if all the elements of setTwo belongs to setOne



#typecasting
#listToSet

l = [10,20,30,40,50]
s = set(l)

print(s, type(s))


#convert two list into set and sort the elements 

l1 = [10,20,30,40,50]
l2 = [50, 100, 150, 200, 250, 300]

print(l1)
print(l2)

ls1 = set(l1)
ls2 = set(l2)

print(ls1)
print(ls2)

ls = ls1.union(ls2)

print(ls)

lst = sorted(ls)
print(lst)


#pop()
#remove()
#discard()
#clear()
#del

