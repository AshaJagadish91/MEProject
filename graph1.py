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
sql="SELECT * FROM `deathData2012`"
cursor.execute(sql)
rows=cursor.fetchall()
#Transforming data into DataFrames
df=pd.DataFrame([[j for j in i] for i in rows])

print(df[2])
choice1=int(raw_input("Enter the Country id:"))
choice2=raw_input("1.Water 2.Sanitation 3.Hygiene Enter your choice: ")

a1=df[[3,6,9]][df[1]==choice1].values

if(choice2=='1'):
	a2=df[[3,4,5]][df[1]==choice1].values
elif(choice2=='2'):
	a2=df[[6,7,8]][df[1]==choice1].values
elif(choice2=='3'):
	a2=df[[9,10,11]][df[1]==choice1].values

#Pie chart to visualise the overall death rate of a choosen country under categories water,sanitation and hygiene. 
value1=[a1[0][0],a1[0][1],a1[0][2]]
label1=['water','sanitation','hygiene']
plt.subplot(211)
colors = ['yellowgreen', 'gold', 'lightskyblue']
explode = (0.1,0.1,0.1)
patches, texts,autot= plt.pie(value1,explode=explode,autopct='%1.0f%%', colors=colors, startangle=90)
plt.legend(patches, label1, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.title('Visualisation of Inadequacy of Water,Sanitation and Hygiene') 

#Bar chart to visualise the total death rate, children death rate and death per lakh of a choosen country under choosen category.
value2=[a2[0][0],a2[0][1],a2[0][2]]
label2=['Total_death','Children_death','Death_per_lakh']
ypos=np.arange(len(label2))
plt.subplot(212)
plt.bar(ypos,value2)
plt.xticks(ypos,label2)
plt.ylabel('Death Rate')
plt.title('Visualization of Particular Inadequacy')
plt.show()


# Close the connection
db.close()
