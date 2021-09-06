import numpy as np
import matplotlib.pyplot as plt

# (0 5)x=6          eq....1
# (1 0)x = 12       eq....2
# (-5 0)x = -16     eq....3
# (-2 -3)x =  0     eq....4
# (3 32)x = 0       eq....5

X_cor, Y_cor = [30, -30],[30, -30]  ###limits of graph

##### let A.X = B be general equation
##### then C = A
#####      c = B

def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def y_cal(C,c,x): 
  y1 = (c - x[0]*C[0])/C[1]
  y2 = (c - x[1]*C[0])/C[1]
  return y1,y2

def x_cal(C,c,y):
  x1 = (c - y[0]*C[1])/C[0]
  x2 = (c - y[1]*C[1])/C[0]
  return x1,x2

####  a) Line Parallel to x-axix  ######
#################################################
Y = y_cal([0,5], 6 ,X_cor) ###calculating x cordinates for eq 1
P1, P2 = np.array([X_cor[0],Y[0]]),np.array([X_cor[1],Y[1]])
x_FP=line_gen(P1,P2) ###  Line Generation of eq 1
plt.plot(x_FP[0,:],x_FP[1,:],label='(0 5)X = 6')
plt.plot(P1[0], P1[1], 'o')
plt.text(P1[0] * (1 - 0.1), P1[1] * (1 + 0.1) , 'A')
plt.plot(P2[0], P2[1], 'o')
plt.text(P2[0] * (1 - 0.3), P2[1] * (1 + 0.2) , 'B')

# plt.grid() 
# plt.xlabel('$x$')
# plt.ylabel('$y$')
# plt.legend(loc='upper right')
# plt.axis('equal')
# plt.show()
#################################################

####  b) lines parallel to y- axis  ######
#################################################
X = x_cal([1,0],12,Y_cor) ###calculating y cordinates for eq 2
P1, P2 = np.array([X[0],Y_cor[0]]),np.array([X[1],Y_cor[1]])
x_FP=line_gen(P1,P2) ###  Line Generation of eq 2
plt.plot(x_FP[0,:],x_FP[1,:],label='(1 0)X = 12')
plt.plot(P1[0], P1[1], 'o')
plt.text(P1[0] * (1 - 0.1), P1[1] * (1 + 0.1) , 'C')
plt.plot(P2[0], P2[1], 'o')
plt.text(P2[0] * (1 - 0.1), P2[1] * (1 + 0.1) , 'D')

X = x_cal([-5,0],-16,Y_cor) ###calculating y cordinates for eq 3
P1, P2 = np.array([X[0],Y_cor[0]]),np.array([X[1],Y_cor[1]])
x_FP=line_gen(P1,P2) ###  ###  Line Generation of eq 3
plt.plot(x_FP[0,:],x_FP[1,:],label='(-5 0)X = -16')
plt.plot(P1[0], P1[1], 'o')
plt.text(P1[0] * (1 - 0.1), P1[1] * (1 + 0.1) , 'E')
plt.plot(P2[0], P2[1], 'o')
plt.text(P2[0] * (1 - 0.1), P2[1] * (1 + 0.1) , 'F')

# plt.grid() 
# plt.xlabel('$x$')
# plt.ylabel('$y$')
# plt.legend(loc='upper center')
# plt.axis('equal')
# plt.show()
#################################################

####  Lines passing through Origin  ######
#################################################
Y = y_cal([-2,-3],0,X_cor) ###calculating y cordinates for eq 4
P1, P2 = np.array([X_cor[0],Y[0]]),np.array([X_cor[1],Y[1]])
x_FP=line_gen(P1,P2) ###  Line Generation of eq 4
plt.plot(x_FP[0,:],x_FP[1,:],label='(-2 -3)X = 0')
plt.plot(P1[0], P1[1], 'o')
plt.text(P1[0] * (1 - 0.1), P1[1] * (1 + 0.1) , 'G')
plt.plot(P2[0], P2[1], 'o')
plt.text(P2[0] * (1 - 0.1), P2[1] * (1 + 0.1) , 'H')

Y = y_cal([3,32],0,X_cor) ###calculating y cordinates for eq 5
P1, P2 = np.array([X_cor[0],Y[0]]),np.array([X_cor[1],Y[1]])
x_FP=line_gen(P1,P2) ###  ###  Line Generation of eq 5
plt.plot(x_FP[0,:],x_FP[1,:],label='(3 32)X = 0')
plt.plot(P1[0], P1[1], 'o')
plt.text(P1[0] * (1 - 0.1), P1[1] * (1 + 0.2) , 'I')
plt.plot(P2[0], P2[1], 'o')
plt.text(P2[0] * (1 - 0.1), P2[1] * (1 + 0.2) , 'J')

plt.grid() 
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='lower left')
plt.axis('equal')
plt.show()
#################################################
