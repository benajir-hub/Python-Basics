#1 Positional argument



def linear_search(l,key):
    
    for i in l:
        if i == key:
            return True
    else:
        return False


l = [10, 20, 30, 40, 50]
key = 40
result = linear_search(l,key)
if result == True:
    print(key, "found in the list")
else:
    print(key, "Not found")


