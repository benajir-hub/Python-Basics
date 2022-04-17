#keyword argument

def validate(username, password):
    if username == "ABC" and password == "Abc@123":
        print ("Valid username and password!")
    else:
        print("Invalid username and password!")

validate("ABC", "Abc@123")
validate("Abc@123", "ABC") #order matters -will print else section
validate(password = "Abc@123", username = "ABC") #keywords are defined as arguments