
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
           
