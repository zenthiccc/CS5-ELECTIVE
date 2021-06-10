# Use this editor to write your program for the exercise
import math

diameter = int(input("Enter diameter: "))
price = int(input("Enter pizza price: "))

radius = diameter/2
area_of_Circle = math.pi * radius **2

cost_per_square_inch = price/area_of_Circle

print("The cost per square inch of your pizza is: " + str(cost_per_square_inch) + "/ inch squared")