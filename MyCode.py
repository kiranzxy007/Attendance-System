#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Assumption : In "Sample Output.csv" provided by DarwinBOX team contain the column 'Break Duration' 
# Column 'Break Duration'  is empty and I also keeping it empty in my ouput
 

# Importing pandas library
import pandas as pd  

# Import data 'data1.csv' file given by Darwin Box team into a dataframe
# Extract the 'data1.csv' into dataframe which should be current in directory 
# convert timestamp values to Timestamp python object while extracting
data=pd.read_csv("data1.csv",parse_dates=["timestamp"],)

# Drop null values 
data.dropna(how='any',inplace=True)

# Rename the column name 'employee_no' to 'Email/Employee ID'
data.rename(columns ={'employee_no': 'Email/Employee ID'},inplace=True)

# Added new coloumn shift date to store date
data["ShiftDate"]=[d.date() for d in data["timestamp"]]

# Sorting by time in increasing order
data2=data.sort_values("timestamp",ascending=True) 

# To get data of day intime punches of all emplyees
# Adding a Intime Date and In Time columns to store correspomding data
data_first_punches=data2.drop_duplicates(subset=["Email/Employee ID","ShiftDate"],keep="first")
data_first_punches["Intime Date"]=[d.date() for d in data_first_punches["timestamp"]]
data_first_punches["In Time"]=[d.time().strftime("%H:%M") for d in data_first_punches["timestamp"]]

# To get data of day outime punches of all employees
# Adding a Intime Date and In Time columns to store correspomding data
data_last_punches=data2.drop_duplicates(subset=["Email/Employee ID","ShiftDate"],keep="last")
data_last_punches["Outtime Date"]=[d.date() for d in data_last_punches["timestamp"]]
data_last_punches["Out Time"]=[d.time().strftime("%H:%M") for d in data_last_punches["timestamp"]]


# Merging of Intime punches data and outtime punches data
output=pd.merge(data_first_punches,data_last_punches,how="outer",left_on=["Email/Employee ID","ShiftDate"],right_on=["Email/Employee ID","ShiftDate"])

# Addnig new column Break Duration
output["Break Duration"]=""

# Sorting the data by Email/Employee ID in increasing order
output=output.sort_values(["Email/Employee ID","ShiftDate"],ascending=True) 


#export output into My_output.csv
output.to_csv("My_output.csv",columns=["Email/Employee ID","ShiftDate","Intime Date","In Time","Outtime Date","Out Time","Break Duration"],index=False)


# In[ ]:





# In[ ]:




