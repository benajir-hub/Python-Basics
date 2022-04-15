#Tuple:
#immutable data Structure
#enumerate function

t = (10, 20, 20, 20, 20, 30, 40)
print(t, type(t))
print(t[1:])
print(t[-1])
print(t[:-1])
print(t[:3])
print(t.index(20))
print(t.count(20)) 



l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

""" 
#orthodox way enumerate
#enumerate retuns tuple basically
for index,value in enumerate(l):
    print( "On Index: ", index, "Value: ", value)
 """
for t in enumerate(l):
    print(t)#print the whole tuple
    print(t[0])#print only indexes
    print(t[-1])#print only values


#list to tuple conversion
l2 = [10,20,30,40,50]
print(l2, type(l2))
t2 = tuple(l2)
print(t2, type(t2))

#tuple to list conversion
t3 = (10,20,30,40,50)
print(t3, type(t3))
l3 = list(t3)
print(l3, type(l3))


#length of a tuple
#maximum element of the tuple
#minimum element of the tuple
print(len(t3))
print(max(t3))
print(min(t3))


#del t #delete the tuple from the memory
#print(t) #nameError





#help(tuple)