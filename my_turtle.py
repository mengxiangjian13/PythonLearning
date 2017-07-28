import turtle

def draw_rect(brad):
	for x in range(1,5):
		brad.forward(100)
		brad.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.color("yellow")
	brad.shape("turtle")
	brad.speed(2)
	
	for x in xrange(1,37):
		draw_rect(brad)
		brad.right(10)

	window.exitonclick()

draw_art()