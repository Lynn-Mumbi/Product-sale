import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


sales=pd.read_csv("C:\\Users\\USER\\PycharmProjects\\pythonProject\\Datasets\\product_sales.csv")
#print(sales)

#Overview of project and business goals
'''The project we are working on is of product sales from the company Pens and Printers.
The company launched a new product and the goal for our analysis is to find out the best sales strategies
to use. The executive team is to be updated on the sales approaches to use for the new product line.
The sales methods include (Email, Call and a combination of Email+Call)
They need to know the following:
- Number of customers in for each approach.
- The spread of the revenue overall and for each method.
- Was there any difference in revenue over time for each of the methods?
- which method would you recommend we continue to use? 
The choice of the  methods should consider time and resources used.'''

#Data validation
'''
Before I did data validation and cleaning, the dataset contained 15000 rows and 8 columns.
After validating each column against the criteria provided, these are my observations:

week: There were no missing values in this column. The  data type is in integer format. No changes were made here.
sales_method: This column has no missing values and are characters. Before cleaning, the data had five unique sales method rather than the three stated in the criteria.
            This is due to textual variations. "em + call" refer to and has been changed to "Email + Call" as well as 'email' to "Email".
            After cleaning, the column now has 3 unique values: Email, Call and Email + Call.
            
customer_id: This column has no missing data and are characters. The customer_ids are unique for each customer(15000 unique ids) as stated in the criteria. No changes made.

nb_sold: This column has no missing values. The data is numeric as stated in the criteria. No changes were made here

revenue: The data is numeric. This column has 1074 missing values as NaN(not a number).
       I replaced the missing values with the mean due to a couple of factors like the fraction of the missing data to the whole dataset which is less than a tenth, 
 the effect on the distribution does not change much, 
 the range is not affected and the median has a small difference of -2.365 from the original data. 
I have ensured that all the data has been rounded to 2 decimal places.
         
years_as_customer: This column has no missing values. The data is numeric. The minimum years as a customer is zero and maximum is 63.
The reasonable range is between 0 to 39 years. There are two outliers 47 and 63 which go past the current date from when the company was founded in 1984.
I added a column (unreasonable_date_as_True) to show dates as True beyond 39 years.

nb_site_visits: This column has no missing values. The data is numeric. The range is between 12 and 41. No changes were made.

state:There are no missing values in this column. Data remains the  same as described in the criteria. There were no changes done here.



'''

#data validation
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

#how many customers were there for each approach?
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

#summary
'''The most used approach /sales_method are Emails which takes up almost half the number of all methods used. 
 This is then followed by call and lastly email+calls
 We see that emails take more than half the number of customers approached using emails + calls.
 We can conclude that most customers were reached through emails in the sales of the products through out the years.
 Further analysis have to be done to conclude which method would be best to use on the new products '''


#what does the spread of revenue look like overall and for each method?
print(sales['revenue'].describe())
#overall box plot
sns.set(style='whitegrid',palette="colorblind")
plt.figure(figsize=(10, 5))
sns.boxplot(data=sales,y='revenue')
plt.title("Overall Revenue Spread ")

#overall summary box plot
'''The box plot  shows that the overall range of the revenue of all the products is from 53 to 106. 
This shows that a significant portion of the revenue value is concentrated in the lower range. 
 This plot captures the central portion of the distribution having the median revenue as 92 shown by the line inside the box. 
 We could consider the values outside the the whiskers as outliers but further analysis have to be done. 
 There is great variability in the data as we can see from the length of the whiskers.
 '''
#overall histogram
plt.figure(figsize=(10,5))
sns.histplot(data=sales['revenue'],bins=20,color='blue',edgecolor='black',kde=True)
plt.title('The Distribution of Revenue')
plt.xlabel('Revenue')
plt.ylabel('Frequency')
print(sales['revenue'].mode())
plt.show()
#summary of overall histogram
'''I used a histogram which shows the distribution of the revenue and clearly visualizes the frequency of the values at different ranges as shown.
When we take a look at the distribution of the revenue,we see that most revenue acquired by the company lies under 106 which concentrates most values to the left.
This extends the tail to the right which shows a few  extreme high values that suggests right skewness.
The shape of the histogram suggests that the data has a positively skewed distribution.
The revenue past 106 could be considered outliers but further analysis have to be done.'''

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
#summary of boxplot per method
'''To check the spread of revenue per sales method, I created multiple box plots.
We can see that the revenue range in Email+call is more significant than the other sales method from 150 and 190. 
This might be the reason for the outliers seen in the over all previous revenue plots.
 This is then followed by email from 88 to 104 with outliers going up to above 150. 
 Lastly the call method generated the least amount of revenue range.
 Therefore, we can conclude the sales method that most efficient to use in terms of revenue generation, is Email+call then followed by Email.
 This is the most beneficial since email requires little work and call time is around ten minutes per customer which is less than just calling the customer which uses more time. 
 '''
