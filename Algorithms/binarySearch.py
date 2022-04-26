#binary search in a sorted list

from operator import truediv


def binarySearch(l, key):
    if len(l)<0:
        return False
    else:
        mid = len(l)//2

        if l[mid] == key:
            return True
        elif l[mid] < key:
            return binarySearch(l[mid+1:], key)
        else:
            return binarySearch(l[:mid],key)



l = [100, 200, 300, 400, 500, 600, 700, 800, 900]
key = 800

result =  binarySearch(l,key)
print(result)