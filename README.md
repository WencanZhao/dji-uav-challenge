# DJI UAV Challenge

This repository presents an experimental study on **PID control tuning** and **flight log analysis** in the context of the DJI UAV Challenge.  
The project demonstrates how UAV flight stability can be quantitatively evaluated and improved using classical control theory.

---

## Motivation

In UAV applications, maintaining stable altitude and attitude is critical for safe and efficient flight.  
However, manual tuning of PID (Proportional–Integral–Derivative) parameters is often a trial-and-error process, prone to instability and overshoot.  

This project provides:
- A **simulation-based framework** to test PID controllers.
- A **data-driven approach** to analyze flight logs and visualize UAV responses.
- A reproducible workflow for UAV control experiments.

---

## Features

- 🛠 **PID Controller Simulation** (`simulate_pid.py`):  
  Models UAV altitude control under different PID settings.
- 📊 **Flight Log Analysis** (`analyze_log.py`):  
  Processes real/simulated flight logs to evaluate control performance.
- 📈 **Visualization**:  
  Generates plots of response curves, stability, and overshoot.
- 🔬 **Research-oriented workflow**:  
  Enables reproducible experiments for UAV control tuning.

---

## Project Structure


---

## Example Result

When running the analysis script, the following response curve can be generated:

![PID Response](results/pid_response.png)

The figure illustrates the deviation between **target altitude** and **measured altitude**, highlighting system stability and tuning effectiveness.

---

## Future Work

- Extend analysis to 6-DOF UAV dynamics.  
- Compare classical PID with modern control methods (LQR, MPC).  
- Integrate real-world DJI UAV flight data for validation.  

---

## Citation

If you find this project useful in your research or coursework, please cite:



