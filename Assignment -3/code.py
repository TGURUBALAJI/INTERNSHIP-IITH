import numpy as np
import math
import matplotlib.pyplot as plt

r = np.array( [-3+((-2)*math.cos(math.pi/3)), -2*(math.sin(math.pi/3))] ) 
q = np.array( [-6+((7)*math.cos(math.pi/3)), 7*(math.sin(math.pi/3))] ) 
p = (r-q)
print (p**2)

i = np.array( [1, 0] ) 
i1 = np.array( [0, 1] )

distance = np.sqrt(((p**2)@i1) + ((p**2)@i))
print(distance)


plt.rcParams["figure.figsize"] = [10, 10]
plt.rcParams["figure.autolayout"] = True
x = np.linspace(1, 10, 1000)
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
# end points
A = np.array([-3 ,-2]) 
B = np.array([-6, 7])
c = np.array([-10 ,-10*(math.sqrt(3))])
d = np.array([10, 10*(math.sqrt(3))])


plt.axvline(x=0, c="black", label="x-axis")
plt.axhline(y=0, c="black", label="y-axis")


x_AB = line_gen(A,B)
x_cd = line_gen(c,d)
x_rq = line_gen(r,q)

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_rq[0,:],x_rq[1,:],label='$RQ$')
plt.plot(x_cd[0,:],x_cd[1,:],label = "$CD-transformed-axis$")
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')

plt.plot(c[0], c[1], 'o')
plt.text(c[0] * (1 - 0.2), c[1] * (1) , 'C')
plt.plot(d[0], d[1], 'o')
plt.text(d[0] * (1 - 0.2), d[1] * (1) , 'D')

plt.plot(r[0], r[1], 'o')
plt.text(r[0] * (1 - 0.2), r[1] * (1) , 'R')
plt.plot(q[0], q[1], 'o')
plt.text(q[0] * (1 - 0.2), q[1] * (1) , 'Q')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid()
plt.show()
