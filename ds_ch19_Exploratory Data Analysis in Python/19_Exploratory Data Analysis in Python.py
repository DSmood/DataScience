
# 19_Exploratory Data Analysis in Python

___________________________________________________________________________________
##  Part I Read, clean, and validate
___________________________________________________________________________________
'''
 
#1)Exploring the NSFG data
 Display the number of rows and columns
nsfg.shape

# Display the names of the columns
nsfg.columns

# Select column birthwgt_oz1: ounces
ounces = nsfg['birthwgt_oz1']

# Print the first 5 elements of ounces
print(ounces.head())


#2)Clean a variable
# Replace the value 8 with NaN
nsfg['nbrnaliv'].replace(8, np.nan, inplace=True)

# Print the values and their frequencies
print(nsfg['nbrnaliv'].value_counts())


#3)Compute a variable
# Select the columns and divide by 100
agecon = nsfg['agecon'] / 100
agepreg = nsfg['agepreg'] / 100

# Compute the difference
preg_length = agepreg - agecon

# Compute summary statistics
print(preg_length.describe())


#4)Make a histogram
# Plot the histogram
plt.hist(agecon.dropna(), bins=20)
# Label the axes
plt.xlabel('Age at conception')
plt.ylabel('Number of pregnancies')
# Show the figure
plt.show()

# Plot the histogram
plt.hist(agecon, bins=20, histtype='step')
# Label the axes
plt.xlabel('Age at conception')
plt.ylabel('Number of pregnancies')
# Show the figure
plt.show()


#5)Compute birth weight
# Create a Boolean Series for full-term babies
full_term = nsfg['prglngth'] >= 37

# Select the weights of full-term babies
full_term_weight = birth_weight[full_term]

# Compute the mean weight of full-term babies
print(full_term_weight.mean())


#6)Filter
# Filter full-term babies
full_term = nsfg['prglngth'] >= 37

# Filter single births
single = nsfg['nbrnaliv'] == 1

# Compute birth weight for single full-term babies
single_full_term_weight = birth_weight[full_term & single]
print('Single full-term mean:', single_full_term_weight.mean())

# Compute birth weight for multiple full-term babies
mult_full_term_weight = birth_weight[~single & full_term]
print('Multiple full-term mean:', mult_full_term_weight.mean())

'''

