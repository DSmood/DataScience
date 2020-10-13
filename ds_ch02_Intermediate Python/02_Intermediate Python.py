
# 02_Intermediate Python

___________________________________________________________________________________
##  Part I Matplotlib
___________________________________________________________________________________
'''
 
#1)Line plot (1)
# Print the last item from year and pop
print(year[-1])
print(pop[-1])
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year,pop)
# Display the plot with plt.show()
plt.show()


#2)Line Plot (2): Interpretation
# 2060


#3)Line plot (3)
# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])
# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap,life_exp)
# Display the plot
plt.show()


#4)Scatter Plot (1)
# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)
# Put the x-axis on a logarithmic scale
plt.xscale('log')
# Show plot
plt.show()


#5)Scatter plot (2)
# Import package
import matplotlib.pyplot as plt
# Build Scatter plot
plt.scatter(pop,life_exp)
# Show plot
plt.show()


#6)Build a histogram (1)
# Create histogram of life_exp data
plt.hist(life_exp)
# Display histogram
plt.show()


#7)Build a histogram (2): bins
# Build histogram with 5 bins
plt.hist(life_exp,bins=5)
# Show and clean up plot
plt.show()
plt.clf()
# Build histogram with 20 bins
plt.hist(life_exp,bins=20)
# Show and clean up again
plt.show()
plt.clf()


#8)Build a histogram (3): compare
# Histogram of life_exp, 15 bins
plt.hist(life_exp,bins=15)
# Show and clear plot
plt.show()
plt.clf()
# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950,bins=15)
# Show and clear plot again
plt.show()
plt.clf()


#9)Choose the right plot (1)
# Histogram


#10)Choose the right plot (2)
# Scatter plot


#11)Labels
# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 
# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'
# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)
# Add title
plt.title(title)
# After customizing, display the plot
plt.show()


#12)Ticks
# Scatter plot
plt.scatter(gdp_cap, life_exp)
# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']
# Adapt the ticks on the x-axis
plt.xticks([1000,10000,100000],['1k','10k','100k'])
# After customizing, display the plot
plt.show()


#13)Sizes
# Import numpy as np
import numpy as np
# Store pop as a numpy array: np_pop
np_pop = np.array(pop)
# Double np_pop
np_pop = np_pop*2
# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)
# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
# Display the plot
plt.show()


#14)Colors
# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2,c=col, alpha = 0.8)
# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])
# Show the plot
plt.show()


#15)Additional Customizations
# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)
# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])
# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')
# Add grid() call
plt.grid(True)
# Show the plot
plt.show()


#16)Interpretation
# The countries in blue, corresponding to Africa, 
# have both low life expectancy and a low GDP per capita

'''
___________________________________________________________________________________
##  Part II Dictionaries & Pandas
___________________________________________________________________________________
'''
 
#1)Motivation for dictionaries
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')
# Use ind_ger to print out capital of Germany
capital = capitals[ind_ger]
print(capital)


#2)Create dictionary
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid','france':'paris','germany':'berlin','norway':'oslo'}
# Print europe
print(europe)


#3)Access dictionary
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
# Print out the keys in europe
print(europe.keys())
# Print out value that belongs to key 'norway'
print(europe['norway'])


#4)Dictionary Manipulation (1)
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
# Add italy to europe
europe['italy'] = 'rome'
# Print out italy in europe
print('italy' in europe)
# Add poland to europe
europe['poland'] = 'warsaw'
# Print europe
print(europe)


#5)Dictionary Manipulation (2)
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }
# Update capital of germany
europe['germany'] = 'berlin'
# Remove australia
del(europe['australia'])
# Print europe
print(europe)


#6)Dictionariception
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
# Print out the capital of France
europe['france']['capital']
# Create sub-dictionary data
data = {'capital':'rome',
        'population':59.83
        }
# Add data to europe under key 'italy'
europe['italy']=data
# Print europe
print(europe)


#7)Dictionary to DataFrame (1)
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
# Import pandas as pd
import pandas as pd
# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {"country":names,
            "drives_right":dr,
            "cars_per_cap":cpc
                                }
# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
# Print cars
print(cars)


#8)Dictionary to DataFrame (2)
import pandas as pd
# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)
# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
# Specify row labels of cars
cars.index = row_labels
# Print cars again
print(cars)


#9)CSV to DataFrame (1)
# Import pandas as pd
import pandas as pd
# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')
# Print out cars
print(cars)


#10)CSV to DataFrame (2)
# Import pandas as pd
import pandas as pd
# Fix import by including index_col
cars = pd.read_csv('cars.csv',index_col=0)
# Print out cars
print(cars)


#11)Square Brackets (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Print out country column as Pandas Series
cars["country"]
print(cars["country"])
# Print out country column as Pandas DataFrame
cars[["country"]]
print(cars[["country"]])
# Print out DataFrame with country and drives_right columns
print(cars[["country","drives_right"]])


#12)Square Brackets (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Print out first 3 observations
print(cars[0:3])
# Print out fourth, fifth and sixth observation
print(cars[3:6])


#13)loc and iloc (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Print out observation for Japan
print(cars.loc['JPN'])
# Print out observations for Australia and Egypt
print((cars.iloc[[1,-1]]))


#14)loc and iloc (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Print out drives_right value of Morocco
print(cars.loc['MOR','drives_right'])
print(cars.iloc[-1,2])
# Print sub-DataFrame
print(cars.loc[['RU','MOR'],['country','drives_right']])
print(cars.iloc[[4,5],[1,2]])
cars


#15)loc and iloc (3)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)
# Print out drives_right column as Series
print(type(cars.loc[:,'drives_right']))
print(cars.loc[:,'drives_right'])
print(cars.iloc[:, 2])
# Print out drives_right column as DataFrame
print(type(cars.iloc[:,[2]]))
print(cars.iloc[:,[2]])
print(cars.loc[:,['drives_right']])
# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])
print(cars.iloc[:,[0,2]])


'''
___________________________________________________________________________________
##  Part III Logic, Control Flow and Filtering
___________________________________________________________________________________
'''
 
#1)Equality
# Comparison of booleans
True==False
# Comparison of integers
#(2 + 2) != 4
#(6+8) == 14
-5*15!=75
# Comparison of strings
"pyscript" == "PyScript" 
# Compare a boolean with an integer
True == 1


#2)Greater and less than
# Comparison of integers
x = -3 * 6
print(x>=-10)
# Comparison of strings
y = "test"
print("test<=y*y")
# Comparison of booleans
print(True>False)


#3)Compare arrays
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# my_house greater than or equal to 18
print(my_house >=18)
# my_house less than your_house
print(my_house <= your_house)


#4)and, or, not (1)
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0
# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen >10 and my_kitchen < 18)
# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen <14 or my_kitchen >17)
# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen*2 < your_kitchen*3)


#5)and, or, not (2)
# False


#6)Boolean operators with Numpy
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house >18.5,my_house <10))
# Both my_house and your_house smaller than 11
print(np.logical_and(my_house<11, your_house<11))


#7)Warmup
# medium


#8)if
# Define variables
room = "kit"
area = 14.0
# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")
# if statement for area
if area > 15.0:
    print("big place!")


#9)Add else
# Define variables
room = "kit"
area = 14.0
# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else:
    print("pretty small.")



#10)Customize further: elif
# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area>10:
    print("medium size, nice!")
else :
    print("pretty small.")


#11)Driving right (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Extract drives_right column as Series: dr
dr = cars.loc[:,'drives_right']
# Use dr to subset cars: sel
sel = cars[dr]
# Print sel
print(sel)


#12)Driving right (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Convert code to a one-liner
#dr = cars['drives_right']
sel = cars[cars['drives_right']]
# Print sel
print(sel)


#13)Cars per capita (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars.loc[:,'cars_per_cap']
many_cars = cpc>500
car_maniac = cars[many_cars]
# Print car_maniac
print(car_maniac)


#14)Cars per capita (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Import numpy, you'll need this
import numpy as np
# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
# Print medium
print(medium)


'''
___________________________________________________________________________________
##  Part IV Loops
___________________________________________________________________________________
'''
 
#1)while: warming up
# 3


#2)Basic while loop
# Initialize offset
offset = 8
# Code the while loop
while offset != 0:
    offset = offset-1
    print("correcting...")
    print(offset)


#3)Add conditionals
# Initialize offset
offset = -6
# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset-1
    else : 
      offset = offset+1    
    print(offset)


#4)Loop over a list
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Code the for loop
for area in areas :
    print(area)


#5)Indexes and values (1)
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas) :
    print("room " + str(index) + ": " + str(area))


#6)Indexes and values (2)
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))


#7)Loop over list of lists
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
    
# Build a for loop from scratch
for room,area in house:
    print("the " + str(room) + " is " + str(area)+ " sqm")


#8)Loop over dictionary
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
  
# Iterate over europe
#for key, value in europe.items():

#    print("the capital of " + str(key ) + " is " + str(value))
for country, capital in europe.items():
    
    print("the capital of " + str(country ) + " is " + str(capital))


#9)Loop over Numpy array
# Import numpy as np
import numpy as np
# For loop over np_height
for x in np_height:
    print(str(x) + " inches")
# For loop over np_baseball
#for np_height,np_weight in np_baseball
#    print(np_height, np_weight)
for val in np.nditer(np_baseball):
    print(val)


#10)Loop over DataFrame (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Iterate over rows of cars
# cars_per_cap,drives_right
for lab, row in cars.iterrows():
    print(lab)
    print(row)


#11)Loop over DataFrame (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab+":",row['cars_per_cap'])
    #print(row)


#12)Add column (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Code for loop that adds COUNTRY column
for lab,row in cars.iterrows():
#   cars.loc[lab,"COUNTRY"] = len(row["country"])
    cars.loc[lab,"COUNTRY"] = row["country"].upper()
# Print cars
    print(cars)


#13)Add column (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Use .apply(str.upper)
#for lab, row in cars.iterrows() :
#    cars.loc[lab, "COUNTRY"] = row["country"].upper()
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)

'''

