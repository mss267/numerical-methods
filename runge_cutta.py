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

dth = 5
dtl = 1e-9

while dth - dtl>1e-8:

  x_rk = x0
  v_rk = v0

  dt = 0.5*(dth+dtl)
  flag = 0

  for t in np.arange(dt, tmax, dt):
    
    # Analytical
    x_analytical = x0*math.sin(B*t + math.pi/2)
    v_analytical = x0*B*math.cos(B*t + math.pi/2)

    # RK4
    # dxdt=v; dvdt=-(k/m)x
    a_x = v_rk
    a_v = -(k/m)*x_rk
    b_x = v_rk + (dt/2)*a_v
    b_v = -(k/m)*(x_rk + (dt/2)*a_x)
    c_x = v_rk + (dt/2)*b_v
    c_v = -(k/m)*(x_rk + (dt/2)*b_x)
    d_x = v_rk + dt*c_v
    d_v = -(k/m)*(x_rk + dt*c_x)

    x_rk = x_rk + (dt/6)*(a_x + 2*b_x + 2*c_x + d_x)
    v_rk = v_rk + (dt/6)*(a_v + 2*b_v + 2*c_v + d_v)


    # Check timestep
    if abs(x_rk - x_analytical) > 0.01*x0 or abs(v_rk - v_analytical) > 0.01*x0*B:
      flag = 1
      break

  print("high:", dth," low:",dtl, "test: ",dt)

  if flag == 1:
    dth = dt
  else:
    dtl = dt

print(dt)
