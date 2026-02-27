import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Question 1 in Assignment
Dataframe = "student_performance_ml.csv"
df = pd.read_csv(Dataframe)

print("Fist 5 records:")
print(df.head())

print("Last 5 records:")
print(df.tail())

print("Total number of rows and columns:")
print(df.shape)

print("List of column names:")
print(df.columns)

print("Data types of each column:")
print(df.dtypes)

# Question 2 in Assignment
print("Total number of students in Dataset:")
print(len(df))

print("Count of Students Passed:")
print((df["FinalResult"] == 1).sum())

print("Count of Students Failed:")
print((df["FinalResult"] == 0).sum())

# Question 3 in Assignment
print("Average StudyHours:")
print(df["StudyHours"].mean())

print("Average Attendance:")
print(df["Attendance"].mean())

print("Maximum PreviousScore:")
print(df["PreviousScore"].max())

print("Minimum SleepHours:")
print(df["SleepHours"].min())

# Question 4 in Assignment
print("Distribution of FinalResult:")
print(df["FinalResult"].value_counts())

print("Percentage of Pass and Fail student:")
print(df["FinalResult"].value_counts(normalize=True)*100)  # 1=60%, 0=40%

# Justification:
# The dataset contains 60% passed students and 30% Failed students. since both classes are present in comparable
# propertions and no class dominates the dataset, it can be considered reasonably balanced.

# Question 5 in Assignment
# Observation:
# From the dataset, students with the high StudyHours are more likely to have a FinalResult of Pass
# compared to those with lower study hours. This indicates that increased study time improves 
# academic performance. Similarly, student with higher Attendance show better final results,
# as regular class participation helps in understanding the subject better. Overall, both StudyHours
# and Attendance have a positive relationship with the final outcome. Hence, higher StudyHours and Attendance 
# increase the chances of passing.

# Question 6 in Assignment
sns.histplot(df["StudyHours"])
plt.show()

# The distribution tells The 1-2 hours range has a high count (around 6 students), which means many students
# study very little. The 4-7 hours range also has high counts, showing many students study moderate to higher
# hours. The study hours are not concentrated in a single range; instead they are spread across low,medium and
# high study hours. This indicates a diverse distribution of StudyHours, covering both low-effort and high-effort students.

# Question 7 in Assignment
pass_student = df[df["FinalResult"] == 1]
fail_student = df[df["FinalResult"] == 0]

plt.scatter(pass_student["StudyHours"],pass_student["PreviousScore"], label='Pass')
plt.scatter(fail_student["StudyHours"],fail_student["PreviousScore"], label='Fail')
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.legend()
plt.title("StudyHours vs PreviousScore")
plt.show()

# Question 8 in Assignment
sns.boxplot(x=df["Attendance"])
plt.show()

# Question 9 in Assignment
plt.bar(df["FinalResult"], df["AssignmentsCompleted"])
plt.xticks([0,1],["Fail","Pass"])
plt.show()

# Observation:
# Students who passed have completed significantly more assignments on average than student who failed 
# The Pass bar is much higher than the Fail bar, showing a clear difference between the two
# groups. This indicated a positive relationship between AssignmentsCompleted and FinalResult.

# Question 10 in Assignment
plt.scatter(df["SleepHours"],df["FinalResult"])
plt.yticks([0,1],['Fail','Pass'])
plt.xlabel("SleepHours")
plt.ylabel("FinalResult")
plt.title("SleepHours against FinalResult")
plt.show()

