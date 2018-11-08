# -*- coding: utf-8 -*-
"""
John Turbefield, November 2018
Data Processing with Python Assignment (MSCDSA04)
"""
#Import Libraries
import pandas as pd

#Set Library Options
pd.set_option('display.max_rows', 50000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)  

#Set Functions
#	g. Show first 3 rows of data
def ShowFirstLines():
    numfirstlines = int(input("How many lines would you like to show?:"))
    print(data.head(numfirstlines))
        
#	h. Show last 4 rows of data    
def ShowLastLines():
    numlastlines = int(input("How many lines would you like to show?:"))
    print(data.tail(numlastlines))

#   Show Whole DataFrame
def ShowWholeDataFrame():
    print(data)
    
#a. Sort data
#		i. Date
#		ii. Totals - high
#		iii. Totals - low
#   Sort DataFrame by Column, Ascending
def SortByAscending():
    print("Which column would you like to sort by (case sensitive)?")
    columntosort = input("Column: ")
    data.sort_values(columntosort, inplace = True)
    print("Data Sorted.")

#   Sort DataFrame by Column, Descending
def SortByDescending():
    print("Which column would you like to sort by (case sensitive)?")
    columntosort = input("Column: ")
    data.sort_values(columntosort, ascending = False, inplace = True)
    print("Data Sorted.")
    
#	b. Sum data
def SumColumn():
    print("Which column would you like the sum of?")
    columntosum = input("Column: ")
    columnsum = data[columntosum].sum()
    print(columnsum) 
    
#		i. Count of entries of each type
def GroupRows():
    print("For which column would you to see a list of entries by count?") 
    columntogroup = input("Column: ")
    data2 = data.groupby(columntogroup)[columntogroup].count()
    data2.sort_values(ascending = False, inplace = True)
    print(data2)

#		ii. Sum of entries of each type?   
def SumGroupedRows():
    print("Which column would you to group up (i.e. Sold Item, Manufacturer, Year)?") 
    columntogroupby = input("Column: ")
    print("Which column would you like the totals for (i.e. sales, inventory)?")
    columntogetsum = input("Column: ")
    data3 = data.groupby(columntogroupby)[columntogroupby,columntogetsum].sum()
    data3.sort_values(columntogetsum, ascending = False, inplace = True)
    print(data3)
    
#	c. Show mean of each type of data    
def ColumnMean():
    print("Which column would you like the mean of?")
    columntomean = input("Column: ")
    columnmean= data[columntomean].mean()
    print(columnmean) 
    
#	d. Show standard deviation    
def ColumnStandardDeviation():
    print("Which column would you like the standard deviation of?")
    columnstdev = input("Column: ")
    columnstd = data.loc[:,columnstdev].std()
    print(columnstd) 
    
#	e. Describe covariance    
def Covariance():
    print(data.cov())
    
#	f. Describe correlation
def Correlation():
    print(data.corr())
    
#   Add Column with % of total of another column
def PercentCol():
    print("Which Column would you like the % for?")
    percol = input("Column: ")
    data[percol+'Percent']= round(((data[percol]/data[percol].sum())*100),2)
    print("Column Added")
    
#   Filter by the entry in a column, i.e. filter '2000' in column 'year'
def FilterColumn():
    print("Which Column would you like to filter by?")
    filcol = input("Column: ")
    
    print("In which way would you like to filter it? Defaults to equal to if error.")
    print("1. Equal to.")
    print("2. Not equal to.")
    print("3. More than or equal to.")
    print("4. Less than or equal to.")
    print("5. More than.")
    print("6. Less than.")
    filtype = int(input("Method: "))
    
    print("Which value would you like to filter by?")
    filval = input("Value:")
    
    filtering = True
    while filtering:
        if filtype == 1:
            istrue = data[filcol] == filval
            FilterColumn.datatemp = data[istrue]
            filtering = False
            print("Filtered by equal to.")
        elif filtype == 2:
            istrue = data[filcol] != filval
            FilterColumn.datatemp = data[istrue]
            filtering = False
            print("Filtered by not equal to.")
        elif filtype == 3:
            istrue = data[filcol] >= int(filval)
            FilterColumn.datatemp = data[istrue]
            filtering = False
            print("Filtered by more than or equal to.")
        elif filtype == 4:
            istrue = data[filcol] <= int(filval)
            FilterColumn.datatemp = data[istrue]
            filtering = False
            print("Filtered by less than or equal to.")
        elif filtype == 5:
            istrue = data[filcol] > int(filval)
            FilterColumn.datatemp = data[istrue]
            filtering = False
            print("Filtered by more than.")
        elif filtype == 6:
            istrue = data[filcol] < int(filval)
            FilterColumn.datatemp = data[istrue]
            filtering = False
            print("Filtered by less than.")
        else:
            istrue = data[filcol] == filval
            FilterColumn.datatemp = data[istrue]
            filtering = False
            print("Error. Filtered as equal to.")
            
