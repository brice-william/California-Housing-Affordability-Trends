# Cleaning data of PUMS 2022 and using pandas to analyze
# Home ownership rate of each state

import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-GUI rendering

import pandas as pd
import matplotlib.pyplot as plt   # Ensure pyplot is imported correctly
import matplotlib.ticker as mticker  # Import ticker for formatting
import os

# Load the data
df = pd.read_csv('hca_data_2022.csv')

#only keep the columns we need
#RNTP: Monthly rent payment
#FINCP: Total family income
#NP: Number of people in the household
#FS 
#Yearly food stamp/Supplemental Nutrition Assistance Program (SNAP) 
#recipiency 
#b .N/A (vacant) 
#1 .Yes 
#2 .No

#We only want these columns to analyze for now
df = df[['RNTP', 'FINCP', 'NP', 'FS']]

#Drop rows with missing values
df = df.dropna()

#drop rows with 0 or less NP
df = df[df['NP'] > 0]

#drop rows with 0 or less RNTP
df = df[df['RNTP'] > 0]

#drop rows with 0 or less FINCP
df = df[df['FINCP'] > 0]

#create a separate data frame for the food stamp/SNAP recipiency
df_fs = df[df['FS'] == 1]
#drop rows with FINCP greater than 200,000
df_fs = df_fs[df_fs['FINCP'] <= 100000]

#create a separate data frame for the food stamp/SNAP non-recipiency
df_fs_non = df[df['FS'] == 2]


print(df_fs.describe().round(0))

print(df_fs_non.describe().round(0))

#create a scatter plot of the food stamp/SNAP recipiency family income vs. rent payment
plt.scatter(df_fs['FINCP'], df_fs['RNTP'], color='blue', label='Food Stamp/SNAP Recipiency', s=2)

#add a legend to the scatter plot
plt.legend()

#add a title to the scatter plot
plt.title('Food Stamp/SNAP Recipiency family income vs. Rent Payment')

#add a label to the x-axis
plt.xlabel('Total Family Income')

# Format the x-axis to display the incomes in intervals of 5 thousand dollars label as 5k, 10k, 15k, 20k and so on do not use dollar signs 
plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(10000))
plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: f'{x/1000:.0f}k'))


#add a label to the y-axis
plt.ylabel('Monthly Rent Payment')

# Format the y-axis to display numbers with commas and dollar signs
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: f'${x:,.0f}'))

#save the scatter plot to a file
plt.savefig('scatter_plot.png', bbox_inches='tight' )












