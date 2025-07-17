# Overview
This Python project analyzes product sales data collected over a 6-week campaign, focusing on the effectiveness of different sales approaches (Email, Call, and Email + Call). It covers customer behavior, revenue distribution, and performance trends over time.

Key Insights Generated
Customer Distribution: Number and percentage of customers by each sales method (count plot + pie chart).

Revenue Analysis:

Overall revenue spread (box plot, histogram).

Revenue spread by sales method (comparative box plots + stacked histograms).

Revenue Trends Over Time: Line and bar plots showing revenue growth per week by method.

Sales vs Revenue: Relationship between number of items sold and revenue, broken down by method.

Revenue Contribution: Share of total revenue per method (bar plot of percentages).

Data Validation & Cleaning:

Handled missing values in revenue.

Standardized inconsistent sales method naming.

Flagged unreasonable customer tenure (years_as_customer > 39).

Dataset Columns Used
sales_method: Channel used for reaching customer.

revenue: Sale value (in currency).

nb_sold: Number of products sold.

week: Weeks since product launch.

years_as_customer: Customer tenure.

nb_site_visits: Customer engagement level.

customer_id, state: Used for uniqueness and location reference.

Dependencies
bash
Copy
Edit
pandas
numpy
matplotlib
seaborn
Install via:

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn

Output
All insights are visualized using Seaborn and Matplotlib, with plots covering:

Revenue distribution and trends

Customer method adoption

Method effectiveness comparisons

