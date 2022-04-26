#string formatting using curly braces, positional argument, keyword argument, % operator
#string stride
##maketrans
#translate
#upper()
#lower()
#title()
#maketrans
#translate
#strip()
#lstrip()
#rstrip()
#index()
#find()
#rfind()
#replace()

""" #1.formatting

#using Curly braces {}
print("{} and {} are the best friends".format("Rahim","Karim"))

#positional arguments
print("{1} and {0} are the best friends".format("Rahim","Karim"))

#keyword arguments
print("{a},{b},{c} are best friends".format(a = "Rahim", b = "Karim", c = "Selim"))

#python string formatting using % operator
#->binds the format specifiers to the values
integer = 100
float = 7.22
string = "Benajir"

print("I have %d full and %f changes remaining and my name is %s"%(integer, float, string))"""


""" #2.stride
s ="python sample string"


print(s[::-1])#reverse print of the string

#memory location unchanged
print(id(s))
print(s.capitalize())
print(id(s))

print()
#memory location changed

print(id(s))
s = s.capitalize()
print(s)
print(id(s))

#other string function
print(s.upper())
print(s.lower())
print(s.title())

print(s.isupper())"""



""" st = "HTML, CSS, PYTHON, JAVA, Django"

print(st)
print(st.split(","))
print(" ".join(st))"""


""" #maketrans
#translate

s1 = "abcd"
s2 = "1234"

s3 = "Python sample string abcd"

table = s3.maketrans(s1,s2)
result = s3.translate(table)

print(result) """



""" 
#index()
#find()
#rfind()
s = "HTML, CSS, PYTHON, PYTHON, PYTHON"
print("PYTHON" in s)
print(s.index("PYTHON"))#return index error if substring not found
print(s.find("PYTHON"))#return -1 if substring not found
print(s.rfind("PYTHON"))#traverse the string from right hand side"""

""" 
#strip()
#lstrip()
#rstrip()

string1 = "     This is Benajir    "
string2 = "****This is Benajir****"
print(string1.strip())
print(string2.strip("*"))
print(string2.rstrip("*"))
print(string2.lstrip("*")) """




""" #center
#ljust
#rjust

s = "python"
print(s.center(20))
print(s.center(20,"*"))
print(s.ljust(20,"*")) """


#replace()
s = "HTML, CSS, JAVA, PYTHON"
print(s.replace("HTML", "HTML5"))