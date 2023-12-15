print("Hello")

question = input("Do you love me?\n") #First question
if (question.lower == "yes" or question.lower == "y"):
    print("Yes!") #everything you write here will appear if the answer is yes
else:
    print("Oh...") #everything you write here will appear if the answer was different to yes
    #If you wish, you can interrupt the code here if the answer is no by deleting print ("Oh...") and typing exit ()
question2 = input("For real?\n") #Second Question
if (question2.lower == "yes" or question2.lower == "y"):
    print("<3") #everything you write here will appear if the answer is yes
else:
    print("...") #everything you write here will appear if the answer is different to yes
