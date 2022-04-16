#Dictionary:
#1. Mutable
#2. Unordered
#3. Key should be unique
#4. keys should immutable : int, float, str, tuple

 
d = {1:'Benajir', 2:'Ridwan', 3:'Joy'}

print(type(d))
print(d)
print("First tenant is:",d[1]) #accessing vaue using keys
print(d.keys())
print(d.values())

Dict = {'Name':'Benajir', 'Age': 25, 'Dept': 'ASE'}
print(Dict)
Dict["Matrical No."] = 580236
print(Dict)
print("Student Name: %s "%Dict["Name"])#printing perticular value
Dict["Matrical No."] = 580236000 #updating a value of a key
print("Updated Matrical No: ", Dict)
print("Matrical No: %d "%Dict["Matrical No."])

#Data Retrieving
#get()
print(Dict.get("Age"))
print(Dict.get("year", "Key not found"))
#setdefault
print(Dict.setdefault("Age"))
#print(Dict.setdefault("old"))#return none if not found
print(Dict.setdefault("old", 2019))# set 2019 as value if not found any value at first
print(Dict)

#iterating a Dictionary
#iterating only keys
for i in Dict:
    print(i)

#iterating keys and values together
for key in Dict:
    print(key, Dict[key])

#values()
#keys()
#items()

print(Dict.keys())
print(Dict.values())
print(Dict.items())

#dictionary values addition automatically
d1 = {}

for key in range(1,11):
    d1[key] = key * key

print(d1)

#dictionary to tuple (key,value)
for d in d1.items():
    print(d)

#list into dictionary
l1 = [1,2,3,4,5]
l2 = [4,8,12,16,20]

#Zip()
#fromkeys()
d2 = dict(zip(l1,l2))
print(d2)

l3 = [1,2,3,4,5,6,7,8,9]
d3 = dict.fromkeys(l3)#default values are none
d3 = dict.fromkeys(l3,0)#default values are 0
print(d3)


#update()
d4 = {1:1, 2:4, 3:9, 4:16, 5:25}
d5 = {6:36, 7:49, 8:64, 9:81, 10:100}
d4.update(d5)#returns none
print(d4)

#pop()
#popitem()
#clear()
#del

r = d4.pop(2) #return the value of the key which was popped
print(d4, r)

r2 = d4.popitem() #return the key and the value which has been popped (mostly last item of the dictionary)
print(d4,r2)


d4.clear() #clear all the items from the dictionary
print(d4) #list is empty

del d4 #delete the library from the memory permanently
print(d4)#nameError

