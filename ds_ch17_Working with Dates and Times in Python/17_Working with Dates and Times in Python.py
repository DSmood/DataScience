
# 17_Working with Dates and Times in Python

___________________________________________________________________________________
##  Part I Dates and Calendar
___________________________________________________________________________________
'''
 
#1)Which day of the week?
# Import date from datetime
from datetime import date

# Import date from datetime
from datetime import date

# Create a date object
hurricane_andrew = date(1992, 8, 24)

# Import date from datetime
from datetime import date
# Create a date object
hurricane_andrew = date(1992, 8, 24)
# Which day of the week is the date?
#print(hurricane_andrew.year)
#print(hurricane_andrew.month)
#print(hurricane_andrew.day)
print(hurricane_andrew.weekday())

#2)How many hurricanes come early?
# Counter for how many before June 1
early_hurricanes = 0
# We loop over the dates
for hurricane in florida_hurricane_dates:
  # Check if the month is before June (month number 6)
  if hurricane.month < 6:
    early_hurricanes = early_hurricanes + 1
print(early_hurricanes)


#3)Subtracting dates
# Import date
from datetime import date
# Create a date object for May 9th, 2007
start = date(2007, 5, 9)
# Create a date object for December 13th, 2007
end = date(2007, 12, 13)
# Subtract the two dates and print the number of days
# returns the days between the 2 dates
print((end - start).days)


#4)Counting events per calendar month
# A dictionary to count hurricanes per calendar month
hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0,
		  				 7: 0, 8:0, 9:0, 10:0, 11:0, 12:0}
# Loop over all hurricanes
for hurricane in florida_hurricane_dates:
  # Pull out the month
  month = hurricane.month
  # Increment the count in your dictionary by one
  #hurricanes_each_month[month+1]
  hurricanes_each_month[month] +=1 
print(hurricanes_each_month)


#5)Putting a list of dates in order
# Print the first and last scrambled dates
print(dates_scrambled[0])
print(dates_scrambled[-1])

# Print the first and last scrambled dates
print(dates_scrambled[0]) # 1988
print(dates_scrambled[-1])# 2011
# Put the dates in order
dates_ordered = sorted(dates_scrambled)
# Print the first and last ordered dates
print(dates_ordered[0])  # 1950
print(dates_ordered[-1]) # 2017


#6)Printing dates in a friendly format
# Assign the earliest date to first_date
first_date = min(florida_hurricane_dates)
print(first_date)
# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.isoformat()
us = "Our earliest hurricane date: " + first_date.strftime("%m/%d/%Y")
print("ISO: " + iso)
print("US: " + us)


#7)Representing dates in different ways
# Import date
from datetime import date
# Create a date object
andrew = date(1992, 8, 26)
# Print the date in the format 'YYYY-MM'
print(andrew.strftime('%Y-%m'))

# Import date
from datetime import date
# Create a date object
andrew = date(1992, 8, 26)
# Print the date in the format 'MONTH (YYYY)'
print(andrew.strftime('%B (%Y)'))

# Import date
from datetime import date
# Create a date object
andrew = date(1992, 8, 26)
# Print the date in the format 'YYYY-DDD'
print(andrew.strftime('%Y-%j'))

'''
___________________________________________________________________________________
##  Part II Combining Dates and Times
___________________________________________________________________________________

