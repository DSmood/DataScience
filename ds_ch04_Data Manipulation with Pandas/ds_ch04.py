# Include: 
# FILES: pickle

# Introduction to Python
import numpy as np
import pandas as pd
import pickle

###  Introduction to Python

#______________________________________________________
## Part I Python Basics
#______________________________________________________
# Transforming Data
#1)
# Print the head of the homelessness data
print(homelessness.head())
#2)
# Import pandas using the alias pd
import pandas as pd
# Print the values of homelessness
print(homelessness.values)
# Print the column index of homelessness
print(homelessness.columns)
# Print the row index of homelessness
print(homelessness.index)
#3)
# Sort homelessness by individual
homelessness_ind = homelessness.sort_values("individuals")
# Print the top few rows
print(homelessness_ind.head())
#4)
# Select the individuals column
individuals = homelessness["individuals"]
# Print the head of the result
print(individuals.head())
#5)
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"] >10000]
#ind_gt_10k = homelessness["individuals"] > 10000 
# See the result
print(ind_gt_10k)
#6)
# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness["region"].isin(["South Atlantic","Mid-Atlantic"])
south_mid_atlantic = homelessness[south_mid_atlantic]
#a = homelessness[south_mid_atlantic]
#print(a)
# See the result
print(south_mid_atlantic)
#7)
# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]
# Add p_individuals col as proportion of individuals
homelessness["p_individuals"]=homelessness["individuals"] / homelessness["total"]
# See the result
print(homelessness)
#8)
# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"]
# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] >= 20 ]
#print([high_homelessness])
# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending = False)
#print(high_homelessness_srt)    
# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state","indiv_per_10k"]]
# See the result
print(result)
#print(homelessness)


#______________________________________________________
##  Part II Aggregating data
#______________________________________________________

#1) Summary Statistics
# Print the head of the sales DataFrame
print(sales.head())
# Print the info about the sales DataFrame
print(sales.info())
# Print the mean of weekly_sales
print(sales["weekly_sales"].mean())
# Print the median of weekly_sales
print(sales["weekly_sales"].median())
#'''
#2)
# Print the maximum of the date column
print(sales["date"].max())
# Print the minimum of the date column
print(sales["date"].min())
#3)
# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column
print(sales["temperature_c"].agg(iqr))
#4)
# Sort sales_1_1 by date // sales_1_1 is created in Datacamp

#Original
#sales_1_1 = sales_1_1.sort_values("date", ascending = True)
# adapted
sales_1_1 = sales.sort_values("date", ascending = True)

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()
# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales["weekly_sales"].cummax()
# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

#1) Counting
# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset = ["store", "type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset = ["store", "department"])
print(store_depts.head())

# Subset the rows that are holiday weeks and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]].drop_duplicates("date")

# Print date col of holiday_dates
print(holiday_dates["date"])

#2) Counting categorical variables
# Count the number of stores of each type
# Count the number of stores of each type
store_counts = store_types["type"].value_counts()
print(store_counts)
 
# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize = True)
print(store_props)
print(store_depts.head())

# Count the number of departments of each type and sort
dept_counts_sorted = store_depts["department"].value_counts(sort = True)
print(dept_counts_sorted)

#print(departments)
# Get the proportion of departments of each type and sort
dept_props_sorted = store_depts["department"].value_counts(sort= True, normalize=True)
print(dept_props_sorted)
#3) Grouped summary statistics
# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()
#print(sales_all)
# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
#print(sales_A)
# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

#4) Calculations with groupby()
# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
print(sales_by_type)

# Get proportion for each type
#sales_propn_by_type = [sales_A, sales_B, sales_C]
sales_propn_by_type = sales_by_type / sales_by_type.sum()
print(sales_propn_by_type)
#5) Multiple gropuped sumaries

# Import NumPy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")["unemployment","fuel_price_usd_per_l"].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)



# Pivot tables
#1)Pivoting on one variable
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values = "weekly_sales", index = "type")

# Print mean_sales_by_type
print(mean_sales_by_type)
# Import NumPy as np

import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values = "weekly_sales", index = "type",aggfunc = [np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values = "weekly_sales", index = "type", columns = "is_holiday")

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

#2) Fill in missing values and sum values with pivot tables
# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values = "weekly_sales", index = "department",columns = "type", fill_value = 0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value = 0, margins = True))

