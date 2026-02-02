import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load CSV file
# -------------------------------
df = pd.read_csv("students.csv")

print("Dataset:")
print(df)

# -------------------------------
# 2. Basic Data Analysis
# -------------------------------
print("\nAverage Marks:")
print("Math:", df["Math"].mean())
print("Science:", df["Science"].mean())
print("English:", df["English"].mean())
print("Attendance:", df["Attendance"].mean())

print("\nSummary Statistics:")
print(df.describe())

# -------------------------------
# 3. Bar Chart: Average Marks
# -------------------------------
subjects = ["Math", "Science", "English"]
averages = [df[sub].mean() for sub in subjects]

plt.figure()
plt.bar(subjects, averages)
plt.title("Average Marks per Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()

# -------------------------------
# 4. Scatter Plot: Attendance vs Math
# -------------------------------
plt.figure()
plt.scatter(df["Attendance"], df["Math"])
plt.title("Attendance vs Math Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Math Score")
plt.show()

# -------------------------------
# 5. Heatmap: Correlation Matrix
# -------------------------------
correlation = df[["Math", "Science", "English", "Attendance"]].corr()

plt.figure()
plt.imshow(correlation)
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Heatmap")
plt.show()
