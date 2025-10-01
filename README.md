# DJI UAV Challenge 

This project explores **PID control tuning** and **flight log analysis** in the context of the DJI UAV Challenge.  
It demonstrates how UAV flight stability can be analyzed and improved using classical control methods.  

---

##  Background  

During the DJI UAV Challenge, one of the key tasks was to maintain stable altitude control.  
Manually tuning PID (Proportional–Integral–Derivative) parameters is often time-consuming and unintuitive.  
This project replicates the process by simulating PID control and analyzing UAV flight logs.  

---

##  Features  

- Simulate altitude control with a **PID controller** (`simulate_pid.py`)  
- Analyze UAV **flight log data** (`analyze_log.py`)  
- Visualize response curves, stability, and overshoot  
- Provide a structured workflow for experimenting with PID tuning  

---

##  Project Structure  

## Example Result

When you run the analysis script, you’ll get a figure like this:

![PID Response](results/pid_response.png)
