import csv
import sys
import matplotlib.pyplot as plt

def MovingAverage(x):  # Moving Avarage with ten terms
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
  
def RotateLeft(x,n):  # n <= len(x)
  r=[]
  for i in range(0,len(x)):
    if i+n<len(x):
      r.append(x[i+n])
    else:
      r.append(x[i+n-len(x)])
  return r
  
def DotProduct(x,y):  # inner product
  r=0
  for i in range(0,len(x)):
    r=r+x[i]*y[i]
  return r
       
filename=sys.argv[1]  # name of input file = csv file

a=[]
with open(filename, newline='') as csvfile:  #read every row of csv file
  csv1=csv.reader(csvfile)
  for row in csv1:   # make matrix with row of csv
    a.append(map(float,row))
csvfile.close()
    
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

# time correlation
u=[]
for i in range(0,len(z2)):
  zl=RotateLeft(z2,i)
  u.append(DotProduct(z1,zl))

plt.title("time correlation of Tc2 and Tc3")
plt.plot(u)
plt.show()

v=[]
for i in range(0,250):  # find the first local max
  v.append(u[i])
mx=max(v)
print(mx)

for i in range(0,len(v)):   # find an index of local max
  if mx==v[i]:
    k=i
    break
t2=MovingAverage(t1)
print(t2[k]-t2[0])
