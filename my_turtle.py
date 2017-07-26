import turtle

def draw_rect():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.color("yellow")
	brad.shape("turtle")
	brad.speed(2)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)

	window.exitonclick()

draw_rect()