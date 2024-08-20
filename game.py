import json

def loadSave():
    with open("save.json","r") as f:
        data = json.load(f)
        if data["level"] > 5:
            print("Wrong level! You have edited the save file :D")
            exit()
        elif data["level"] == 1:
            level1()
        elif data["level"] == 2:
            level2()
        elif data["level"] == 3:
            level3()
        elif data["level"] == 4:
            level4()
        elif data["level"] == 5:
            level5()
        else:
            print("We couldn't open up the save file!")
        f.close()    
def save(level):
    try:
        with open("save.json","r") as f:
            data = json.load(f)
            data["level"] = level
    except Exception as e:
        print(e)
        exit(1)
    with open("save.json","w") as f:
        json.dump(data,f)                
                                                
def level1():
    print('Type print("Hello World!") to write your first code!')
    code = ""
    isRun = ""
    while code != 'print("Hello World!")':
        code = str(input("Enter your code piece:\n"))
    while isRun != "run":
        isRun = str(input("Now type 'run' to run your code!\n"))
    eval(code)
    print("Good job! Now, you can move on with level two.")
    save(2)
def level2():
    print("In this level you are going to learn about variables.")
    x = ""
    isRun = ""
    code = ""
    while code != "x = 15":
        code = str(input("Enter 'x = 15 ' to declare your x variable as 15:\n"))
    x = 15
    while code != "print(x)":
        code = str(input("Good job mate! Now type 'print(x)' to print out your variable! Yes, you don't need to use quotes to print out your variables!\nQuotes are only used with texts. Use your next code piece now!\n"))                    
    while isRun != "run":
        isRun = str(input("Now, type 'run' to run your code! You don't need to type 'run' to run your real Python codes.\n"))
    eval(code)
    print("You are doing great!")
    save(3)
def level3():
    print("In this level you are going to learn how to do mathematical operations.\nLets assign 15 to x variable by writing 'x = 15' again.")
    code = ""
    isRun = ""
    x = ""
    while code != "x = 15":
        code = str(input(""))
    x = 15
    while code !="x = 15 + 40":
        code = str(input("Amazing! Now let's assign our x variable to 15 plus 40 by typing 'x = 15 + 40'\n"))
    x = 15 + 40
    while code != "print(x)":
        code = str(input("Wow, you are doing great! It is time to print out new value of x variable by typing 'print(x)'\n"))
    while isRun == "run":
        isRun =  str(input("Everything's ready to go! Type 'run' to run your amazing code!"))   
    eval(code)
    print("Nice!")
    save(4)
def level4():
    print("Are you aware of how much you have learnt? If you aren't, it is really a lot.\nNow, it is time to learn another way of doing mathematical operations with the value stored in variable.")                
    code = ""
    isRun = ""
    x = ""
    while code != "x = 15":
        code = str(input("Let's assign our x variable as 15 again. This time you have to do it yourself, don't worry you know the way :')!\n"))
    x = 15
    while code != "x = x + 40":
        code = str(input("Amazing, now it is time to do a mathematical operation with the variable's itself. Type 'x = x + 40' to do the operation.\n"))
    x = x + 40
    while code != "print(x)":
        code = str(input("Aye, captain! Now print out the variable's value. You know the way!\n"))
    while isRun != "run":
        isRun = str(input("Now do the last trick! Type 'run'\n"))
    eval(code)
    print("Aye aye, captain!")
    save(5)
def level5():
    print("Well done, now you are going to learn how to store text in a variable.\n")
    code = ""
    isRun = ""
    x = ""
    while code != 'x = "I love my family!"':
        code = str(input("""Well, since you are doing very good you should assign variable x to 'I love my family!' text by typing 'x = "I love my family!"'\nDon't worry you'll show it to your family at the end :')\n"""))
    x = "I love my family!"
    while code != "print(x)":
        code = str(input("Now, use your magic to print out the value stored in x variable.\n"))
    while isRun != "run":
        isRun = str(input("Run the code captain!\n"))
    eval(code)
    print("Good job! Now show them your work, I am sure they will be happy :D")
def main():
    loadSave()
while 1:
    main()        
        
                            
            
                       
