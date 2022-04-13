#Write a program to find those numbers which are devisible by 5 and 7, between 1500 and 2700(both included).

for devident in range(1500,2700+1):
    if(devident%5 == 0):
        print(devident, end = " ")
        #print(devident)
        #print("Devided by 5: ", devident)
    elif(devident%7 == 0):
        print(devident, end = " ")
        #print("\t",devident)
        #print("Devided by 7: ", devident)
    else:
        pass    
else:
    print ("Programme ended here!")
