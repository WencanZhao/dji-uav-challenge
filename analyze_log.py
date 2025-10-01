import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("results", exist_ok=True)

# 读取（默认用刚才模拟生成的日志）
df = pd.read_csv("data/sim_flight_log.csv")

t  = df["time_s"].values
sp = df["setpoint_m"].values
h  = df["altitude_m"].values
u  = df["control_u"].values

def metrics(y, t, sp):
    y = np.asarray(y); sp = float(sp[-1])
    overshoot = max(0.0, (y.max()-sp)/sp*100.0) if sp != 0 else 0.0
    try:
        t10 = t[np.where(y >= 0.1*sp)[0][0]]
        t90 = t[np.where(y >= 0.9*sp)[0][0]]
        rise = t90 - t10
    except IndexError:
        rise = np.nan
    band = 0.02*abs(sp)
    idx = np.where(np.abs(y-sp) > band)[0]
    settle = t[idx[-1]] if len(idx) else 0.0
    return overshoot, rise, settle

overshoot, rise, settle = metrics(h, t, sp)
print(f"[LOG] Overshoot: {overshoot:.1f}% | Rise: {rise:.2f}s | Settling: {settle:.2f}s")

plt.figure(figsize=(9,5))
plt.subplot(2,1,1)
plt.plot(t, h, label="Altitude (m)")
plt.plot(t, sp, "--", label="Setpoint")
plt.ylabel("Altitude (m)")
plt.title("Flight Log Response")
plt.legend(); plt.grid(True, alpha=0.3)

plt.subplot(2,1,2)
plt.plot(t, u, label="Control u")
plt.xlabel("Time (s)"); plt.ylabel("u")
plt.grid(True
