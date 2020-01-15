import csv
import sys
import matplotlib.pyplot as plt

def MovingAverage(x):  # Moving Avarage with ten terms
  ln=10
  r=[]
  for i in range(5,len(x)-5):
    s=x[i]
    for j in range(0,5):
      if j==0: s=s+x[i-5+j]*0.5
      else: s=s+x[i-5+j]
    for j in range(0,5):
      if j==4:s=s+x[i+1+j]*0.5
      else: s=s+x[i+1+j]
    s=s/10.0
    r.append(s)
  return r
filename=sys.argv[1]

a=[]
with open(filename, newline='') as csvfile:  #read every row of csv file
  csv1=csv.reader(csvfile)
  for row in csv1:   # make matrix with row of csv
    a.append(map(float,row))
    
b=[list(x) for x in list(zip(*a))]; # transpose matrix

time=b[0];x1=b[1];x2=b[2];  # time, second Tc, third Tc

t1=[];y1=[];y2=[]; # data in 610sec<=time<=810sec
for i in range(0,len(time)):
  if time[i] > 619.9 and time[i] < 810.1:
    t1.append(time[i]);
    y1.append(x1[i]);
    y2.append(x2[i]);

# before moving avarage
plt.title("before moving avarage, Tc2")
plt.plot(y1)
plt.show()
plt.title("before moving avarage, Tc3")
plt.plot(y2)
plt.show()

# after moving avarage
z1=MovingAverage(y1)
z2=MovingAverage(y2)
plt.title("after moving avarage, Tc2")
plt.plot(z1)
plt.show()
plt.title("after moving avarage, Tc3")
plt.plot(z2)
plt.show()

csvfile.close()