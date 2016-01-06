import turtle
import random
kame = turtle.Turtle()
kame.shape('turtle')
kame.shapesize(2,2,3)
kame.forward(5000)
kame.right(90)
kame.circle(100)
kame.undo()
kame.home()
kame.window_width()
kame.goto(150,200)
while True:
	kame.left(random.randint(1, 360))
	kame.forward(15)
	if kame.distance(0, 0) > 200:
		kame.undo()
