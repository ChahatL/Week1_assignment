#!/usr/bin/env python
# coding: utf-8

# In[26]:


'''Note:

* Before writing any code remember that this assigment is for helping you understand the basics of file
handling in csv file.

* This project is designed to have a work flow such that everyone is in same page for this purpose the variables are
given a strict name which should not be changed or modified according to your convinience

* Few of new functions like .head() .xticks().... and concepts may have been introduced in the assingment, so we encourage you
all to go through them without skipping.

*  functions which are to be used in the Your code sections are globally available so try to look for those where you have been prompted
'''

'''Its the data of a meal delivery company which operates in multiple cities.
They have various fulfillment centers in these cities for dispatching meal orders to their customers.
train.csv: Historical data of demand for a product-center combination
fulfilment_center_info.csv: Information for fulfillment center like center area, city information etc.
meal_info.csv: Product(Meal) features such as category, sub-category, current price and discount'''


'''START CODE'''

#Import necessary libraries: Numpy,pandas,matplotlib

import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

#read meal_info.csv file from provided dataset into a df_meal named variable
#Note: Proper file directory should be provided
csv_path='meal_info.csv'
df_meal=pd.read_csv(csv_path)
df_meal.head()

'''This is for displaying first five data points'''

#read fulfilment_center_info.csv file from provided dataset
#Note: Proper file directory should be provided
csv_path='fulfilment_center_info.csv'
df_center=pd.read_csv(csv_path)
df_center.head()
'''This is for displaying first five data points'''

#read train.csv file from provided dataset
#Note: Proper file directory should be provided
csv_path='train.csv'
df_food=pd.read_csv(csv_path)
df_food.head()
'''Since the provided information is in different files, your work here is to merge them.Look for the functions
in pandas library to do so'''
df=pd.merge(df_center,df_food,on='center_id',how='outer')
df=pd.merge(df,df_meal,on='meal_id')
df


'''Here we have used pd.pivot_table() kindly go through the function and mention in comment what it does'''

table = pd.pivot_table(data=df,index='category',values='num_orders',aggfunc=np.sum)
table
# this function creates an excel style pivot table agrregating dataframes with different operations.



'''Graph tweaking
************************
Plot a bar graph with title 'Most popular food' for category(x-axis) vs number-of-orders(y-axis)

give x label 'Food items'
give y label 'Quantity sold'


'''

'''************Yourcode*********************'''
table.plot.box(()
# Signature: table.plot.box(by=None, **kwargs)
plt.xticks(rotation=70) plt.xticks()
#                Signature: plt.xticks(ticks=None, labels=None, **kwargs)
# Get or set the current tick locations and labels of the x-axis.
# Call signatures::
# locs, labels = xticks()            # Get locations and labels
#     xticks(ticks, [labels], **kwargs)  # Set locations and labels
plt.xlabel('category')
plt.ylabel('Quantity Sold')
plt.title('Most Popular Food')
plt.savefig('Most_Popular_Food.png')
plt.show()

# bar graph


# xticks
# plt.xticks(rotation=70) '''Write on comment what you feel this function does'''

# x-axis labels

#
# y-axis labels


# plot title


# save plot


# display


'''************************************************'''


'''Comparison of weekly and monthly sales
 Create a new column
* named 'revenue' where each element is product of checkout_price and num_orders
** named 'month' by using ['week'] column (week column value divided by 4 gives month value)'''

df['Revenue']=df['checkout_price']*df['num_orders']
df['month']=(df['week'])//4
df

'''Here we have created two list month and month_order ,
store month number in month list and revenue of each month in month_order'''
#list to store month-wise revenue
# month=[]
# month_order=[]

'''***********************************Your code***********************'''


'''*********************************************************************'''
'''Here we have created two list week and week_order ,you need to store in them mapping the monthly orders'''
#list to store week-wise revenue
# week=[]
# week_order=[]

'''***********************************Your code***********************'''
month=table1.index.tolist() #converting index into  list by this index.tolist() function
month_order=table1.values.tolist()
# table.index.tolist()
# Return a list of the values.
# These are each a scalar type, which is a Python scalar
# (for str, int, float) or a pandas scalar
# (for Timestamp/Timedelta/Interval/Period)

'''*********************************************************************'''
''' Plot two subplots in the same space : one for weekly revenue and other for monthly revenue.
For weekly : Title(Weekly income),x_label(week),y_label(revenue); similarly for monthly revenue.
'''

'''************Yourcode*********************'''
# pd.pivot_table(data,values=None,index=None,columns=None,aggfunc='mean',fill_value=None,
# margins=False,dropna=True, margins_name='All',observed=False)
table1=pd.pivot_table(
    data=df,
    values=['Revenue'],
    index=['month'],
    aggfunc=np.sum
)
month=table1.index.tolist()
month_order=table1.values.tolist()
table2=pd.pivot_table(
    data=df,
    values=['Revenue'],
    index=['week'],
     aggfunc=np.sum,
   )
week=table2.index.tolist()
week_order=table2.values.tolist()
fig, ax=plt.subplots(nrows=1,ncols=2,figsize=(20,6))
fig.savefig(income.png)
# savefig(fname, dpi=None, facecolor='w', edgecolor='w',
#           orientation='portrait', papertype=None, format=None,
#           transparent=False, bbox_inches=None, pad_inches=0.1,
#           frameon=None, metadata=None)
ax[0].plot(month,month_order)
ax[0].set_xlabel('month')
ax[0].set_ylabel('Revenue')
ax[0].set_title('Monthly Income')
ax[1].plot(week,week_order)
ax[1].set_xlabel('week')
ax[1].set_ylabel('Revenue')
ax[1].set_title('Weekly Income')
plt.show()
#    subplot(nrows, ncols, index, **kwargs)
# plt.subplots() function returns a tuple containing a figure and axes objects
# when you use fig,ax=plt.sunbplots() you unpack this tuple into variables fig and ax


''' Display the plot'''
