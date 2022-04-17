#default argument

import random

""" 
print(chr(97))#asci value of a = 97
print(ord('A'), ord('Z')) #asci range (65-90)
print(ord('a'), ord('z')) #asci range (97-122)
 """



def generate_password(length = 8):

    l = ['!', '@', '#', '%', '&']
    upper = chr(random.randint(65,90))#converting integer into character by chr()
    lower = chr(random.randint(97,122))
    special = random.choice(l)
    digit = random.randint(10000,99999)
    password = upper + lower + special + str(digit) 
    l = random.sample(password,length)
    password = ("").join(l) #join() returns string 
    return password

result = generate_password()
print(result)


result = generate_password(5)
print(result)