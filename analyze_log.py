import pandas as pd
import matplotlib.pyplot as plt

# 假设日志在 data/flight_log.csv
log_path = "data/flight_log.csv"

try:
    df = pd.read_csv(log_path)
    print("Loaded flight log:")
    print(df.head())

    plt.figure(figsize=(8,5))
    plt.plot(df["time"], df["altitude"], label="Altitude")
    plt.plot(df["time"], df["target"], "--", label="Target")
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.title("Flight Log Analysis")
    plt.legend()
    plt.grid(True)
    plt.savefig("results/log_analysis.png")
    print("Analysis complete. Saved to results/log_analysis.png")

except FileNotFoundError:
    print("No flight log found. Please add data/flight_log.csv")