# Deal with missing data in columns. Shows mean, median and mode in case user doesn't wish for 0.
def MissingData():
    print("Which column has missing entries that you would like to replace?")
    misscol = input("Column: ")
    columnmean = data[misscol].mean()
    columnmode = data[misscol].mode()
    columnmedian = data[misscol].median()
    print("Data for this column, excluding missing points:")
    print("Mean:",columnmean)
    print("Median:",columnmedian)
    print("Mode:",columnmode)
    
    print("What would you like to replace the missing entries with?")    
    replacewith = input("Replacement:")
    data[misscol].fillna(replacewith, inplace = True)

# Export dataframe to CSV (#5. Option to save/export changed data) 
def Export():
    exportfile = input("What would you like to name the file?: ")
    data.to_csv(exportfile + '.csv')
    print("File written.")
    
    
#3. List options of what to do with data
def options():
    print("What would you like to do?")
    print("1. Show the top x lines.")
    print("2. Show the last x lines.")
    print("3. Show the full table.")
    print("4. Sort table - Ascending.")
    print("5. Sort table - Descending.")
    print("6. Output total sum of a column.")
    print("7. Output list of entries within a column by count of entries.")
    print("8. Output list of column entries by sum of another column")
    print("9. Show the mean value of a column of integers")
    print("10. Show the standard deviation of the values in a column.")
    print("11. Show the covariance between the columns of integers.")
    print("12. Show the correlation between the columns of integers.")
    print("13. Add column with % of the total of a specified column.")
    print("14. Filter by a value in a column.")
    print("15. Resolve missing values in columns.")
    print("97. Reload the CSV file.")
    print("98. Export the table to a new CSV file.")
    print("99. Exit the script.")

#Ask for file Name
print("Please ensure the source data file is in the same directory as this script.")
print("Enter the name of the CSV file (without .csv extension) you would like to open:")
datafilename = input("File: ")
datafilename = datafilename+(".csv")
print("The file name is " + datafilename + ". Now opening.")
print()


#Load the file
data = pd.read_csv(datafilename)
print("File opened.")

options()

scriptrunning = True
while scriptrunning:
    UserChoice = int(input("Selection: "))
    if UserChoice == 1:
        ShowFirstLines()
        options()
    elif UserChoice == 2:
        ShowLastLines()
        options()
    elif UserChoice == 3:
        ShowWholeDataFrame()
        options()
    elif UserChoice == 4:
        SortByAscending()
        options()
    elif UserChoice == 5:
        SortByDescending()
        options()
    elif UserChoice == 6:
        SumColumn()
        options()
    elif UserChoice == 7:
        GroupRows()
        options()
    elif UserChoice == 8:
        SumGroupedRows()
        options()
    elif UserChoice == 9:
        ColumnMean()
        options()
    elif UserChoice == 10:
        ColumnStandardDeviation()
        options()
    elif UserChoice == 11:
        Covariance()
        options()
    elif UserChoice == 12:
        Correlation()
        options()
    elif UserChoice == 13:
        PercentCol()
        options()
    elif UserChoice == 14:
        FilterColumn()
        data = FilterColumn.datatemp
        options()
    elif UserChoice == 15:
        MissingData()
        options()
    elif UserChoice == 97:
        data = pd.read_csv(datafilename)
        print("Data file reloaded.")
    elif UserChoice == 98:
        Export()
        options()
#6. Exit
    elif UserChoice == 99:
        print("Script closed.")
        scriptrunning = False
    else: 
        print("Invalid selection.")