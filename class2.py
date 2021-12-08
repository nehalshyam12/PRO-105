import csv
import plotly.express as px
import pandas as pd
import math

with open('class2.csv', newline='')as f:
    r=csv.reader(f)
    df=list(r)

df.pop(0)
totalmarks=0
totalentries=len(df)
for m in df:
    totalmarks += float(m[1])

mean=totalmarks/totalentries
squares=0
for m in df:
    m1=float(m[1])-mean
    squares+=(m1*m1)
variants=squares/totalentries
deviation=variants**0.5
print("Standard Deviation: ", deviation)
data=pd.read_csv("class2.csv")
graph=px.scatter(data, x="Student Number", y="Marks")
graph.update_layout(shapes=[dict(type='line', y0=mean, y1=mean, x0=0, x1=totalentries)])
graph.show()