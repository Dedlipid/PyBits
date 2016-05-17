import math
import turtle
import random
t = turtle.Pen()
def make_shape():
	sides = input("How many sides? ")
	sides = int(sides)
	size = input("How long should each side be?(In Pixels) ")
	size = int(size)
	t.forward(size*3)
	t.right(90)
	t.clear()
	t.left(180)
	user_color = input("What color do you want mister? ")
	t.color(user_color)
	t.begin_fill()
	for x in range(sides):
		t.forward(size)
		t.left(180-(((sides-2)*180.0)/sides))
	t.end_fill()
	t.right(sides*270.0)
make_shape()	
