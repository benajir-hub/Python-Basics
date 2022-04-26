#code reuse
#modularity [easy to maintain easy to debug]
#In Python, call by reference means passing the actual value as an argument in the function.



def reverseValue(value):
    if type(value) == list or type(value) == str:
        reverse = value[::-1]
        #print( reverse )
        return reverse #commenting out this line will lead us to a "None" result
    else:
        temp = str(value)
        reverse = temp[::-1]
        return reverse



s = "Python"
l = [10, 20,30,40,50]
i = 63
#result = reverseValue(s)
print("Reversed String: ", reverseValue(s))
print("Reversed list: ", reverseValue(l))
print("Reversed integer: ", reverseValue(i))





