
def handleInput(prompt,expectedType,limit,multiChoice):
    while(True):
        inputType = ""
        inputLoop = True
        while(inputLoop):
            userInput = input(prompt)
            if(userInput):
                inputLoop = False
            else: print("No value entered !!! ***Try again ")
        try:
            userInput = int(userInput)
            if(userInput < 0):
                inputType = "negative"
            else: 
                inputType = "integer"    
        except ValueError:
            try:
                userInput = float(userInput)
                inputType = "float"
            except ValueError:
                inputType = "string"
            # below is check for limit of input, for number its numerical rage and number of words for sting input
        if (expectedType == inputType):
            if(limit == None):
                return userInput
            hasLimitError = checkLimitError(userInput,expectedType,limit,multiChoice)
            if(hasLimitError != True):
                return userInput
        else:
            print("**Error!!! {} value entered".format(inputType));            


def checkLimitError(userInput,expectedType,limit,multiChoice):
    if(expectedType == "string"):
        stringLength = len(userInput.split())
        if(stringLength > limit[1]): #checking if input has got multiple words
            print("**Error!!! word length should not exceed {}".format(limit[1]))
            return True
        if(multiChoice != None):  #chekcing if char input has only defined character input
            if(userInput in multiChoice):
                return False # user input is valid character hence error is false
            else:
                print("**Error!!! Enter valid character"); 
                return True    
    else:
        if(limit[1] == None):
            if(limit[0] > userInput):
                print("**Error!!! Number should be greater than {} ".format(limit[0]));
                return True
            else: return False
        if(limit[0] > userInput or userInput > limit[1]):
            print("**Error!!! Number should be in range of {} to {}".format(limit[0],limit[1]));
            return True
        else: return False
