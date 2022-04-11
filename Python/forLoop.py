#1. for iterating_variable in sequence
#2. range() denotes range(start,stop,step-size/distance)
#   range(5) 0 1 2 3 4 
#   range(10,100) 10 11 12 13 .... 99
#   range(10, 100, 5) 10 15 20 25 30 ... 95
#3. len() is combined with range() that iterate through a sequence using indexing
#4. NestedLoop
#outerLoop: for iterating_var1 in sequence:
#innerLoop: for iterating_var2 in sequence:


""" #1->
list = [1,2,3,4,5,6,7,8,9]

#printing the elements in the list
for i in list:
    print(i)

#printing summation  of the elements in list
sum = 0
for i in list:
    sum = sum+i

print("Summation of the list elements: ",sum)


#2->
num = int(input("Enter a number"))

for i in range(2,num,2):
    print(i)


#3->
list1 =['Justin', 'Trasten', 'Igor', 'Kamrul']
for i in range(len(list1)):
    
    #printing the list sequentially using index
    print("Hello ", list1[i])
 """

#4->
""" # User input for number of rows  
rows = int(input("Enter the rows:"))  
# Outer loop will print number of rows  
for i in range(0,rows+1):  
# Inner loop will print number of Astrisk  
    for j in range(i):  
        print("*",end = '')  
    print()   """


r = int(input("Enter the rows:"))
print("Total rows: ", r)
for i in range(0,r+1):
    for j in range(i):
        print("*", end =" ")
    print()
