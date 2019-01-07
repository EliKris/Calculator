#The start of the program
#Trying to make the user input fetuare for the calculator
#The print functions are mostly made for telling the user what to do.
print("Type in the first nummber and press enter")
FI = int(input("Enter first nummber here:")) #This is the first input for the calculator
print("Type in the second nummber and press enter")
SI = int(input("Enter second nummber here:")) #This is the second input for the calculator
print("Type in the operator and press enter (Exampels, +, -, *, /)")
V = (input("Enter The Operator here:")) #This is the input for the operator, things like +, -, and * 
ASVR = FI + V + SI   #This is the part where we take all the inputs and put them together and get the answer
print(ASVR) #Now we have the answer and can print it out to the user