___________________________________________________________________________________
##  Part V Case Study: Hacker Statistics
___________________________________________________________________________________
'''
 
#1)Random float
# Import numpy as np
import numpy as np
# Set the seed
np.random.seed(123)
# Generate and print random float
print(np.random.rand())


#2)Roll the dice
# Import numpy and set seed
import numpy as np
np.random.seed(123)
# Use randint() to simulate a dice
coin = np.random.randint(1,7)
print(coin)
# Use randint() again
coin = np.random.randint(1,7)
print(coin)


#3)Determine your next move
# Numpy is imported, seed is set
# Starting step
step = 50
# Roll the dice
dice = np.random.randint(1,7)
# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice >=3 and dice <6 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)
    
# Print out dice and step
print(dice,step)
#print(step)


#4)The next step
# Numpy is imported, seed is set
# Initialize random_walk
random_walk = [0]
# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]
    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)



#5)How low can you go?
# Numpy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0,step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)


#6)Visualize the walk
# Numpy is imported, seed is set
# Initialization
random_walk = [0]
for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# Plot random_walk
plt.plot(random_walk)
# Show the plot
plt.show()


#7)Simulate multiple walks
# Numpy is imported; seed is set
# Initialize all_walks (don't change this line)
all_walks = []
# Simulate random walk 10 times
for i in range(10):

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)


#8)Visualize all walks
# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)
# Plot np_aw and show
plt.plot(np_aw)
plt.show()
# Clear the figure
plt.clf()
# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)
# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()
print(type(np_aw_t))


#9)Implement clumsiness
# numpy and matplotlib imported, seed set
# Simulate random walk 250 times
all_walks = []
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()


#10)Plot the distribution
# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()


#11)Calculate the odds
# 78.4%


'''