import math
import turtle
import random
t = turtle.Pen()
def make_shape():
	sides = input("How many sides mister?");sides = int(sides);size = math.sqrt(sides)*16;t.left(90);t.forward(size*3);t.right(90);t.clear();t.left(180);
	user_color = input("What color do you want mister?")
	t.color(user_color)
	t.begin_fill()
	for x in range(sides):
		t.forward(size);t.left(float((180-(((sides-2)*180)/sides))));
	t.end_fill();t.right(180-(sides*270));
make_shape()	
