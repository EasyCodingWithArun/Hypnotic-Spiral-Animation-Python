import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Hypnotic Spiral 🌀")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

n = 360  
hue = 0

for i in range(n):
    # Smooth color transition
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    pen.pencolor(color)
    
    # Spiral drawing
    pen.forward(i * 0.5)
    pen.left(59)  
    
    # Gradual zoom effect
    pen.width(1 + (i / 100))

    hue += 0.005  

# Finish
turtle.done()
