import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text,"html.parser")
print(soup.title.text)
table = (soup.find_all('table')[1])
soup.find('table', class_ = "wikitable sortable")
titles = table.find_all('th')
titles_table = [title.text.strip() for title in titles]
df = pd.DataFrame(columns = titles_table)
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data
print(df)
df.to_csv(r'c:\Users\DELL\Desktop\Companies.csv')    
        #Exploratory Data Analysis
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
# Display the first few rows of the dataset
print(df.head())

# Display basic information about the dataset
print(df.info())

# Display summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

df.sort_values(by='Revenue growth',ascending=False).head(10)
#Check for duplicate value
df.duplicated().sum()

#display dinstinct industry categories
print(df['Industry'].unique())

#count dinstinct industry categories
print(df['Industry'].value_counts())

#display dinstinct countries
print(df['Headquarters'].unique())

#count dinstinct countries
print(df['Headquarters'].value_counts())


#DATA CLEANING 
df['Revenue (USD millions)'] = df['Revenue (USD millions)'].replace('[\$,]', '', regex=True).astype(float)
df['Revenue growth'] = df['Revenue growth'].str.rstrip('%').astype(float) / 100.0
print(df)

#DATA VISUALIZATION
#Visualising the revenue using Histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Revenue (USD millions)'], bins=30, kde=True)
plt.title('Revenue Distribution')
plt.xlabel('Revenue in Millions')
plt.ylabel('Frequency')
plt.show()

#Visualising the revenue growth using Histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Revenue growth'], bins=30, kde=True)
plt.title('Revenue Growth Distribution')
plt.xlabel('Revenue Growth')
plt.ylabel('Frequency')
plt.show()

#Visualizing top 10 companies by revenue using barchat
top_companies = df.nlargest(10, 'Revenue (USD millions)')
plt.figure(figsize=(12, 8))
sns.barplot (x='Revenue (USD millions)', y='Name', data=top_companies)
plt.title('Top 10 Companies by Revenue')
plt.xlabel('Revenue in Millions')
plt.ylabel('Company')
plt.show()

#Visualizing top 10 companies by revenue growth using barchat
top_companies = df.nlargest(10, 'Revenue growth')
plt.figure(figsize=(12, 8))
sns.barplot (x='Revenue growth', y='Name', data=top_companies)
plt.title('Top 10 Companies by Revenue growth')
plt.xlabel('Revenue growth')
plt.ylabel('Company')
plt.show()


#Visualizing industry by revenue using boxplot
plt.figure(figsize=(12, 8))
sns.boxplot(x='Industry', y='Revenue (USD millions)', data=df)
plt.title('Revenue by Industry')
plt.xlabel('Industry')
plt.ylabel('Revenue in Millions')
plt.xticks(rotation=90)
plt.show()

# Select relevant columns for the pair plot
pairplot_cols = ['Revenue (USD millions)', 'Revenue growth']
sns.pairplot(df[pairplot_cols])
plt.suptitle('Pair Plot of Key Financial Metrics', y=1.02)
plt.show()

#Visualizing revenue by industry
plt.figure(figsize=(12, 8))
industry_revenue = df.groupby('Industry')['Revenue (USD millions)'].sum().sort_values()
sns.barplot(x=industry_revenue.values, y=industry_revenue.index)
plt.title('Total Revenue by Industry')
plt.xlabel('Total Revenue in Millions')
plt.ylabel('Industry')
plt.show()


plt.figure(figsize=(12, 8))
country_revenue = df.groupby('Headquarters')['Revenue (USD millions)'].sum().sort_values()
sns.barplot(x=country_revenue.values, y=country_revenue.index)
plt.title('Total Revenue by Country')
plt.xlabel('Total Revenue in Millions')
plt.ylabel('Country')
plt.show()
















