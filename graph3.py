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

#retreiving data of Asia
a1=df[df[3]==1].values
asia=pd.DataFrame(a1)
#print asia

#retreiving data of Africa
a2=df[df[3]==2].values
africa=pd.DataFrame(a2)
#print africa

#retreiving data of North_america
a3=df[df[3]==3].values
north_america=pd.DataFrame(a3)
#print north_america

#retreiving data of South_america
a4=df[df[3]==4].values
south_america=pd.DataFrame(a4)
#print south_america


#retreiving data of Antractica
a5=df[df[3]==5].values
antractica=pd.DataFrame(a5)
#print antractica

#retreiving data of Europe
a6=df[df[3]==6].values
europe=pd.DataFrame(a6)
#print europe

#retreiving data of Australia
a7=df[df[3]==7].values
australia=pd.DataFrame(a7)
#print australia

a=int(df.iloc[54,76])
b=int(df.iloc[54,76])
c=int(df.iloc[77,76])
d=int(df.iloc[17,76])
e=int(df.iloc[98,76])
f=int(df.iloc[7,76])

a1=int(df.iloc[54,79])
b1=int(df.iloc[54,79])
c1=int(df.iloc[77,79])
d1=int(df.iloc[17,79])
e1=int(df.iloc[98,79])
f1=int(df.iloc[7,79])

l=['Sanitation','Water']
val=[a,b,c,d,e,f]
val1=[a1,b1,c1,d1,e1,f1]

#Bar graph to visualise the improvement happened in Sanitation and Water by the Continents in the year 2008.
label1=['Asia','Africa','North_america','South_america','Europe','Australia']
X=np.arange(len(label1))
wid=.35
plt.bar(X + 0.00, val, color = 'b', width = 0.25)
plt.bar(X + 0.25, val1, color = 'g', width = 0.25)
plt.ylabel("Percentage Improvement")
plt.xlabel("COntinents")
locs, labels = plt.xticks(X,label1)
plt.setp(labels, rotation=15)
plt.title("Sanitation And Water Improvement By Continents-2008")
plt.legend(l,loc=2)
plt.show()

# Close the connection
db.close()