'''
#1)Creating datetimes by hand
# Import datetime
from datetime import datetime
# Create a datetime object
dt = datetime(2017, 10, 1, 15, 26, 26)
# Print the results in ISO 8601 format
print(dt.isoformat())

# Import datetime
from datetime import datetime
# Create a datetime object
dt = datetime(2017,12,31,15,19,13)
# Print the results in ISO 8601 format
print(dt.isoformat())

# Import datetime
from datetime import datetime
# Create a datetime object
dt = datetime(2017, 12, 31, 15, 19, 13)
# Replace the year with 1917
dt_old = dt.replace(year=1917)
# Print the results in ISO 8601 format
print(dt_old)

#2)Counting events before and after noon
# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}
# Loop over all trips
for trip in onebike_datetimes:
  # Check to see if the trip starts before noon
  if trip['start'].hour < 12:
    # Increment the counter for before noon
    trip_counts['AM'] += 1
  else:
    # Increment the counter for after noon
    trip_counts['PM'] += 1
print(trip_counts)


#3)Turning strings into datetimes
# Import the datetime class
from datetime import datetime
# Starting string, in YYYY-MM-DD HH:MM:SS format
s = '2017-02-03 00:00:01'
# Write a format string to parse s
fmt = '%Y-%m-%d %H:%M:%S'
# Create a datetime object d
d = datetime.strptime(s, fmt)
# Print d
print(d)

# Import the datetime class
from datetime import datetime
# Starting string, in YYYY-MM-DD format
s = '2030-10-15'
# Write a format string to parse s
fmt = '%Y-%m-%d'
# Create a datetime object d
d = datetime.strptime(s, fmt)
# Print d
print(d)

# Import the datetime class
from datetime import datetime
# Starting string, in MM/DD/YYYY HH:MM:SS format
s = '12/15/1986 08:00:00'
# Write a format string to parse s
fmt = '%m/%d/%Y %H:%M:%S'
# Create a datetime object d
d = datetime.strptime(s, fmt)
# Print d
print(d)


#04)Parsing pairs of strings as datetimes
# Write down the format string
fmt = "%Y-%m-%d %H:%M:%S"
#print(onebike_datetime_strings) # format type '2017-10-01 15:23:25'
#print(type(onebike_datetime_strings))
# Initialize a list for holding the pairs of datetime objects
onebike_datetimes = []
# Loop over all trips
for (start, end) in onebike_datetime_strings:
  trip = {'start': datetime.strptime(start, fmt),
          'end': datetime.strptime(end, fmt)}
  # Append the trip
  onebike_datetimes.append(trip)


#05)Recreating ISO format with strftime()
# Import datetime
from datetime import datetime

# Pull out the start of the first trip
first_start = onebike_datetimes[0]['start']
print(first_start)
# Format to feed to strftime()
fmt = "%Y-%m-%dT%H:%M:%S"
# Print out date with .isoformat(), then with .strftime() to compare
print(first_start.isoformat())
print(first_start.strftime(fmt))


#06)Unix timestamps
# Import datetime
from datetime import datetime
# Starting timestamps
timestamps = [1514665153, 1514664543]
# Datetime objects
dts = []
# Loop
for ts in timestamps:
  dts.append(datetime.fromtimestamp(ts))
# Print results
print(dts)


#7)Turning pairs of datetimes into durations
# Initialize a list for all the trip durations
onebike_durations = []
print(onebike_datetimes[0]['start'])
print(onebike_datetimes[-1]['end'])

for trip in onebike_datetimes:
  # Create a timedelta object corresponding to the length of the trip
  #trip_duration = ____[____] - ____[____]
  trip_duration = trip['end'] - trip['start']
  
  # Get the total elapsed seconds in trip_duration
  trip_length_seconds = trip_duration.total_seconds()
  print(trip_length_seconds)
  # Append the results to our list
  onebike_durations.append(trip_length_seconds)


#8)Average trip time
# What was the total duration of all trips?
total_elapsed_time = sum(onebike_durations)
#print(total_elapsed_time)

# What was the total number of trips?
number_of_trips = len(onebike_durations)
  
# Divide the total duration by the number of trips
print(total_elapsed_time / number_of_trips)


#9)The long and the short of why time is hard
# Calculate shortest and longest trips
shortest_trip = min(onebike_durations)
longest_trip = max(onebike_durations)
# Print out the results
print("The shortest trip was " + str(shortest_trip) + " seconds")
print("The longest trip was " + str(longest_trip) + " seconds")

'''
___________________________________________________________________________________
##  Part III Time Zones and Daylight Saving
___________________________________________________________________________________
'''
 
#1)Creating timezone aware datetimes
# Import datetime, timezone
from datetime import datetime, timedelta, timezone
# October 1, 2017 at 15:26:26, UTC
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo = timezone.utc)
# Print results
print(dt.isoformat())

# Import datetime, timedelta, timezone
from datetime import datetime, timedelta, timezone
# Create a timezone for Pacific Standard Time, or UTC-8
pst = timezone(timedelta(hours=-8))
# October 1, 2017 at 15:26:26, UTC-8
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=pst)
# Print results
print(dt.isoformat())

# Import datetime, timedelta, timezone
from datetime import datetime, timedelta, timezone
# Create a timezone for Australian Eastern Daylight Time, or UTC+11
aedt = timezone(timedelta(hours=+11))
# October 1, 2017 at 15:26:26, UTC+11
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=aedt)
# Print results
print(dt.isoformat())


#2)Setting timezones
# Create a timezone object corresponding to UTC-4
edt = timezone(timedelta(hours=-4))

# Loop over trips, updating the start and end datetimes to be in UTC-4
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo=edt)
  trip['end'] = trip['end'].replace(tzinfo=edt)


#3)What time did the bike leave in UTC?

# Loop over the trips
for trip in onebike_datetimes[:10]:
  # Pull out the start and set it to UTC
  #dt = trip['start'].replace(tzinfo=timezone.utc)
  dt = trip['start'].astimezone(timezone.utc)
  
  # Print the start time in UTC
  print('Original:', trip['start'], '| UTC:', dt.isoformat())


#4)Putting the bike trips into the right time zone
# Import tz
from dateutil import tz

# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo=et)
  trip['end'] = trip['end'].replace(tzinfo=et)


#5)What time did the bike leave? (Global edition)
# Create the timezone object
uk = tz.gettz('Europe/London')
# Pull out the start of the first trip
local = onebike_datetimes[0]['start']
# What time was it in the UK?
notlocal = local.astimezone(uk)
# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

# Create the timezone object
ist = tz.gettz('Asia/Kolkata')
# Pull out the start of the first trip
local = onebike_datetimes[0]['start']
# What time was it in India?
notlocal = local.astimezone(ist)
# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

# Create the timezone object
sm = tz.gettz('Pacific/Apia')
# Pull out the start of the first trip
local = onebike_datetimes[0]['start']
# What time was it in Samoa?
notlocal = local.astimezone(sm)
# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())


#6)How many hours elapsed around daylight saving?
# Import datetime, timedelta, tz, timezone
from datetime import datetime, timedelta, timezone
from dateutil import tz
# Start on March 12, 2017, midnight, then add 6 hours
start = datetime(2017, 3, 12, tzinfo = tz.gettz('America/New_York'))
end = start + timedelta(hours = 6)
print(start.isoformat() + " to " + end.isoformat())

# Import datetime, timedelta, tz, timezone
from datetime import datetime, timedelta, timezone
from dateutil import tz
# Start on March 12, 2017, midnight, then add 6 hours
start = datetime(2017, 3, 12, tzinfo = tz.gettz('America/New_York'))
end = start + timedelta(hours=6)
print(start.isoformat() + " to " + end.isoformat())
# How many hours have elapsed?
print((end - start).total_seconds()/(60*60))

# Import datetime, timedelta, tz, timezone
from datetime import datetime, timedelta, timezone
from dateutil import tz

# Start on March 12, 2017, midnight, then add 6 hours
start = datetime(2017, 3, 12, tzinfo = tz.gettz('America/New_York'))
end = start + timedelta(hours=6)
print(start.isoformat() + " to " + end.isoformat())
# How many hours have elapsed?
print((end - start).total_seconds()/(60*60))
# What if we move to UTC?
#print((end.____(____) - start.____(____))\
#      .total_seconds()/(60*60))
print((end.astimezone(tz.gettz('UTC')) - start.astimezone(tz.gettz('UTC')))\
      .total_seconds()/(60*60))


#7)March 29, throughout a decade
# Import datetime and tz
from datetime import datetime
from dateutil import tz
# Create starting date
dt = datetime(2000, 3, 29, tzinfo = tz.gettz('Europe/London'))
# Loop over the dates, replacing the year, and print the ISO timestamp
for y in range(2000, 2011):
  print(dt.replace(year=y).isoformat())


#8)Finding ambiguous datetimes
# Loop over trips
for trip in onebike_datetimes:
  # Rides with ambiguous start
  if tz.datetime_ambiguous(trip['start']):
    print("Ambiguous start at " + str(trip['start']))
  # Rides with ambiguous end 
  if tz.datetime_ambiguous(trip['end']):
    print("Ambiguous end at " + str(trip['end']))


#9)Cleaning daylight saving data with fold
trip_durations = []
for trip in onebike_datetimes:
  # When the start is later than the end, set the fold to be 1
  if trip['start'] > trip['end']:
    trip['end'] = tz.enfold(trip['end'])
  # Convert to UTC
  start = trip['start'].astimezone(tz.gettz('UTC'))
  end = trip['end'].astimezone(tz.gettz('UTC'))

  # Subtract the difference
  trip_length_seconds = (end-start).total_seconds()
  trip_durations.append(trip_length_seconds)

# Take the shortest trip duration
print("Shortest trip: " + str(min(trip_durations)))

'''
___________________________________________________________________________________
##  Part IV Easy and Powerful: Dates and Times in Pandas
___________________________________________________________________________________
'''
 
#1)Loading a csv file in Pandas
# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', 
                    parse_dates = ['Start date', 'End date'])

# Print the initial (0th) row
print(rides.iloc[0])


#2)Making timedelta columns
# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds() # accepts .head()

print(rides['Duration'].head())


#3)How many joyrides?
# Create joyrides
joyrides = (rides['Start station'] == rides['End station'])
print(joyrides)
# Total number of joyrides
print("{} rides were joyrides".format(joyrides.sum()))

# Median of all rides
print("The median duration overall was {:.2f} seconds"\
      .format(rides['Duration'].median()))
#print("The median duration overall was rides['Duration'].mean() seconds")
      
# Median of joyrides
print("The median duration for joyrides was {:.2f} seconds"\
      .format(rides[joyrides]['Duration'].median()))


#4)It's getting cold outside, W20529
# Import matplotlib
import matplotlib.pyplot as plt
# Resample rides to daily, take the size, plot the results
rides.resample('D', on = 'Start date')\
  .size()\
  .plot(ylim = [0, 15])
# Show the results
plt.show()

# Import matplotlib
import matplotlib.pyplot as plt
# Resample rides to monthly, take the size, plot the results
rides.resample('M', on = 'Start date')\
  .size()\
  .plot(ylim = [0, 150])
# Show the results
plt.show()

#5)Members vs casual riders over time
# Resample rides to be monthly on the basis of Start date
monthly_rides = rides.resample('M', on = 'Start date')['Member type']

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())


#6)Combining groupby() and resample()
# Group rides by member type, and resample to the month
grouped = rides.groupby('Member type')\
  .resample('M', on = 'Start date')

# Print the median duration for each group
print(grouped['Duration'].median())


#7)Timezones in Pandas
# Localize the Start date column to America/New_York
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', ambiguous='NaT')
# Print first value
print(rides['Start date'].iloc[0])

# Localize the Start date column to America/New_York
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', 
                                						 ambiguous='NaT')
# Print first value
print(rides['Start date'].iloc[0])
# Convert the Start date column to Europe/London
rides['Start date'] = rides['Start date'].dt.tz_convert('Europe/London')
# Print the new value
print(rides['Start date'].iloc[0])

#8)How long per weekday?
# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['Start date'].dt.weekday_name
print(rides)

# Print the median trip time per weekday
print(rides.groupby('Ride start weekday')['Duration'].median())


#9)How long between rides?
# Shift the index of the end date up one; now subract it from the start date
rides['Time since'] = rides['Start date'] - (rides['End date'].shift(1))

# Move from a timedelta to a number of seconds, which is easier to work with
rides['Time since'] = rides['Time since'].dt.total_seconds()

# Resample to the month
monthly = rides.resample('M', on = 'Start date')

# Print the average hours between rides each month
print(monthly['Time since'].mean()/(60*60))

'''


