import numpy as np
import matplotlib.pyplot as plt

# 目标高度
target_altitude = 10  

# PID 参数
Kp, Ki, Kd = 0.6, 0.1, 0.05  

# 初始状态
altitude = 0
integral = 0
prev_error = 0
dt = 0.1  

altitudes = []
times = np.arange(0, 20, dt)

for t in times:
    error = target_altitude - altitude
    integral += error * dt
    derivative = (error - prev_error) / dt
    control = Kp * error + Ki * integral + Kd * derivative
    
    # 简化的动态模型
    altitude += control * dt  
    prev_error = error
    altitudes.append(altitude)

# 保存图像
plt.figure(figsize=(8, 5))
plt.plot(times, altitudes, label="Altitude (m)")
plt.axhline(target_altitude, color="r", linestyle="--", label="Target")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("PID Altitude Control Simulation")
plt.legend()
plt.grid(True)
plt.savefig("results/pid_response.png")
print("Simulation complete. Result saved to results/pid_response.png")
