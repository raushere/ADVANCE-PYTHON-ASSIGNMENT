#!/usr/bin/env python
# coding: utf-8

# # Python Advance Assignment-25

# Q1. What is the distinction between a numpy array and a pandas data frame? Is there a way to convert between the two if there is ?
# Ans: Numpy Ndarray provides a lot of convenient and optimized methods for performing several mathematical operations on vectors.
# 
# Pandas Dataframe is an in-memory 2-dimensional tabular representation of data. In simpler words, it can be seen as a spreadsheet having rows and columns.
# 
# Conversion : Dataframe=pandas.DataFrame(array)

# Q2. Identify some of the plotting techniques that are used to produce a stock-market chart ?
# Ans: Bar chart, Line Chart are used for plotting.

# Q3. Why is it essential to print a legend on a stock market chart ?
# Ans: Legend will help comparison between different stocks, so will be essential on a stock market chart.

# Q4. What is the best way to limit the length of a pandas data frame to less than a year ?
# Ans: : We can use start and end parameters for that. In start we write the date from where we are starting and at the end we write the end date. SO within this span we can restric the duration.Also we can use the parameters like periods for how much times we need the duration and we can also use the frequency parameter.

# Q5. What is the definition of a 180-day moving average ?
# Ans: : The 180-day moving average is represented as a line on charts and represents the average price over the past 180 days. The moving average can give traders a sense regarding whether the trend is up or down, while also identifying potential support or resistance areas.
