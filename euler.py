import matplotlib.pyplot as plt
import numpy as np
import math

# Student number 40 26 00 33

# Constants
k = 1
m = 33+100
x0 = 0.1
v0 = 0
tmax = 724.6
w = math.sqrt(k)/(2*math.pi*math.sqrt(m))
t = 0
B = math.sqrt(k/m)

dth = 3
dtl = 1e-9

while dth - dtl>1e-8:

  x_old = x0
  v_old = v0

  dt = 0.5*(dth+dtl)
  flag = 0

  for t in np.arange(dt, tmax, dt):
    
    # Analytical
    x_analytical = x0*math.sin(B*t + math.pi/2)
    v_analytical = x0*B*math.cos(B*t + math.pi/2)

    # Euler
    v = v_old + dt*(-k/m)*x_old
    x = x_old + dt*v_old

    x_old = x
    v_old = v

    # Check timestep
    if abs(x - x_analytical) > 0.01*x0 or abs(v - v_analytical) > 0.01*x0*B:
      flag = 1
      break

  print("high:", dth," low:",dtl, "test: ",dt)

  if flag == 1:
    dth = dt
  else:
    dtl = dt

print(dt)
