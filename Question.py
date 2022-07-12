print("Hello")

question = (input("Do you love me?")) #First question
if (question<"yes"): 
    print(":(") #everything you write here will appear if the answer is different
    #If you wish, you can interrupt the code here if the answer is no by deleting print (":(") and typing exit ()
   
else:
    print("Yes!") #everything you write here will appear if the answer was equal to (question<yes)
    
next #use it to separate questions

question2 = (input("For real?")) #Second Question
if (question>"yes"):
    print("Fuck") #everything you write here will appear if the answer is different

else:
    print("<3") #everything you write here will appear if the answer was equal to (question>yes)
