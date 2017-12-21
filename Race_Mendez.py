#David Mendez
#this program will race 2 turtles one randomly generated one from a coordinant
#document, and will display results in the end
import turtle
import random
from time import sleep
#import turtle, random, and sleep
#create turtle dimensions and sizing for lines.
print ("Welcome to Turtule Race!")
#print intro message
def boundary(turt, width, height):
    turtle.penup()
    turtle.ht()
    turtle.seth(0)
    turtle.goto(-400,400)
    turtle.pendown()
    turtle.pensize(10)
    for i in range(2):
        turtle.forward (width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
#create a boundary
red = turtle.Turtle()
green = turtle.Turtle()
red.pensize(5)
green.pensize(5)
name1 = input("Enter the name of the red turtle: ")
name2 = input("Enter the name of the green turtle: ")
filename = input("Enter the name of the file for the red turtle's path: ")

Snuff = turtle.Turtle()
Snuff.penup
win = turtle.Screen()
win.title("Turtle Race v1.0")
win.bgcolor("white")
Snuff.color("black")
boundary(Snuff, 800, 800)

#create variables


#name1 = red
#name2 = green

#create shape of object
red.shape("turtle")
green.shape("turtle")
red.color("red")
green.color("green")
red.penup()
green.penup()
gx = int(-400)
gy = -200
rx = -400
ry = 200
red.goto(rx,ry)
green.goto(gx, gy)


fin = open(filename,"r")
xs = []
ys = []
for line in fin:
    line= line.strip() 
    parts = line.split (" ")
    xval =int(parts[0])
    yval =int(parts[1])
    xs.append(xval)
    ys.append(yval)
#create for and int statements    
totalr = 0
previousr = rx   
totalg = 0
#for statement
for i in range(len(xs)):
    
    red.pendown()
    red.goto(xs[i],ys[i])
    totalr += abs(previousr - xs[i])
    previousr = xs[i]
    
    gsteps = random.randint(2,20)
    gx += gsteps
    gy = gy + random.randint(-10,10)
    green.pendown()
    green.goto(gx,gy)
    totalg += gsteps

#if and elif statements for both outcomes    
    if xs[i] >= 400:
        print("%s wins!" % name1)
        break
    elif gx >= 400:
        print("%s wins!" % name2)
        break
print("%s went a distance of %d, while %s went a distance of %d." % (name1, totalr, name2, totalg))
sleep(5.0)
#create outro message
print ("Thank you for playing!")                     
#pring results for total and winner
