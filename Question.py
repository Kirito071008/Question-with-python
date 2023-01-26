print("Hello")

question = (input("Do you love me?")) #First question
if (question == "yes" or question == "Yes" or question == "YES"): 
    print("Yes!") #everything you write here will appear if the answer is yes
    
   
else:
    print("Oh...") #everything you write here will appear if the answer was different to yes
    #If you wish, you can interrupt the code here if the answer is no by deleting print ("Oh...") and typing exit ()
    
next #use it to separate questions, it's not compulsory

question2 = (input("For real?")) #Second Question
if (question == "yes" or question == "Yes" or question == "YES"):
    print("<3") #everything you write here will appear if the answer is yes

else:
    print("...") #everything you write here will appear if the answer is different to yes
