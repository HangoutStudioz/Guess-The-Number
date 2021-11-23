import random
print("1 = You have only 10 chances")
print("2 = You Get The Direction Of The Words After 2 Chances")
print("3 = You Stats Is Saved In ""states.txt")
print("4 = Your Number Is Generated (1 - 100)")
print("5 = Enjoy Your Game!")
score = open("states.txt", "a")
a = score.write("1st Round")
# variable

num =  random.randint(1, 100)
Num_Guess = int(input("Enter your Guess"))
try:
    Num_Guess = int(input("Enter Your Guess"))
except:
    print("You Can Only Type A Number") 
Guess_limit = 10
Guess_Count = 0
#Main Function

while num != Num_Guess:
        Num_Guess = int(input("Enter your Guess:"))
        if num <= Num_Guess:
            print("No No Is Samller")
            Guess_Count += 1
            a = score.write("\nYour Number Was Smaller In This Condition")
        elif num >= Num_Guess:
         print("No No Is Bigger")
         Guess_Count += 1     
         a = score.write("\nYour Number Was Bigger In This Condition")
        if Guess_Count == Guess_limit:
            print("You Lost,")
            print("The Number Was",num)
            a = score.write("\nYou Lost")
               

if  Num_Guess == num:
            print("You Won!")
            print("The Number Was",num)
            a = score.write("\nYou Won") 
           
