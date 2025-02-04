
# 16_Cleaning Data in Python

___________________________________________________________________________________
##  Part I Common data problems
___________________________________________________________________________________
'''
 
#1)Numeric data or ... ?
# Print the information of ride_sharing
print(ride_sharing.info())
# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())


The user_type column has an finite set of possible values that represent groupings 
of data, it should be converted to category.


# Print the information of ride_sharing
print(ride_sharing.info())
# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())
# Convert user_type from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')
# Write an assert statement confirming the change
assert ride_sharing['user_type_cat'].dtype == 'category'
# Print new summary statistics 
print(ride_sharing['user_type_cat'].describe())


#2)Summing strings and concatenating numbers
# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')
#print(ride_sharing['duration_trim'])
# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')
#print(ride_sharing['duration_trim'])
# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration 
print(ride_sharing[['duration','duration_trim','duration_time']])
print(ride_sharing['duration_time'].mean())


#3)Tire size constraints
# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')
# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27
# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')
# Print tire size description
print(ride_sharing['tire_sizes'].describe())


#4)Back to the future
# Convert ride_date to datetime
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing["ride_date"])
#print(ride_sharing['ride_dt'])
# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())


#5)How big is your subset? Choose the correct usage of .duplicated() below:

#loans.duplicated(subset = ['first_name', 'last_name'], keep = False)
#Because subsetting on consumer metadata and not discarding any duplicate returns 
#all duplicated rows


#6)Finding duplicates
# Find duplicates
duplicates = ride_sharing.duplicated('ride_id', keep = False)
#print(duplicates)
# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values(by='ride_id')
# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])


#7)Treating duplicates
# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates(inplace=False)
print(ride_dup)
# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Group by ride_id and compute new statistics
#ride_unique = ride_dup.____('____').____(____).reset_index()
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset = 'ride_id', keep = False)
duplicated_rides = ride_unique[duplicates == True]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0


'''
___________________________________________________________________________________
##  Part II Text and categorical data problems
___________________________________________________________________________________
'''
 
#1)Finding consistency
# Print categories DataFrame
print(categories)
# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")
print('Safety: ', airlines['safety'].unique(), "\n")
print('Satisfaction: ', airlines['satisfaction'].unique(), "\n")

# cleanliness because it has an Unacceptable category.

# Find the cleanliness category in airlines not in categories
#creates a set in a df[column] and finds difference comparing to categories criteria
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])
# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)
# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])
# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)
# Print rows with inconsistent category
print(airlines[cat_clean_rows])
# Print rows with consistent categories only
print(airlines[~cat_clean_rows])


#2)Inconsistent categories
# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())


#3)Inconsistent categories
# Both 2 and 3 are correct.

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())
# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())
# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower() 
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})
# Remove white spaces from `dest_size`
airlines['dest_size'] = airlines['dest_size'].str.strip()
# Verify changes have been effected
print(airlines['dest_size'].unique())
print(airlines['dest_region'].unique())


#4)Remapping categories
# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']
# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, 
                                labels = label_names)
# Create mappings and replace (creating criteria)
mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', 
            'Thursday': 'weekday', 'Friday': 'weekday', 
            'Saturday': 'weekend', 'Sunday': 'weekend'}
airlines['day_week'] = airlines['day'].replace(mappings)


#5)Removing titles and taking names
# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.","")

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.","")

# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Miss","")

# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Ms.","")

# Assert that full_name has no honorifics
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False


#6)Keeping it descriptive
# Store length of each row in survey_response column
resp_length = airlines['survey_response'].str.len()

# Find rows in airlines where resp_length > 40
airlines_survey = airlines[resp_length > 40]

# Assert minimum survey_response length is > 40
#assert airlines['survey_response'].str.len().min() > 40
assert airlines_survey['survey_response'].str.len().min() > 40

# Print new survey_response column
print(airlines_survey['survey_response'])


'''
___________________________________________________________________________________
##  Part III Advanced data problems
___________________________________________________________________________________
'''
 
#1)Ambiguous dates
# All of the above are possible, as long as we investigate where our data comes from,
#  and understand the dynamics affecting it before cleaning it.


#2)Uniform currencies
# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'
# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] *1.1
# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'
# Print unique values of acct_cur
assert banking['acct_cur'].unique() == 'dollar'


#3)Uniform dates
# Print the header of account_opened
print(banking['account_opened'].head())

The 21-14-17 entry is erroneous and leads to an error.

# Print the header of account_opened
print(banking['account_opened'].head())
# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
# Infer datetime format (try to infer format)
infer_datetime_format = True,
#Return missing value for error
errors = 'coerce') 

# Print the header of account_opend
print(banking['account_opened'].head())
# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format = True,
                                           # Return missing value for error
                                           errors = 'coerce') 
# Get year of account opened
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')
# Print acct_year
print(banking['acct_year'])


#4)How's our data integrity?
# Store fund columns to sum against
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']
#print(banking.head(0))
# Find rows where fund_columns row sum == inv_amount
inv_equ = banking[fund_columns].sum(axis=1) == banking['inv_amount']
# Store consistent and inconsistent data
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]
# Store consistent and inconsistent data
print("Number of inconsistent investments: ", inconsistent_inv.shape[0])

# Store today's date and find ages
today = dt.date.today()
ages_manual = today.year - banking['birth_date'].dt.year
# Find rows where age column == ages_manual
age_equ = banking['age'] == ages_manual
# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]
# Store consistent and inconsistent data
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])


#5)Is this missing at random?
#Missing not at random.


#6)Missing investors
# Print number of missing values in banking
print(banking.isna().sum())
# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Print number of missing values in banking
print(banking.isna().sum())
# Visualize missingness matrix
msno.matrix(banking)
plt.show()
# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]
# The inv_amount is missing only for young customers, since the average age in 
# missing_investors is 22 and the maximum age is 25.
# Print number of missing values in banking
print(banking.isna().sum())
# Visualize missingness matrix
msno.matrix(banking)
plt.show()
# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]
# Sort banking by age and visualize
banking_sorted = banking.sort_values(by='age',ascending=True)
msno.matrix(banking_sorted)
plt.show()


#7)Follow the money
# Drop missing values of cust_id
banking_fullid = banking.dropna(subset = ['cust_id'])
# Compute estimated acct_amount
acct_imp = banking_fullid['inv_amount']*5.0
#print(acct_imp.head())
# Impute missing acct_amount with corresponding acct_imp
banking_imputed = banking_fullid.fillna({'acct_amount': acct_imp})
# Print number of missing values
print(banking_imputed.isna().sum())


'''
___________________________________________________________________________________
##  Part IV Record linkage
___________________________________________________________________________________
'''
 
#1)Minimum edit distance
1 by transposing 'g' with 'n'


#2)The cutoff point
# Import process from fuzzywuzzy
from fuzzywuzzy import process
# Store the unique values of cuisine_type in unique_types
unique_types = restaurants['cuisine_type'].unique()
# Calculate similarity of 'asian' to all values of unique_types
print(process.extract('asian', unique_types, limit = len(unique_types)))
# Calculate similarity of 'american' to all values of unique_types
print(process.extract('american', unique_types, limit = len(unique_types)))
# Calculate similarity of 'italian' to all values of unique_types
print(process.extract('italian', unique_types, limit = len(unique_types)))

# 80


#3)Remapping categories II
categories = ['asian', 'american', 'italian']

# For each correct cuisine_type in categories
for cuisine in categories:
  # Find matches in cuisine_type of restaurants
  matches = process.extract(cuisine, restaurants['cuisine_type'], 
                            limit = restaurants.shape[0])
  
  # For each possible_match with similarity score >= 80
  for possible_match in matches:
    if possible_match[1] >= 80:
      # Find matching cuisine type
      matching_cuisine = restaurants['cuisine_type'] == possible_match[0]
      restaurants.loc[matching_cuisine, 'cuisine_type'] = cuisine
#print(restaurants.head(50))

# Print unique values to confirm mapping
print(restaurants['cuisine_type'].unique())


#4)Pairs of restaurants
# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()
#print(indexer)
#print(type(indexer))
# Block pairing on cuisine_type
#       block method
indexer.block('cuisine_type')
#print(indexer.block('cuisine_type')) # type index, class recordlinkage.api.index
# Generate pairs
pairs = indexer.index(restaurants, restaurants_new)
#print(pairs)


# Compare between columns, score the comparison, then link the DataFrames.


#5)Similar restaurants
# Create a comparison object
comp_cl = recordlinkage.Compare()

# Find exact matches on city, cuisine_types 
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label = 'cuisine_type')
# Find similar matches of rest_name
comp_cl.string('rest_name', 'rest_name', label='name', threshold = 0.80)

# Create a comparison object
comp_cl = recordlinkage.Compare()
# Find exact matches on city, cuisine_types - 
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label='cuisine_type')
# Find similar matches of rest_name
comp_cl.string('rest_name', 'rest_name', label='name', threshold = 0.8) 
# Get potential matches and print
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
print(potential_matches)

# 3 because I need to have matches in all my columns.


#6)Getting the right index
# Both 1 and 3 are correct.


#7)Linking them together!
# Isolate potential matches with row sum >=3
# axis=1 sum() along the row all the columns.
# axis=0 sum() along the column all the rows.
matches = potential_matches[potential_matches.sum(axis=1) >= 3]
# Get values of second column index of matches
matching_indices = matches.index.get_level_values(1)
# Subset restaurants_new based on non-duplicate values
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]
# Append non_dup to restaurants
full_restaurants = restaurants.append(non_dup)
print(full_restaurants)



'''
