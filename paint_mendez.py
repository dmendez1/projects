#David Mendez
#import math so such comands like math.ceil can be used.
import math 
#create a nice border.
print ( "**************************************************************")
#Print a name of the program.
print ("Welcome to Paint Calculator v 1.0")
#create a nice border.
print ( "**************************************************************")
#Assign inputs for each variable such as h,w,l.
h = int( input ( " Please enter the height of the room in inches:" ) )

w = int( input ( " Please enter the width of the room in inches:" ) )

l = int( input ( " Please enter the length of the room in inches:" ) )

frstp = input ( ( " Is this the first time the room has been painted (y or n) ?" ) )

do_you_p = input ( ( " Do you wish to paint the ceiling, too (y or n)?" ) )

hd = int( input ( " How many doors are there?" ) )

hw = int( input ( " How many windows are there?" ) )

costperg = float ( input ( " Enter the cost of paint per gallon: $" ) )

costperg2 = float( input ( " Enter the cost of primer per gallon: $" ) )
#incorporate the varaibles into equations.
uno = ( (w * h) * 2 )

duo = ( (l * h) * 2 )

windows = ( ( 5 * 3) * hw )

doors = ( ( 7 * 3) * hd )
ceil= 0
#create if statement for both user input posibilities.
if do_you_p  == "y" or do_you_p  == "Y":
    ceil = (w * l)
#Create more variables that hold variable equations.
total = (uno + duo - windows - doors + ceil)
cvtotal = (total/144)
paint = math.ceil(cvtotal/350)
price = math.ceil(cvtotal/200)
#use math.ceil to round the totals so outcome is right.
totcostwp =  (paint * costperg + price * costperg2) 
totcostp =  (paint * costperg)


#create if statement for both user input posibilities.
if frstp == "y" or frstp == "Y":
    print( " You need to buy " , paint, "gallons of paint and" , price , " gallons of primer." )
    print( " Your total cost will be.", totcostwp )
#create else statement for no option.
else:
    print( " You need to buy " ,paint, "gallons of paint" )
    print( " Your total cost will be.", totcostp )
#create good bye message.
print (" Thank you for using The Paint Calculator v 1.0")    
#create a nice border.
print ("*************************************************************")           
    
    
    




















