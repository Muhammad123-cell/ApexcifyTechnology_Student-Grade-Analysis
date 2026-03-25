import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("students.csv")

print("\n========== STUDENT GRADE ANALYSIS ==========\n")

# Students Average
df["Average"] = df[["Math", "English", "Science"]].mean(axis=1)

print("Students' Average Score")
print(df[["Name","Math","English","Science","Average"]].to_string(index=False)) 

# Grade Assigning
def assign_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 55:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(assign_grade)

# ✅ Ranking Students (FIXED)
df["Rank"] = df["Average"].rank(method="dense", ascending=False).astype(int)

# Top Student
top_student = df.loc[df["Average"].idxmax()]

print("\n========== TOP STUDENT ==========\n")

print("Name:", top_student["Name"])
print("Grade:", top_student["Grade"])
print("Math:", top_student["Math"])
print("English:", top_student["English"])
print("Science:", top_student["Science"])
print("Average:", round(top_student["Average"],2))

# Top 5 Students
print("\n========== TOP 5 STUDENTS ==========\n")

top5 = df.sort_values(by="Average", ascending=False).head(5)

print(top5[["Rank","Name","Math","English","Science","Average","Grade"]].to_string(index=False))  

# Subject Toppers
print("\n========== SUBJECT TOPPERS ==========\n")

math_topper = df.loc[df["Math"].idxmax()]
english_topper = df.loc[df["English"].idxmax()]
science_topper = df.loc[df["Science"].idxmax()]

print("Math Topper:", math_topper["Name"], "-", math_topper["Math"])
print("English Topper:", english_topper["Name"], "-", english_topper["English"])
print("Science Topper:", science_topper["Name"], "-", science_topper["Science"])

# Class Stats
print("\n========== CLASS STATISTICS ==========\n")

stats = df[["Math","English","Science","Average"]].describe()
print(stats)

# Grades Distribution
print("\n========== GRADE DISTRIBUTION ==========\n")

grade_counts = df["Grade"].value_counts().sort_index()

for grade, count in grade_counts.items():
    print(f"Grade {grade}: {count} students")

# Graphs
# 1.Bar Chart: Subject Averages

subject_means = df[["Math","English","Science"]].mean()
sorted_subjects = subject_means.sort_values(ascending=False)
color_map = {}
color_order = ["green", "orange", "red"]

for i, subject in enumerate(sorted_subjects.index):
    color_map[subject] = color_order[i]
colors = [color_map[sub] for sub in subject_means.index]

plt.figure()
subject_means.plot(kind="bar", color=colors)
plt.title("Average Marks per Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()

# 2.Histogram: Average Distribution
plt.figure()
plt.hist(df["Average"], bins=10)
plt.title("Distribution of Student Averages")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.show()

# 3.Pie Chart: Grade Distribution
grade_counts = df["Grade"].value_counts()

plt.figure()
plt.pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%")
plt.title("Grade Distribution")
plt.show()
