import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/students.csv")

# Display the data
print("STUDENT DATA")
print(df)

# Display basic information
print("\nDATASET INFORMATION")
print(df.info())

# Calculate each student's average
df["Average"] = df[["Math", "Python", "English"]].mean(axis=1)

print("\nSTUDENT AVERAGES")
print(df[["Name", "Average"]])

# Calculate class statistics
class_average = df["Average"].mean()
highest_average = df["Average"].max()
lowest_average = df["Average"].min()

# Find the best-performing student
best_student = df.loc[df["Average"].idxmax(), "Name"]

# Display the results
print("\nCLASS STATISTICS")
print(f"Class average: {class_average:.2f}/20")
print(f"Highest average: {highest_average:.2f}/20")
print(f"Lowest average: {lowest_average:.2f}/20")
print(f"Best-performing student: {best_student}")

# Create a bar chart
plt.figure(figsize=(10, 6))

plt.bar(df["Name"], df["Average"], color="skyblue")

plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Average Grade / 20")

plt.ylim(0, 20)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

# Save the results
df.to_csv("data/student_results.csv", index=False)

print("\nResults saved to data/student_results.csv")