#______________________________________________________
##  Part III Slicing and indexing
#______________________________________________________


#3) Setting & removing indexes
# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop = True))

#4) Subsetting with .loc[]
# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

#5) Setting multi-level indexes
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

# 
#1) Sorting by index values
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level=["city"], ascending=[True]))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country", "city"], ascending=[True, False]))

#2)Slicing index values
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Incorrectly subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])

# Subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan","Lahore"):("Russia","Moscow")])

#3) Slicing in both directions
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India","Hyderabad"):("Iraq","Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, "date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India","Hyderabad"):("Iraq","Baghdad"), "date":"avg_temp_c"])

#4) Slicing time series
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

# Set date as an index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])

#5) Subsetting by row/column number
# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[23,2])

# Use slicing to get the first 5 rows
print(temperatures.head())

# Use slicing to get columns 2 to 3
print(temperatures.iloc[:,2:4])

# Use slicing in both directions at once
print(temperatures.iloc[0:5, 2:4])

#'''
#6) Pivot temperature by city and year
# Add a year column to temperatures
# this solution runs error in vs code: Can only use .dt accessor with datetimelike values
#temperatures["year"] = temperatures["date"].dt.year # works in datacamp
# solution:
temperatures['year'] = pd.to_datetime(temperatures.date, format='%Y-%m-%d %H:%M')
print(temperatures['year'])
# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index = ["country", "city"], columns = "year")

# See the result
print(temp_by_country_city_vs_year)

#7) Subsetting pivot tables
# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt":"India"]

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi")]

# Subset in both directions at once
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi"),"2005":"2010"]

#8) Calculating on a pivot table
# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()
#print(mean_temp_by_year)
# Find the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")
print(mean_temp_by_city)
# Find the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
#'''

#_______________________________________________________________________________
##  Part IV Creating and Visualizing DataFrames
#_______________________________________________________________________________

#'''
# Which avocado size is most popular?
#1) # Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
#nb_sold_by_size = avocados["nb_sold"].cumsum()
#nb_sold_by_size = avocados["nb_sold"].sum()
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

print(nb_sold_by_size)
# Create a bar plot of the number of avocados sold by size
#avocados_by_size.plot(kind = "bar")
nb_sold_by_size.plot(kind = "bar")
# Show the plot
#plt.show()
#'''

#2) Changes in sales over time
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()
# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind = "bar")
# Show the plot
#plt.show()


#3) Avocado supply and demand
# Scatter plot of nb_sold vs avg_price with title
avocados.plot(x="nb_sold", y="avg_price", kind = "scatter", title="Number of avocados sold vs. average price")
# Show the plot
#plt.show()

#4) Price of conventional vs. organic avocados
# Histogram of conventional avg_price 
avocados[avocados["type"]=="conventional"]["avg_price"].hist()
# Histogram of organic avg_price
avocados[avocados["type"]=="organic"]["avg_price"].hist()
# Add a legend
plt.legend(["conventional","organic"])
# Show the plot
#plt.show()

#5) Finding missing values // Needs avocados_2016
'''
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
# Check individual values for missing values
print(avocados_2016.isna())
# Check each column for missing values
print(avocados_2016.isna().any())
# Bar plot of missing values by variable
print(avocados_2016.isna().sum().plot(kind="bar"))
# Show plot
#plt.show()
 
#6) Removing missing values
# Remove rows with missing values
avocados_complete = avocados_2016.dropna()
# Check if any columns contain missing values
print(avocados_complete.isna().any())

#7) Replacing missing values
# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()
# Show the plot
plt.show()
'''

#8) List of dictionaries
# Create a list of dictionaries with new data
avocados_list = [
    {"date":"2019-11-03", "small_sold":10376832, "large_sold":7835071},
    {"date":"2019-11-10", "small_sold":10717154, "large_sold":8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)

#9) Dictionary of lists
# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17","2019-12-01"],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}
# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)
# Print the new DataFrame
print(avocados_2019)

#10) CSV to DataFrame // needs airline_bumping.csv
'''
# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv("airline_bumping.csv")
# Take a look at the DataFrame
print(airline_bumping.head())

#11)DataFrame to CSV
# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values("bumps_per_10k", ascending = False)
# Print airline_totals_sorted
print(airline_totals_sorted)
# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv("airline_totals_sorted.csv")
'''