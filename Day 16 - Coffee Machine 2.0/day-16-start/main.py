from turtle import Turtle, Screen

# timmy is an object from the Class Turtle()
timmy = Turtle()
# shape and color are methods for my object timmy
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

# my_screen is an object from the Class Screen()
my_screen = Screen()
# canvheight is an attribute of my object
print(my_screen.canvheight)
# exitonclick is a method to my object. It will close the window only when I click
my_screen.exitonclick()
