import pandas as pd
import matplotlib.pyplot as plt

# 读取飞行日志
df = pd.read_csv("data/flight_log.csv")

# 画图
plt.figure(figsize=(8,5))
plt.plot(df["time"], df["altitude"], label="Actual Altitude", marker="o")
plt.plot(df["time"], df["target"], label="Target Altitude", linestyle="--")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("UAV Altitude Tracking")
plt.legend()
plt.grid(True)

# 保存结果
plt.savefig("results/pid_response.png")
print("图表已保存到 results/pid_response.png")
