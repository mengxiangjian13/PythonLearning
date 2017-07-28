import turtle

def draw_diamond(brad):
	for x in xrange(1,5):
		brad.forward(100)
		if x % 2 == 0:
			brad.right(120)
		else:
			brad.right(60)


def draw_flower():
	window = turtle.Screen()
	window.bgcolor("white")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(8)

	for x in xrange(1,73):
		draw_diamond(brad)
		brad.right(5)

	brad.right(90)
	brad.forward(250)


	window.exitonclick()

draw_flower()