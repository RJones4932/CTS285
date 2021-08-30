## CTS 285
## M1HW - Calculator
## Reginald Jones
## August 22nd, 2021
##


"""
This is a program that allows the user to choose a option of a basic calculator.
The functions include: Add, Subtract, Multiply and Divide.
The Inputs will be two intergers that will give a result to the user.
"""


##Program Guidelines and Expections
##------------------------------------
##Menu
##User Chooses Option

##Option 1: Addition
##Option 2: Subtraction

##User gives first input
##User gives second input

##The two inputs should generate an output

##Output given. User then chooses to continue or quit program.
##If yes, Program returns to the top and runs again
##If no, Program ends.
##------------------------------------

#Greeting
print("\nSelect an Option")

#Function for the Calculator Menu
def cal_run():
    
    select = 0
    
    #While Loop for the menu
    while select !=5:
        
        #Display Menu
        menu()
        
        #User Input
        select = int(input("Enter Number:  "))
        
        #Selection 1 for Addition
        if select == 1:
            
            #Calls Addition Function
            add()
            
            #Note: This Nested If-Else Statement appears 
            #in other selections. 
            
            #Continue Screen if User wants to repeat the process
            print("\nContinue?")
            print("------------")
            print("1: Repeat")
            print("2: Main Menu")
            contin = int(input("\nEnter Number: "))
            
            #Repeats the following function once more
            if contin == 1:
                add()
                
            #Continues to Main Menu
            elif contin == 2:
                print("Returning to Menu")
                print()
                
            #Error Message    
            else:
                print("Invalid Number")
                
        #Selection 2 for Subtraction        
        elif select == 2:
            
            #Calls Subtraction Function
            sub()
            
            print("\nContinue?")
            print("------------")
            print("1: Repeat")
            print("2: Main Menu")
            contin = int(input("\nEnter Number: "))
            
            if contin == 1:
                sub()
            
            elif contin == 2:
                print("Returning to Menu")
                print()
                
            else:
                print("Invalid Number")
        
        #Selection 3 for Division        
        elif select == 3:
            
            #Calls Division Function
            div()
            
            print("\nContinue?")
            print("------------")
            print("1: Repeat")
            print("2: Main Menu")
            contin = int(input("\nEnter Number: "))
            
            if contin == 1:
                div()
            
            elif contin == 2:
                print("Returning to Menu")
                print()
                
            else:
                print("Invalid Number")
        
        #Selection 4 for Multiplication                
        elif select == 4:
            
            #Calls Multiplication Function
            mul()
            
            print("\nContinue?")
            print("------------")
            print("1: Repeat")
            print("2: Main Menu")
            contin = int(input("\nEnter Number: "))
            
            if contin == 1:
                mul()
            
            elif contin == 2:
                print("Returning to Menu")
                print()
                
            else:
                print("Invalid Number")
        
        #Exits the program        
        elif select == 5:
            print("\nGoodbye.")
        
        #Error Message
        else:
            print("Invalid Choice.")
            print()

#Menu                
def menu():

    print("1: Addition")
    print("2: Subtraction")
    print("3: Divide")
    print("4: Multiply")
    print("5: Exit")
    
#Addition
def add():
    print("\nAddition")
            
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))
            
    finalnum = num1 + num2
            
    print()
    print("Result:", num1, "+", num2, "=", finalnum)

#Subtraction
def sub():
    print("\nSubtraction")
            
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))
            
    finalnum = num1 - num2
            
    print()
    print("Result:", num1, "-", num2, "=", finalnum) 

#Multiplication
def mul():
    print("\nMultiplication")
            
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))
            
    finalnum = num1 * num2
            
    print()
    print("Result:", num1, "*", num2, "=", finalnum)

#Division    
def div():
    print("\nDivision")
            
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))
            
    finalnum = num1 / num2
            
    print()
    print("Result:", num1, "/", num2, "=", finalnum)
    
#Calls the function    
cal_run()