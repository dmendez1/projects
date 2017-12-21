#David Mendez
#this program will generate a random password

#import random
import random
#print border
print ("*" *20)
print ("welcome to Password Generator V1.0")
fname = input("Enter the name of the file that contains the word list: ")
fvar = open(fname,"r")
#create input statement for ammount of password user chooses
password_count = int(input("How many passwords do you want to create? "))


words = []
for line in fvar:
   line = line.strip()
   if line != "":
       words.append(line)
#allows user to do as many passwords as they want
for i in range(password_count):
    #set variable values
    first_word = random.choice(words)
    second_word = random.choice(words)
    second_word = second_word.upper()
    third_word = random.choice(words)



    second_word_new = ""
#create for loop
    for letter in second_word:
        if  letter == "I":
            replacement = "1"
        elif letter == "O":
            replacement = "0"
        elif  letter == "S":
            replacement = "$"
        else:
            replacement = letter
        second_word_new = second_word_new + replacement


#generates a number ranging from 1000 to 9999
    num = random.randint(1000,9999)
    third_word = third_word + str(num)
    final_word =  first_word + second_word_new + third_word
    print("%s" %final_word)
#print outtro message
print ("Thank you for using Password Generator V1.0")     
print ("*" *20)
