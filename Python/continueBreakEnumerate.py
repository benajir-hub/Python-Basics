#break
#continue
#enumerate
#for-else

lst = [10,20,30,40,50]
key = 400
sum = 0

for i in lst:
    #print (i)
    if i == key:
        print("Element found!!", end = "Which is: ")
        print (i)
        break
    else:
        #print("Element not found!!")
        continue
else:
    print("Element not found!!")
