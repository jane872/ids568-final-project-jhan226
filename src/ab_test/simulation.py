
import numpy as np
import scipy.stats as stats

np.random.seed(42)
n = 1000
A_acc = np.random.normal(0.85, 0.05, n)
B_acc = np.random.normal(0.89, 0.04, n)
A_lat = np.random.normal(0.20, 0.05, n)
B_lat = np.random.normal(0.15, 0.04, n)

t_acc, p_acc = stats.ttest_ind(A_acc, B_acc)
t_lat, p_lat = stats.ttest_ind(A_lat, B_lat)

print(f"Accuracy p-value: {p_acc:.4f}")
print(f"Latency p-value: {p_lat:.4f}")
