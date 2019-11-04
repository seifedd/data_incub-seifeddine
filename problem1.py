"""
Please answer as many questions as you can. We do not expect you to answer them all, but you must answer at least one for each section.
Answering more questions correctly will help you and answering them incorrectly will not hurt you. Please give
all numerical answers to 10 digits of precision. Partial credit will be given to answers that agree to less than 10 digits. (*) denotes a required field.


"""
import csv
import pandas as pd
#Arrest dataset CSV name
filename="Arrest_Data_from_2010_to_Present.csv"

# with open(filename, newline='') as csvfile:
#     reader=csv.reader(csvfile, delimiter=',', quotechar='|')
#     for row in reader:
#         print(','.join(row))

#Read the results as dataframe and assign the result to arrests
arrests=pd.read_csv(filename)
print(arrests.head(10))

print("Shape :", arrests.shape)

# Extract the date from arrests records
arr_date=arrests['Arrest Date'];

s=[i.split('/') for i in arr_date];
res=[]
res_month,res_day,res_year=[],[],[]
for i,x in enumerate(s):
    element=list(map(int,[j for j in x]))
    res.append(element)

arrests['day']=list([ mmonth[0] for mmonth in res])
arrests['month']=list([day[1] for day in res])
arrests['year']=list([myear[2] for myear in res])

# How many arrests in 2018
arrests_2018=arrests[arrests['year']==2018];
print("The number arrests made in 2018:",len(arrests[arrests['year']==2018]))

#The area with the most arrests in 2018
df=arrests
df1 = df.groupby('Area ID')['year'].sum().to_fra    me().reset_index().sort_values(by='year')
print(df1[])