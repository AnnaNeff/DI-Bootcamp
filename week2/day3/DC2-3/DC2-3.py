# Daily Challenge - Circle
# Last Updated: April 30th, 2025

# What You will learn :
# OOP dunder methods


# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

import math

class Circle:
    def __init__(self, l, parametr):
        self.par = parametr
        self.l = l
        if self.par == "r":
            self.r = self.l
            self.d = self.l * 2
        elif self.par == "d":
            self.r = self.l / 2
            self.d = self.l
        else: raise TypeError("Choose r (radius), or d (diametr)")
        


    def __str__(self):
        return f'Circle radius is {self.r}, diametr is {self.d}'
    
    def __repr__(self):
        return f"Circle(r={self.r:.2f})"
    
    def area(self):
        circ_area = math.pi * (self.r ** 2)
        return circ_area
    
    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(self.r + other.r, "r")
    
    def __lt__(self, other):
        if self.r < other.r:
            return True
        else:
            return False
        
    def __eq__(self, other):
        if self.r == other.r:
            return True
        else:
            return False
        

c1 = Circle(5, "r")
c2 = Circle(7, "d")
c3 = Circle(20, "d")
c4 = Circle(2, "r")

print(c1)
print(c2)
print(c1 + c2)
print((c1 + c2).area())
print(c1 > c2)

circles = [c1, c2, c3, c4]
circles.sort() 
print(circles)

import turtle

def draw_circles(sorted_circles):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    screen = turtle.Screen()
    screen.title("Sorted Circles by Radius")

    x = -300
    for c in sorted_circles:
        t.penup()
        t.setpos(x, -c.r)
        t.pendown()
        t.circle(c.r)
        
        t.penup()
        t.setpos(x, -c.r - 20)
        t.write(f"r={c.r:.1f}", align="center", font=("Arial", 10, "normal"))
        x += c.d + 20

    screen.mainloop()

circles_sorted = sorted([c1, c2, c3, c4])

draw_circles(circles_sorted)


        
        
