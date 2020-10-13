
# Introduction to Python
import numpy as np
import pandas as pd


#Part I Python Basics

#The Python Interface
#1)
# Example, do not modify!
print(5 / 8)
# Print the sum of 7 and 10
print(7+10)
#2)
#Addition
print(7 + 10) 
#3)
# Addition, subtraction
print(5 + 5)
print(5 - 5)
#4)
# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# How much is your $100 worth after 7 years?
print(100*1.1**7)

#Variables and types
#1)
# Create a variable savings
x=5
y=x+2
# Print out savings
print (y)
x=['n','z','v','s','t','h','o']
print(x[-3] + x[-5])
print(x[-2] + x[-5])
print(x[-3] + x[-4])
savings = 100
print(savings)
#2)
# Create a variable savings
savings = 100
# Create a variable growth_multiplier
growth_multiplier = 1.1
# Calculate result
result = savings*growth_multiplier**7
# Print out result
print(result)
#3)
# Create a variable desc
desc = "compound interest"
# Create a variable profitable
profitable = True
#5)
savings = 100;
growth_multiplier = 1.1;
desc = "compound interest";
# Assign product of growth_multiplier and savings to year1;
year1= growth_multiplier*savings;
# Print the type of year1;
#print(year1)
print(type(year1))
# Assign sum of desc and desc to doubledesc;
doubledesc = desc + desc;
# Print out doubledesc;
print(doubledesc)
#6)
# Definition of savings and result
savings = 100
result = 100 * 1.10**7
# Fix the printout
#print("I started with $" +savings+ " and now have $" + result + ". Awesome!")
# Definition of pi_string
pi_string = "3.1415926"


#Part II Python lists

# Python lists
#1)
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
# Create list areas
areas=[hall, kit, liv, bed, bath]
# Print areas
print(areas)
#2)
# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv,"bedroom", bed, "bathroom", bath]
# Print areas
print(areas)
#3)
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom",bed],
         ["bathroom",bath]
         ]
# Print out house
print(house)


# Subsetting lists
#1)
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Print out second element from areas
print(areas[1])
# Print out last element from areas
print(areas[-1])
# Print out the area of the living room
print(areas[5])
#2)
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area=areas[3]+areas[-3]
# Print the variable eat_sleep_area
print(eat_sleep_area)
#3)
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Use slicing to create downstairs
downstairs=areas[0:6]
# Use slicing to create upstairs
upstairs=areas[6:10]
# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
#4)
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Alternative slicing to create downstairs
downstairs=areas[:6]
# Alternative slicing to create upstairs
upstairs=areas[6:]
print(downstairs)
print(upstairs)

# Manipulating lists. 

#1)
# # Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Correct the bathroom area
areas[-1]=10.50
# Change "living room" to "chill zone"
areas[4]="chill zone"
print(areas) 
#2)
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]
# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse",24.5]
print(areas_1)
# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
print(areas_2)

#3)
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Create areas_copy
#areas_copy = list(areas)
areas_copy = areas[:]
# Change areas_copy
areas_copy[0] = 5.0
# Print areas
print(areas)


# Part III Functions and packages

# Functions
#1)
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
# Paste together first and second: full
full = first + second
print(full)
# Sort full in descending order: full_sorted
full_sorted = sorted(full)
print(full_sorted)
# Print out full_sorted
full_sorted = sorted(full,reverse=1)
print(full_sorted)

# Methods
#1)
# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)
# Print out the number of o's in place
print(place.count('o'))
#2)
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Print out the index of the element 20.0
print(areas.index(20.0))
# Print out how often 9.50 appears in areas
print(areas.count(9.50))
#3)
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print(areas)
# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)
print(areas)
# Print out areas
print(areas)
# Reverse the orders of the elements in areas
areas.reverse()
# Print out areas
print(areas)

# Packages

#1)
# Definition of radius
r = 0.43
# Import the math package
import math
print(math.pi)
pi = math.pi
# Calculate C
C = 2*r*pi
print(C)
# Calculate A
A = pi*r**2
print(A)
# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))
#2)
# Definition of radius
r = 192500
# Import radians function of math package
from math import radians
phi = radians(12)
# Travel distance of Moon over 12 degrees. Store in dist.
dist = r*phi
# Print out dist
print(dist)


# Part IV Numpy

# NumPy

#1)
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
# Import the numpy package as np
import numpy as np 
# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out type of np_baseball
print(type(np_baseball))
#2)
# height is available as a regular list
# missing data
# Import numpy
import numpy as np
# Create a numpy array from height_in: np_height_in
np.np_height_in = np.array(height_in)
# Print out np_height_in
print(np.np_height_in)
# Convert np_height_in to m: np_height_m
np.np_height_m = (np.np_height_in)*0.0254
# Print np_height_m
print(np.np_height_m)
#3)
# height and weight are available as a regular lists

# Import numpy
import numpy as np
# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2
# Create the light array
light = np.array(bmi<21)
print(type(light))
light
# Print out light
print(light)
# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
len(bmi[light])
#4)
# height and weight are available as a regular lists
# Import numpy
import numpy as np
# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)
# Print out the weight at index 50
print(np_weight_lb[50])
# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])


# 2D Numpy Arrays
#1)
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np
# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out the type of np_baseball
print(type(np_baseball))
print(np_baseball.shape)
# Print out the shape of np_baseball
print(np_baseball.shape)
#2)
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np
# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out the shape of np_baseball
print(np_baseball.shape)
#3)
# baseball is available as a regular list of lists
# Import numpy package
import numpy as np
# Create np_baseball (2 cols)
np_baseball = np.array(baseball)
# Print out the 50th row of np_baseball
#print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]
print(np_weight_lb.shape)
# Print out height of 124th player
print(np_baseball[123,0])
#4)
# baseball is available as a regular list of lists
# updated is available as 2D numpy array
# Import numpy package
import numpy as np
# Create np_baseball (3 cols)
np_baseball = np.array(baseball)
# Print out addition of np_baseball and updated
print(np_baseball + updated)
# Create numpy array: conversion
conversion = [0.0254, 0.453592, 1]
# Print out product of np_baseball and conversion
print(np_baseball*conversion)

# Numpy basics statistics.
#1)
# np_baseball is available

# Import numpy
import numpy as np
import pandas as pd

# Create np_height_in from np_baseball
np_height_in = np.array(np_baseball[:,0])
print(np_height_in.shape)
# Print out the mean of np_height_in
print(np.mean(np_height_in))
# Print out the median of np_height_in
print(np.median(np_height_in))
#2)
# np_baseball is available

# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))
# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))
# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))
# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))
#3)
# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions =='GK']
#print(gk_heights) #ok working fine

# Heights of the other players: other_heights
other_heights = np_heights[np_positions !='GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
