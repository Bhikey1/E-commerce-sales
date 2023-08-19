import numpy as np
import panda as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('sales1.csv')

""" TASK:
1. Analyzing customer demographics by countries and states to better future marketing campaigns.
2. Tracking changes in customer's spending habits over time for different product categories.
3. Identifying which product categories have the highest average revenue per sale to help prioritize
resources for those products or services. """

# Checking for missing values.
df.isnull().sum()
Date                0
Day                 0
Month               0
Year                0
Customer_Age        0
Age_Group           0
Customer_Gender     0
Country             0
State               0
Product_Category    0
Sub_Category        0
Product             0
Order_Quantity      0
Unit_Cost           0
Unit_Price          0
Profit              0
Cost                0
Revenue             0
dtype: int64

# Checking for duplicates values.
>>> df.duplicated().sum()
0
>>> df.describe()
                 Day           Year  ...           Cost        Revenue
count  112036.000000  112036.000000  ...  112036.000000  112036.000000
mean       15.665607    2014.400925  ...     471.103333     757.138527
std         8.781485       1.273327  ...     886.971635    1312.061623
min         1.000000    2011.000000  ...       1.000000       2.000000
25%         8.000000    2013.000000  ...      28.000000      64.000000
50%        16.000000    2014.000000  ...     112.000000     226.000000
75%        23.000000    2016.000000  ...     442.000000     806.000000
max        31.000000    2016.000000  ...   42978.000000   58074.000000

[8 rows x 9 columns]

df.head()
         Date  Day     Month  Year  ...  Unit_Price Profit  Cost Revenue
0  2013-11-26   26  November  2013  ...         120    590   360     950
1  2015-11-26   26  November  2015  ...         120    590   360     950
2  2014-03-23   23     March  2014  ...         120   1366  1035    2401
3  2016-03-23   23     March  2016  ...         120   1188   900    2088
4  2014-05-15   15       May  2014  ...         120    238   180     418

[5 rows x 18 columns]

# Removing all 2016 values
df = df[df['Date'] != '2016']

# Customer demographics by countries and states to better future marketing campaigns.
cust_demographics = df.groupby(['Country', 'State'])['Revenue'].sum()
cust_demographics.head()
Country    State          
Australia  New South Wales    9125980
           Queensland         5055843
           South Australia    1396139
           Tasmania            580139
           Victoria           5038294
Name: Revenue, dtype: int64

# Exporting df for visualization.
cust_demographics.to_csv('cust demographics.txt')

#Tracking changes in customer spending habits over time for different product categories.
cust_spending_habit = df.groupby(['Date', 'Product_Category'])['Revenue'].sum()
cust_spending_habit.head()
Date        Product_Category
2011-01-01  Bikes               12821
2011-01-02  Bikes               11868
2011-01-03  Bikes               31175
2011-01-04  Bikes               18909
2011-01-05  Bikes                4675
Name: Revenue, dtype: int64

# Exporting df for visualization.
cust_spending_habit.to_csv('cust spending habit.txt')

# Identifying which product categories have the highest revenue per sale.
df['ARPU'] = df['Revenue'].sum() / df['Order_Quantity'].sum()
product_ARPU = df.groupby(['Date', 'Product_Category'])['ARPU'].sum()
product_ARPU.head()
Date        Product_Category
2011-01-01  Bikes               318.011749
2011-01-02  Bikes               254.409399
2011-01-03  Bikes               508.818799
2011-01-04  Bikes               318.011749
2011-01-05  Bikes               190.807050
Name: ARPU, dtype: float64

# Exporting df for visualization.
product_ARPU.to_csv('product ARPU.txt')

# CONCLUSION

""" DEMOGRAPHICS FOR FUTURE MARKETING CAMPAIGN: The countries and states to lookout for
in the future are the United States: California, Washington, Oregon, Austrailia: New
South Wales, Queensland, Victoria, The United Kingdom, Canada: British Columbia. They
are countries and states that generating large amount of revenue. 

AVERAGE REVENUE PER SALE: Accessories have the highest average revenue per sale, followed
by bikes and clothing respectively. """