___________________________________________________________________________________
##  Part II Distributions
___________________________________________________________________________________
'''
 
#1)Make a PMF
# Compute the PMF for year
pmf_year = Pmf(gss['year'], normalize=False)
# Print the result
print(pmf_year)

#2867


#2)Plot a PMF
# Select the age column
age = gss['age']

# Make a PMF of age
pmf_age = Pmf(gss['age'], normalize=True)

# Select the age column
age = gss['age']
# Make a PMF of age
pmf_age = Pmf(age)
# Plot the PMF
pmf_age.bar()
# Label the axes
plt.xlabel('Age')
plt.ylabel('PMF')
plt.show()


#3)Make a CDF
# Select the age column
age = gss['age']

# Compute the CDF of age
cdf_age = Cdf(gss['age'])

# Select the age column
age = gss['age']
# Compute the CDF of age
cdf_age = Cdf(age)
# Calculate the CDF of 30
#p=cdf_age(30)
print(cdf_age(30))


#4)Compute IQR
# Calculate the 75th percentile 
cdf_income.head()
cdf_income.describe()
type(cdf_income)
p=0.75
percentile_75th = cdf_income.inverse(p)


# Calculate the 75th percentile 
percentile_75th = cdf_income.inverse(0.75)
# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25) 


# Calculate the 75th percentile 
percentile_75th = cdf_income.inverse(0.75)
# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)
# Calculate the interquartile range
iqr = percentile_75th - percentile_25th
# Print the interquartile range
print(iqr)


#29679


#5)Plot a CDF
# Select realinc
income = gss['realinc']

# Make the CDF
cdf_income = Cdf(income)

# Plot it
cdf_income.plot()

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.show()


#6)Distribution of education
Cdf(gss['educ']) = 53 %


#7)Extract education levels
# Select educ
educ = gss['educ']
# Bachelor's degree
bach = (educ >= 16)
# Associate degree
assc = ((educ >= 14) & (educ < 16))
# High school (12 or fewer years of education)
high = (educ <= 12)
print(high.mean())


#8)Plot income CDFs
income = gss['realinc']

# Plot the CDFs
Cdf(income[high]).plot(label='High school')
Cdf(income[assc]).plot(label='Associate')
Cdf(income[bach]).plot(label='Bachelor')

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.legend()
plt.show()


#9)Distribution of income
# Extract realinc and compute its log
income = gss['realinc']
log_income = np.log10(income)

# Compute mean and standard deviation
mean = log_income.mean()
std = log_income.std()
print(mean, std)

# Make a norm object
from scipy.stats import norm
dist = norm(mean, std)


#10)Comparing CDFs
# Evaluate the model CDF
xs = np.linspace(2, 5.5)
ys = dist.cdf(xs)

# Plot the model CDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Create and plot the Cdf of log_income
Cdf(log_income).plot()
    
# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('CDF')
plt.show()


#11)Comparing PDFs
# Evaluate the normal PDF
xs = np.linspace(2, 5.5)
ys = dist.pdf(xs)

# Plot the model PDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Plot the data KDE
sns.kdeplot(log_income)

# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('PDF')
plt.show()

'''
___________________________________________________________________________________
##  Part III Relationships
___________________________________________________________________________________
'''
 
#1)PMF of age
# Extract age
age = brfss['AGE']

# Plot the PMF
Pmf(age).bar()

# Label the axes
plt.xlabel('Age in years')
plt.ylabel('PMF')
plt.show()


#2)Scatter plot
# Select the first 1000 respondents
brfss = brfss[:1000]

# Extract age and weight
age = brfss['AGE']
weight = brfss['WTKG3']

# Make a scatter plot
plt.plot(age, weight, 'o', alpha=0.1)

plt.xlabel('Age in years')
plt.ylabel('Weight in kg')

plt.show()


#3)Jittering
# Select the first 1000 respondents
brfss = brfss[:1000]

# Add jittering to age
#age = brfss['AGE'] + np.random.normal(0, 2.5)
age = brfss['AGE'] + np.random.normal(0, 2.5, size=len(brfss))
# Extract weight
weight = brfss['WTKG3']

# Make a scatter plot
plt.plot(age, weight, 'o', markersize=5, alpha=0.2)

plt.xlabel('Age in years')
plt.ylabel('Weight in kg')
plt.show()


#4)Height and weight
# Drop rows with missing data
data = brfss.dropna(subset=['_HTMG10', 'WTKG3'])

# Make a box plot
sns.boxplot(y='WTKG3', x='_HTMG10', data=data, whis=10)

# Plot the y-axis on a log scale
plt.yscale('log')

# Remove unneeded lines and label axes
sns.despine(left=True, bottom=True)
plt.xlabel('Height in cm')
plt.ylabel('Weight in kg')
plt.show()


#5)Distribution of income
# Extract income
income = brfss['INCOME2']
# Plot the PMF
Pmf(income).bar()
# Label the axes
plt.xlabel('Income level')
plt.ylabel('PMF')
plt.show()


#6)Income and height
# Drop rows with missing data
data = brfss.dropna(subset=['INCOME2', 'HTM4'])

# Make a violin plot
sns.violinplot(x='INCOME2', y='HTM4', data=data, inner=None)

# Remove unneeded lines and label axes
sns.despine(left=True, bottom=True)
plt.xlabel('Income level')
plt.ylabel('Height in cm')
plt.show()


#7)Computing correlations
# Select columns
columns = ['AGE', 'INCOME2', '_VEGESU1']
subset = brfss[columns]

# Compute the correlation matrix
print(subset.corr())


#8)Income and vegetables
from scipy.stats import linregress

# Extract the variables
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']

# Compute the linear regression
res = linregress(xs,ys)
print(res)


#9)Fit a line
# Plot the scatter plot
plt.clf()
x_jitter = xs + np.random.normal(0, 0.15, len(xs))
plt.plot(x_jitter, ys, 'o', alpha=0.2)

# Plot the line of best fit
fx = np.array([xs.min(), xs.max()])
fy = res.intercept + res.slope * fx
plt.plot(fx, fy, '-', alpha=0.7)

plt.xlabel('Income code')
plt.ylabel('Vegetable servings per day')
plt.ylim([0, 6])
plt.show()

'''
___________________________________________________________________________________
##  Part IV Multivariate Thinking
___________________________________________________________________________________
'''
 
#1)Using StatsModels
from scipy.stats import linregress
import statsmodels.formula.api as smf

# Run regression with linregress
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']
res = linregress(xs,ys)
print(res)

# Run regression with StatsModels
results = smf.ols('_VEGESU1 ~ INCOME2', data = brfss).fit()
print(results.params)


#2)Plot income and education
# Group by educ
grouped = gss.groupby(by='educ')

# Compute mean income in each group
mean_income_by_educ = grouped['realinc'].mean()

# Plot mean income as a scatter plot
plt.plot(mean_income_by_educ, 'o', alpha=0.5)

# Label the axes
plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.show()


#3)Non-linear model of education
import statsmodels.formula.api as smf

# Add a new column with educ squared
gss['educ2'] = gss['educ']**2

# Run a regression model with educ, educ2, age, and age2
model = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss)
results = model.fit() 

# Print the estimated parameters
print(results.params)


#4)Making predictions
# Run a regression model with educ, educ2, age, and age2
results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

# Make the DataFrame
df = pd.DataFrame()
df['educ'] = np.linspace(0, 20)
df['age'] = 30
df['educ2'] = df['educ']**2
df['age2'] = df['age']**2

# Generate and plot the predictions
pred = results.predict(df)
print(pred.head())


#5)Visualizing predictions
# Plot mean income in each age group
plt.clf()
grouped = gss.groupby('educ')
mean_income_by_educ = grouped['realinc'].mean()
plt.plot(mean_income_by_educ, 'o', alpha=0.5)

# Plot the predictions
pred = results.predict(df)
plt.plot(df['educ'], pred, label='Age 30')

# Label axes
plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.legend()
plt.show()


#6)Predicting a binary variable
# Recode grass
gss['grass'].replace(2, 0, inplace=True)
# Run logistic regression
results = smf.logit('grass ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()
results.params


# Recode grass
gss['grass'].replace(2, 0, inplace=True)
# Run logistic regression
results = smf.logit('grass ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()
results.params
# Make a DataFrame with a range of ages
df = pd.DataFrame()
df['age'] = np.linspace(18, 89)
df['age2'] = df['age']**2
# Set the education level to 12
df['educ'] = 12
df['educ2'] = 12**2


# Recode grass
gss['grass'].replace(2, 0, inplace=True)
# Run logistic regression
results = smf.logit('grass ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()
results.params
# Make a DataFrame with a range of ages
df = pd.DataFrame()
df['age'] = np.linspace(18, 89)
df['age2'] = df['age']**2
# Set the education level to 12
df['educ'] = 12
df['educ2'] = df['educ']**2
# Generate predictions for men and women
df['sex'] = 1
pred1 = results.predict(df)
df['sex'] = 2
pred2 = results.predict(df)


# Recode grass
gss['grass'].replace(2, 0, inplace=True)
# Run logistic regression
results = smf.logit('grass ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()
results.params
# Make a DataFrame with a range of ages
df = pd.DataFrame()
df['age'] = np.linspace(18, 89)
df['age2'] = df['age']**2
# Set the education level to 12
df['educ'] = 12
df['educ2'] = df['educ']**2
# Generate predictions for men and women
df['sex'] = 1
pred1 = results.predict(df)
df['sex'] = 2
pred2 = results.predict(df)
# visualizing results
plt.clf()
grouped = gss.groupby('age')
favor_by_age = grouped['grass'].mean()
plt.plot(favor_by_age, 'o', alpha=0.5)
plt.plot(df['age'], pred1, label='Male')
plt.plot(df['age'], pred2, label='Female')
plt.xlabel('Age')
plt.ylabel('Probability of favoring legalization')
plt.legend()
plt.show()


'''
