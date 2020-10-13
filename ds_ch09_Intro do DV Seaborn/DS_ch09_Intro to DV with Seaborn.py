# DS_ch09_Intro to DV with Seaborn
___________________________________________________________________________________
##  Part I Introduction to Seaborn
___________________________________________________________________________________
'''
#1)Making a scatter plot with lists
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns


#2)Making a count plot with a list
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()


#3)"Tidy" vs. "untidy" data
# Import Pandas
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())


#4)Making a count plot with a DataFrame
# Import Matplotlib, Pandas, and Seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x='Spiders', data=df)

# Display the plot
plt.show()


#5)Hue and scatter plots
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location")

# Show plot
plt.show()


#6)Hue and count plots

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors
palette_colors = {'Rural': "green", 'Urban': "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x='school', data=student_data, hue='location', palette=palette_colors)

# Display plot
plt.show()

'''

___________________________________________________________________________________
##  Part II Visualizing Two Quantitative Variables
___________________________________________________________________________________

'''
#1)Creating subplots with col and row
# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3", 
                data=student_data,
                kind='scatter')
# Show plot
plt.show()

# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter",
            col="study_time")
# Show plot
plt.show()

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")
# Show plot
plt.show()

#2)Creating two-factor subplots
# Create a scatter plot of G1 vs. G3
sns.relplot(x='G1',y='G3', data=student_data, kind='scatter')

# Show plot
plt.show()


#3)Changing the size of scatter plot points
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower",
            y="mpg",
            data=mpg,
            kind="scatter",
            size="cylinders")
# Show plot
plt.show()

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders",
            hue='cylinders')

# Show plot
#plt.grid()
plt.show()

#4)Changing the style of scatter plot points
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x='acceleration',
            y='mpg',
            data=mpg,
            kind='scatter',
            style='origin',
            hue='origin')
# Show plot
plt.show()


#5)Interpreting line plots
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(x='model_year', y='mpg', data=mpg,
            kind='line')
# Show plot
plt.show()


#6)Visualizing standard deviation with line plots
# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line",
            ci='sd')
# Show plot
plt.show()


#7)Plotting subgroups in line plots
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot of model year vs. horsepower
sns.relplot(x='model_year', y='horsepower',
            data=mpg,
            kind='line',
            ci=None)
# Show plot
plt.show()

'''
__________________________________________________________________________________
##  Part III Visualizing a Categorical and a Quantitative Variable
___________________________________________________________________________________

'''
#1)Count plots
# Create count plot of internet usage
sns.catplot(x='Internet usage',
            data=survey_data,
            kind='count'
            )
# Show plot
plt.show()

# Change the orientation of the plot
sns.catplot(y="Internet usage", data=survey_data,
            kind="count")

# Show plot
plt.show()

# Create column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count",
            col="Age Category"
            )

# Show plot
plt.show()


#2)Bar plots with percentages
# Create a bar plot of interest in math, separated by gender
sns.catplot(x="Gender",
            y="Interested in Math",
            data=survey_data,
            kind="bar")
# Show plot
plt.show()


#3)Customizing bar plots
# Create bar plot of average final grade in each study category
sns.catplot(x="study_time",
            y="G3",
            data=student_data,
            kind="bar"
            )
# Show plot
plt.show()

# Rearrange the categories
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"]
            )
# Show plot
plt.show()

# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=["<2 hours", 
                   "2 to 5 hours", 
                   "5 to 10 hours", 
                   ">10 hours"],
                   ci=None)
# Show plot
plt.show()

#4)Create and interpret a box plot
# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="box",
            order=study_time_order)

# Show plot
plt.show()


#5)Omitting outliers
# Create a box plot with subgroups and omit the outliers
sns.catplot(x="internet",
            y="G3",
            data=student_data,
            kind="box",
            hue="location",
            sym="")
#hue to create parameter to create subgroups.
#sym to not display the outliers.
# Show plot
plt.show()


#6)Adjusting the whiskers
# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=0.5)
#By default, the whiskers extend to 1.5 * the interquartile range.
#Make them extend to 2.0 * IQR: whis=2.0
#Show the 5th and 95th percentiles: whis=[5, 95]
#Show min and max values: whis=[0, 100]
# Show plot
plt.show()

# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[5, 95])
# Show plot
plt.show()

# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])
            
#By default, the whiskers extend to 1.5 * the interquartile range
#Make them extend to 2.0 * IQR: whis=2.0
#Show the 5th and 95th percentiles: whis=[5, 95]
#Show min and max values: whis=[0, 100]
# Show plot
plt.show()

#7)Customizing point plots
# Create a point plot of family relationship vs. absences
sns.catplot(x="famrel",
            y="absences",
            data=student_data,
            kind="point")
# Show plot
plt.show()

# Add caps to the confidence interval
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2)
# Show plot
plt.show()

# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2,
            join=False)
# Show plot
plt.show()

#8)Point plots with subgroups
# Create a point plot with subgroups
sns.catplot(x="romantic",
            y="absences",
            data=student_data,
            kind="point",
            hue="school"
            )
# Show plot
plt.show()

# Turn off the confidence intervals for this plot
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None)
# Show plot
plt.show()

# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator=median)
# Show plot
plt.show()
'''
___________________________________________________________________________________
##  Part IV Customizing Seaborn Plots
___________________________________________________________________________________