#hist plot per method
print(sales.groupby('sales_method')['revenue'].agg({'max','min'}))
plt.figure(figsize=(10,5))
sns.histplot(data=sales,x='revenue',hue='sales_method',bins=20,multiple='stack')
plt.title('Histogram of revenue per sales method')
plt.xlabel('Revenue')
plt.ylabel('Frequency')
plt.show()
#summary of histogram per sales method
'''We could also look at this  stacked histogram which offers a more detailed view of the distribution of revenue
 against the number of times used.
Email has been the most used method over the six week period but generated lower revenue than the of Emails+Calls method.
Calls method comes second in use. 
As we can see Email+Call generate highest range of revenue and has been the least used method.
These are the extreme values we see in the plot. 
In conclusion we can consider using the Email+Call method more often to increase the revenue generation.'''



#Was there any difference in revenue over time for each of the methods?
print(sales['week'].agg({'max','min'}))
#lineplot
plt.figure(figsize=(10,5))
sns.lineplot(data=sales, x="week",y="revenue",hue="sales_method",hue_order=['Email + Call','Email','Call'],ci=None)
plt.xlabel('weeks since product launch')
plt.ylabel('revenue')
plt.title("The Revenue vs Time for each Sales method")

#summary of line plot of revenue vs time per method
'''The line plot shows the revenue generated by each of the sales method.
The fact that none of the lines touch shows that there is no overlap between the revenue values 
for the each sales methods.Each method has its distinct revenue trajectory.
All the sales methods show a positive trend and slight drops over the third week with the revenue increasing over time.
This shows there is potential overall improvement in  revenue generation through these strategies.
However,there is distinct separation of the lines that suggest that each sales method contributes differently to total revenue.
It is clear from this that Email+ call method leads in terms of high revenue production.  
'''
#barlot
plt.figure(figsize=(10,5))
sns.barplot(data=sales,x="week",y="revenue",hue="sales_method",ci=None, hue_order=['Email + Call','Email','Call'])
plt.title("The Revenue comparison over Time for each Sales method")
plt.xlabel("Week since product launch")
plt.ylabel("Revenue")
plt.show()

#summary of barplot of revenue vs time per sales method
'''Each sales method is represented by a different color. 
The heights show that Email+Calls had the highest revenue production followed by Email then Calls over the six weeks.
In conclusion: there is a positive trend in revenue for the three methods and from the plot Email+Calls 
is the sales method leading in revenue. This method should be put into consideration most in terms if revenue.
'''


'''Some other information to consider are the number of products sold in comparison to the revenue 
generated and and the sale method used. After plotting a bar plot to show the comparison of revenue and products
sold by the sales method, I came to a conclusion that Email+Call method sold most products. 
with calls having the lowest number of products sold and revenue generated.'''
#bar plot sales_method,revenue and nb sold
print(sales['nb_sold'].agg({'min','max'}))
plt.figure(figsize=(10, 5))
sns.barplot(x='nb_sold', y='revenue', data=sales, hue='sales_method',ci=None,hue_order=['Email + Call','Email','Call'])
plt.title('Comparison of Revenue and products Sold by Sales Method')
plt.xlabel('Number of products sold')
plt.ylabel('Revenue')
plt.legend()
plt.show()


#another consideration
'''I decided to calculate the total percentage and sum of the revenue each sales method.
This is to see which method had the most revenue overall.
'''
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
'''Email method generated the highest percentage of revenue at 51 % followed by
 email + call at 31% and call and 17%.
 Conlusion: Email being the most used method has the highest revenue generation.
 '''

#Definition of a metric for the business to monitor
'''BUSINESS METRICS
Given that our objective is to find out which sales method is the best to use for selling the new product line, retain 
customer engangement and revenue generation.
My proposal would be we use the overall revenue generation percentage of the sales methods:
Email+ Call and Email in the products sold over the six week period as our key metric.

Reviewing our data over 80% of revenue is generated through this methods and as we have seen from comparing 
methods to the time that there has been a positive trend which would be an indication of progress towards achieving our 
goal.


RECOMMENDATION
For the new line of stationery I suggest focusing on the following:
1.Optimize  use of combination of Email+ Call since it demonstrated high revenue and significant number of products sold..
   -strategic email campaigns: since email reaches a large number of customers we can reshape content and timing to maximize engagement.
   -We should explore ways to enhance the call method and enhance its contribution to overall sales since its time and resource consuming.
2. We can implement feedback mechanism to find out which channel of communication most customers prefer being addressed through and their experience.
3.Identify trends over time and make data-driven decisions on resource allocation and strategy adjustments.
4. Enhance data collection process for more in depth analysis.
5.Improve quality of data collected particularly in revenues from each sale.
6.Continuous monitoring of key metrics to see the percentage of revenue generated by each sales method..
7.Regular data analysis to stay informed on methods that are most beneficial.
 '''

#years


print(sales.isna().sum())
print(sales.head())


