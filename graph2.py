import MySQLdb
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# Connect
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="vinag",
                     db="miniproject")

cursor = db.cursor()

# Execute SQL select statement
sql="SELECT * FROM `yearly_data`"
cursor.execute(sql)
rows=cursor.fetchall()
#Transforming data into DataFrames
df=pd.DataFrame([[j for j in i] for i in rows])

choice1=input("Enter the Country Id:")

years=["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"]
count=np.arange(len(years))
data=df.iloc[choice1]
v=[]
labels=['san_total','san_urban','san_rural','water_total','water_rural','water_urban']
for k in range(len(labels)):
	v.append([data[3+k],data[9+k],data[15+k],data[21+k],data[27+k],data[33+k],data[39+k],data[45+k],data[51+k],data[57+k],data[63+k],data[69+k],data[75+k],data[81+k],data[87+k],data[93+k]])

line=[]
line2=[]
for i in range(6):
	for j in range(16):
		line2.append(v[i][j])
	line.append(line2)
	line2=[]

country=df.iloc[choice1,1]
print country
objects = np.arange(0,16,1)
name=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]

#multiline graph to visualise the improvement rate of the choosen country over last 15years.
plt.plot(objects,line[0],label='SanTotal')
plt.plot(objects,line[1],label='SanRural')
plt.plot(objects,line[2],label='SanUrban')
plt.plot(objects,line[3],label='WaterTotal')
plt.plot(objects,line[4],label='WaterRural')
plt.plot(objects,line[5],label='WaterUrban')
plt.xticks(count,name)
locs, labels = plt.xticks(objects,name)
plt.setp(labels, rotation=90)
plt.xlabel("Years")
plt.ylabel("Frequency of Improvement")
plt.legend()
plt.title("Improvement Rate Of Sanitation And Water In India(2000-2015) ")
plt.show()

# Close the connection
db.close()