''' 
#1)Changing style and palette
# Set the style to "whitegrid"
sns.set_style("whitegrid")
# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]
sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)
# Show plot
plt.show()

# Set the color palette to "Purples"
sns.set_style("whitegrid")
sns.set_palette("Purples")
# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]
sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)
# Show plot
plt.show()

# Change the color palette to "RdBu"
sns.set_style("whitegrid")
#sns.set_palette("Purples")
sns.set_palette("RdBu")
# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]
sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)
# Show plot
plt.show()


#2)Changing the scale
# Set the context to "paper"
sns.set_context("paper")
# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")
# Show plot
plt.show()

# Change the context to "notebook"
sns.set_context("notebook")
# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")
# Show plot
plt.show()

# Change the context to "talk"
sns.set_context("talk")
# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")
# Show plot
plt.show()

# Change the context to "poster"
sns.set_context("poster")
# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")
# Show plot
plt.show()

#3)Using a custom palette
# Set the style to "darkgrid"
sns.set_style("darkgrid")
sns.set_palette(["#39A7D0","#36ADA4"])
# Set a custom color palette
# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")
# Show plot
plt.show()


#4)FacetGrids vs. AxesSubplots
# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")
# Identify plot type
type_of_g = type(g)
# Print type
print(type_of_g)


#5)Adding a title to a FacetGrid object
# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle("Car Weight vs. Horsepower")

# Show plot
plt.show()


#6)Adding a title and axis labels
# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")
# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")
# Show plot
plt.show()

# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")
# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")
# Add x-axis and y-axis labels
g.set(xlabel="Car Model Year",
      ylabel="Average MPG")
# Show plot
plt.show()

#7)Rotating x-tick labels
# Create point plot
sns.catplot(x="origin", 
            y="acceleration", 
            data=mpg, 
            kind="point", 
            join=False, 
            capsize=0.1)

# Rotate x-tick labels
plt.xticks(rotation=90)

# Show plot
plt.show()


#8)Box plot with subgroups
# Set palette to "Blues"
sns.set_palette("Blues")

# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data, 
                kind="box", hue="Interested in Pets")

# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle("Age of Those Interested in Pets vs. Not")

# Show plot
plt.show()


#9)Bar plot with subgroups and subplots
# Set the figure style to "dark"
sns.set_style("dark")

# Adjust to add subplots per gender
g = sns.catplot(x="Village - town", y="Likes Techno", 
                data=survey_data, kind="bar",
                col="Gender")

# Add title and axis labels
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence", 
       ylabel="% Who Like Techno")

# Show plot
plt.show()
'''