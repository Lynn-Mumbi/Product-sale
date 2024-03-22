import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


sales=pd.read_csv("C:\\Users\\USER\\PycharmProjects\\pythonProject\\Datasets\\product_sales.csv")
#print(sales)


#Data validation
#print(sales.columns)
print(sales.isna().sum())
print(sales.dtypes)

#sales_method
print(sales['sales_method'].nunique())
print(sales['sales_method'].value_counts())
sales['sales_method']=sales['sales_method'].str.replace('em + call','Email + Call')
sales['sales_method']=sales['sales_method'].str.replace('email','Email')
print(sales['sales_method'].nunique())
print(sales['sales_method'].value_counts())

#customer_id
print(sales['customer_id'].nunique())

#revenue
print(sales['revenue'].agg({'min','max','mean','median'}))
sales['revenue'].fillna(sales['revenue'].mean(),inplace=True)
print(sales['revenue'].agg({'min','max','mean','median'}))
sales['revenue']=round(sales['revenue'],2)
print(sales['revenue'])

#years_as_customer
print(sales['years_as_customer'].min())
print(sales['years_as_customer'].max())
sales['unreasonable_date_as_True']= sales['years_as_customer'] > 39

#nb_site_visits
print(sales['nb_site_visits'].min())
print(sales['nb_site_visits'].max())

#state
#print(sales['state'].value_counts())






#GUIDE TO ANALYSIS PROJECTS
#print(sales.head(5))
print(sales.columns)

#number of customers were there for each approach?
count_per_sales_method= sales['sales_method'].value_counts()
print(count_per_sales_method)

#countplot
plt.figure(figsize=(10, 5))
sns.countplot(data=sales,x='sales_method')
plt.xlabel("Sales Method")
plt.ylabel("Count per approach")
plt.title("The number of customers in each sales method/approach")

#pie chart
plt.figure(figsize=(10, 5))
plt.pie(count_per_sales_method, labels=count_per_sales_method.index, autopct='%1.1f%%')
plt.title('Percentage of customers in each sales method')
plt.show()

#what does the spread of revenue look like overall and for each method?
print(sales['revenue'].describe())
#overall box plot
sns.set(style='whitegrid',palette="colorblind")
plt.figure(figsize=(10, 5))
sns.boxplot(data=sales,y='revenue')
plt.title("Overall Revenue Spread ")

#overall histogram
plt.figure(figsize=(10,5))
sns.histplot(data=sales['revenue'],bins=20,color='blue',edgecolor='black',kde=True)
plt.title('The Distribution of Revenue')
plt.xlabel('Revenue')
plt.ylabel('Frequency')
print(sales['revenue'].mode())
plt.show()

#box plot per method
'''tf=sales.groupby('sales_method')['revenue'].agg(
    lambda x: x.quantile(0.25))
sf=sales.groupby('sales_method')['revenue'].agg(
    lambda x: x.quantile(0.75))
print(tf)
print(sf)'''
plt.figure(figsize=(10,5))
sns.boxplot(data=sales,x='sales_method',y='revenue',palette='colorblind')
plt.title('Revenue spread per sale method')

#hist plot per method
print(sales.groupby('sales_method')['revenue'].agg({'max','min'}))
plt.figure(figsize=(10,5))
sns.histplot(data=sales,x='revenue',hue='sales_method',bins=20,multiple='stack')
plt.title('Histogram of revenue per sales method')
plt.xlabel('Revenue')
plt.ylabel('Frequency')
plt.show()

#Was there any difference in revenue over time for each of the methods?
print(sales['week'].agg({'max','min'}))
#lineplot
plt.figure(figsize=(10,5))
sns.lineplot(data=sales, x="week",y="revenue",hue="sales_method",hue_order=['Email + Call','Email','Call'],ci=None)
plt.xlabel('weeks since product launch')
plt.ylabel('revenue')
plt.title("The Revenue vs Time for each Sales method")

#barlot
plt.figure(figsize=(10,5))
sns.barplot(data=sales,x="week",y="revenue",hue="sales_method",ci=None, hue_order=['Email + Call','Email','Call'])
plt.title("The Revenue comparison over Time for each Sales method")
plt.xlabel("Week since product launch")
plt.ylabel("Revenue")
plt.show()

#bar plot sales_method,revenue and nb sold
print(sales['nb_sold'].agg({'min','max'}))
plt.figure(figsize=(10, 5))
sns.barplot(x='nb_sold', y='revenue', data=sales, hue='sales_method',ci=None,hue_order=['Email + Call','Email','Call'])
plt.title('Comparison of Revenue and products Sold by Sales Method')
plt.xlabel('Number of products sold')
plt.ylabel('Revenue')
plt.legend()
plt.show()


total_revenue_per_method=sales.groupby('sales_method')['revenue'].sum()
percentage_rev_per_method=(total_revenue_per_method/total_revenue_per_method.sum())*100
print(percentage_rev_per_method)
#plot
plt.figure(figsize=(10,5))
sns.barplot(x=percentage_rev_per_method.index, y=percentage_rev_per_method.values)
plt.title('percentage of Revenue per sales method over the six weeks')
plt.xlabel('sales_method')
plt.ylabel('percentage of revenue')
plt.show()


#years
'''print(sales.isna().sum())
print(sales.head())'''


