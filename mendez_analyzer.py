#David Mendez
#variables must = 0 because they will count how many lines or words show up
#when using the loop.
lines = 0
word = 0
sent = 0
punct = 0                
cons = 0
vowel = 0
print ("*" * 50)# prints top border

print ("Welcome to Text Analyzer V1.0") #print greeting.

file = input("Enter name of gile to analyze: ") #set a variable name for the file

open_file = open(file, "r") # declare file name in order for the program to open it

for line in open_file: 

    line = line.strip().lower()#will strip all characters from beginning and end of a string 

    lines = lines + 1#converts letters to lowercase

    word = word + 1

    for ch in line:    # this counts everything that I set to zero in lines adds one for every
                       #given variable
        if ch in " ":
            word = word + 1

        if ch in ".?!":
            sent = sent + 1

        if ch in ".?!';:'\"(){}[]\\/":
            punct = punct + 1

        if ch in "bcdfghjklmnpqrstuvwxyz":
            cons = cons + 1

        if ch in "aeiou":
            vowel = vowel + 1

print("Results:") #prints results

print("Lines: %d" % lines)#assign print line for value of each variable

print("Words: %d" % word)

print("Sentences: %d" % sent)

print("Punctuation: %d" % punct)

print("Consonants: %d" % cons)

print("Vowels: %d" % vowel)

print("Thank you for using Text Analyzer V1.0.")#print good bye message
open_file.close()       

print("*" * 50 ) #prints bottom border
