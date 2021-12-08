import pandas as pd
data=[60,61,65,63,98,99,90,95,91,96]
totalmarks=0
totalentries=len(data)
for m in data:
    totalmarks += float(m)

mean=totalmarks/totalentries
squares=0
for m in data:
    m1=float(m)-mean
    squares+=(m1*m1)
variants=squares/totalentries
deviation=variants**0.5
print("Standard Deviation: ", deviation)
print("Mean: ", mean)