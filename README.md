# numerical-methods

The position and velocity of a simple harmonic oscillator are calculated over ten oscillations using three different numerical methods: Euler, Euler-Cromer, and 4th order Runge-Kutta. Each program compares a different numerical method with the analytical results, and calculates the maximum time-step for which the numerical values of position and velocity are within 1% of their analytical values.

The results produced are as follows:

Method | Maximum time-step (s)
--- | ---
Euler | 0.004
Euler-Cromer | 0.231
Runge-Kutte | 4.322

The Euler method gives the smallest maximum time-step. This implies that it is the least accurate numerical method of the three, since it takes the most iterations to produce results to 1% accuracy.

By contrast, the time-step given by the Runge-Kutta method is the largest, implying better agreement with the analytical solutions, as well as a more efficient approach.

The Euler method takes the gradient at each time-step, and uses it to calculate the direction of the next step forward. The Runge-Kutta method takes several gradients at the initial position, at a half-step forwards, and at a full-step forwards. This gives a more accurate value for the next step forward.

The higher number of gradient calculations makes the Runge-Kutta more accurate with fewer iterations.

The Euler-Cromer method is a more stable version of the Euler method and hence gives better results.
