import os, csv
import numpy as np
import matplotlib.pyplot as plt

# ============ 可调 PID 参数 ============
Kp, Ki, Kd = 1.2, 0.6, 0.08   # 你可以改这三项感受曲线变化
setpoint = 1.0                # 目标高度 1 米
dt = 0.01                     # 步长 10ms
T = 10.0                      # 模拟 10 秒
# =====================================

os.makedirs("results", exist_ok=True)
os.makedirs("data", exist_ok=True)

# 简化垂直动力学：二阶系统（速度衰减 + 推力驱动）
# v_dot = -v/tau + k*u
# h_dot = v
tau = 0.6
k = 2.0

n = int(T / dt)
t = np.arange(n) * dt
h = np.zeros(n)   # altitude
v = np.zeros(n)   # vertical velocity
u = np.zeros(n)   # control (thrust command)

err_int = 0.0
prev_err = 0.0

for i in range(1, n):
    err = setpoint - h[i-1]
    err_int += err * dt
    derr = (err - prev_err) / dt
    prev_err = err

    # PID
    u[i] = Kp*err + Ki*err_int + Kd*derr
    u[i] = np.clip(u[i], -1.0, 1.0)  # 推力限幅

    # Plant update
    v_dot = -v[i-1]/tau + k*u[i]
    v[i] = v[i-1] + v_dot * dt
    h[i] = h[i-1] + v[i] * dt

# 计算指标
def metrics(y, t, sp):
    y = np.asarray(y)
    sp = float(sp)
    # 超调
    overshoot = max(0.0, (y.max()-sp)/sp*100.0) if sp != 0 else 0.0
    # 上升时间（10%->90%）
    try:
        t10 = t[np.where(y >= 0.1*sp)[0][0]]
        t90 = t[np.where(y >= 0.9*sp)[0][0]]
        rise = t90 - t10
    except IndexError:
        rise = np.nan
    # 调整时间（2% 带宽）
    band = 0.02*abs(sp)
    idx = np.where(np.abs(y-sp) > band)[0]
    settle = t[idx[-1]] if len(idx) else 0.0
    return overshoot, rise, settle

overshoot, rise, settle = metrics(h, t, setpoint)
print(f"Overshoot: {overshoot:.1f}% | Rise time: {rise:.2f}s | Settling time: {settle:.2f}s")

# 保存曲线图
plt.figure(figsize=(9,5))
plt.plot(t, h, label="Altitude (m)")
plt.plot(t, [setpoint]*len(t), "--", label="Setpoint")
plt.plot(t, u, label="Control u (arb.)", alpha=0.7)
plt.xlabel("Time (s)"); plt.title("Altitude Step Response with PID")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("results/altitude_response_pid.png")
print("图已保存：results/altitude_response_pid.png")

# 保存日志 CSV
with open("data/sim_flight_log.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["time_s","setpoint_m","altitude_m","control_u"])
    for ti, hi, ui in zip(t, h, u):
        w.writerow([f"{ti:.2f}", setpoint, f"{hi:.4f}", f"{ui:.4f}"])
print("日志已保存：data/sim_flight_log.csv")
