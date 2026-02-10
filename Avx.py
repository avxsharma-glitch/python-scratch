import sys
print("Python executable:", sys.executable)

# =========================
# Core Python Libraries
# =========================
import os
import sys
import math
import random
import time
import datetime
import warnings
warnings.filterwarnings("ignore")

# =========================
# Numerical & Data Handling
# =========================
import numpy as np
import pandas as pd

# =========================
# Visualization
# =========================
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# Statistics
# =========================
from scipy import stats

# =========================
# Machine Learning
# =========================
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# =========================
# Deep Learning (optional)
# =========================
import torch
import torch.nn as nn

# =========================
# Utility
# =========================
from pathlib import Path

# =========================
# Configuration
# =========================
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

# =========================
# Demo Dataset
# =========================
np.random.seed(42)

data = {
    "feature_1": np.random.rand(100),
    "feature_2": np.random.rand(100),
    "target": np.random.rand(100) * 10
}

df = pd.DataFrame(data)

print("Dataset Preview:")
print(df.head())

# =========================
# Basic EDA
# =========================
print("\nSummary Statistics:")
print(df.describe())

# =========================
# Visualization
# =========================
sns.scatterplot(x="feature_1", y="target", data=df)
plt.title("Feature 1 vs Target")
plt.show()

# =========================
# Train/Test Split
# =========================
X = df[["feature_1", "feature_2"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# Scaling
# =========================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# =========================
# Model Training
# =========================
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# =========================
# Evaluation
# =========================
y_pred = model.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print(f"MSE: {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# =========================
# GPU Check (Colab)
# =========================
device = "cuda" if torch.cuda.is_available() else "cpu"
print("\nRunning on device:", device)

# =========================
# End
# =========================
print("\nScript executed successfully.")
