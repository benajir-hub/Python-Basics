#explained code
def swap_case(s):
    str = s
    print("User Input: ", str)
    if len(str)<0:
        print("No input data!")
    else:
        #print(len(str))#size of string
        l = []
        for i in range(0, len(str)):
            pos = ord(str[i]) #fetch the ascii value of the character of index
            #print("position of letter", str[i], "is: ", pos)
            if  pos >= 97 and 122 >= pos :#defining the lower letter clause
                pos = pos - 32
                #print("New position value: ", pos)
                char = chr(pos)
                #print(char)
                l.insert(i, char)
                #l[i] = char
            elif pos >=67 and 90 >= pos:#defining the upper letter clause
                pos = pos + 32
                char = chr(pos)
                #l[i] = char
                l.insert(i, char)
            else:#defining the character except any letter
                #print("Invalid Character!!")
                #break
                l.insert(i,str[i])
    str = ("").join(l)#typecasting the list into string
    return str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print("Vice versa string: ", result)



"""     
#submitted code
def swap_case(s):
    str = s
    l =[]
    for i in range(0, len(str)):
        pos = ord(str[i])
        if  pos >= 97 and 122 >= pos :
            pos = pos - 32
            char = chr(pos)
            l.insert(i, char)
        elif pos >=67 and 90 >= pos:
            pos = pos + 32
            char = chr(pos)
            l.insert(i, char)
        else: 
            l.insert(i,str[i])

        
    str = ("").join(l)            
    return str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result) """

