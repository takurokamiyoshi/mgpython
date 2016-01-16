# coding:shift-jis

import turtle
import math
import random

class Line:
	def __init__(self,slp,x0,y0):
		self.slp = float(slp)
		self.x0 = float(x0)
		self.y0 = float(y0)

	def get_y(self,x):
		return self.slp * (x-self.x0) + self.y0
		
	def get_x(self,y):
		return self.x0 + (y - self.y0) / self.slp

class Kame(turtle.Turtle):
	def __init__(self):
		super(Kame,self) .__init__()
		self.shape('turtle')
		self.shapesize(2,2)
		self.radians()
		self.width(10)
		self.getscreen().bgcolor('gray')
		self.pencolor('white')

	def hit_wall(self):
		xx = self.window_width() / 2.0
		yy = self.window_height() /2.0

		line = Line(math.tan(self.heading()),self.xcor(),self.ycor())
		rand_angle = math.pi * random.random()

		if self.towards(-xx,yy) > self.heading() >= self.towards(xx,yy):
			des_x = line.get_x(yy)
			des_y = yy
			turn_angle = self.heading() + rand_angle
		elif self.towards(-xx,-yy) > self.heading() >= self.towards(-xx,yy):
			des_x = -xx
			des_y = line.get_y(-xx)
			turn_angle = self.heading() - 0.5 * math.pi + rand_angle
		elif self.towards(xx,-yy) > self.heading() >= self.towards(-xx,-yy):
			des_x = line.get_x(-yy)
			des_y = -yy
			turn_angle = self.heading() - rand_angle
		else:
			des_x = xx
			des_y = line.get_y(xx)
			turn_angle = self.heading() - 0.5 * math.pi -rand_angle
		self.goto(des_x,des_y)
		self.right(turn_angle)

	def run(self):
		while True:
			self.hit_wall()
