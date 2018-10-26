import turtle


def draw_art():
    tenlines = turtle.Turtle()
    tenlines.shape("turtle")
    counter = 0
    for i in range(1, 37):
        if counter == 0:
            tenlines.color("blue")
            counter += 1
        elif counter == 1:
            tenlines.color("red")
            counter += 1
        else:
            tenlines.color("yellow")
            counter = 0
        tenlines.right(10)
        tenlines.circle(100)


draw_art()

