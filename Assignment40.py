import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score,confusion_matrix)

Dataframe = "student_performance_ml.csv"
df = pd.read_csv(Dataframe)

feature_values = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X = df[feature_values]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.2, random_state=10)

model = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=10)

model.fit(X_train,Y_train)

# Question 1 in Assignment Calculating importance score of each Feature
feature_importance = model.feature_importances_

for feature,importance in zip(feature_values,feature_importance): # zip() is used to join two list position by position
    print(feature,":",importance)

# Attendence Feature is contributing the most in predicting FinalResult.
# Remaining all Feature contributes the least.

Y_pred = model.predict(X_test)

print("Actual Value:")
print(Y_test)

print("Predicted Value:")
print(Y_pred)

Accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy is:",Accuracy*100)

# Question 2 in Assignment Removing the column SleepHours from the dataset

df1 = df.drop("SleepHours", axis=1) # axis=1 means column and axis=0 means row

feature_values1 = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted"]

X1 = df1[feature_values1]
Y1 = df1["FinalResult"]

X1_train, X1_test, Y1_train, Y1_test = train_test_split(X1, Y1, test_size=0.2, random_state=10)

model1 = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=10)

model1.fit(X1_train,Y1_train)

Y1_pred = model1.predict(X1_test)

Accuracy1 = accuracy_score(Y1_test,Y1_pred)
print("Accuracy after removing SleepHours Feature:",Accuracy1*100)

# Removing SleeHours Feature doesn't affect Performance

