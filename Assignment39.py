import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import(accuracy_score, confusion_matrix, classification_report,
ConfusionMatrixDisplay)

Dataframe = "student_performance_ml.csv"

df = pd.read_csv(Dataframe)

feature_values = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X = df[feature_values]
Y = df["FinalResult"] 

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Creating a object model
# model = DecisionTreeClassifier(criterion='gini',max_depth=2,random_state=42) # 100% accuracy 
model = DecisionTreeClassifier(criterion='gini',max_depth=3,random_state=42) # 100 % accuracy
# model = DecisionTreeClassifier(criterion='gini',max_depth=None,random_state=42) # 100% accuracy

# Training the model using fit()
model.fit(X_train,Y_train)

# Using the trained model to predict the results for X_test
Y_pred = model.predict(X_test)

#Displaying Predicted values along with Actual Values
print("Actual Values:")
print(Y_test)

print("Predicted Values:")
print(Y_pred)

#Calculating accuracy using accuracy_score
Accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of model is:",Accuracy*100)

#Confusion matrix
Confusion_matrix = confusion_matrix(Y_test, Y_pred) # there are 6 values in test data which is 5 0 value and 1 1 value
print("Confusion matrix:")
print(Confusion_matrix)

Display = ConfusionMatrixDisplay(confusion_matrix=Confusion_matrix)
Display.plot()
plt.title("Confusion matrix")
plt.show()

# Explaination:
# from confusion matrix 5 (True 0->Predicted 0) values that is True Negative
# 0 value that is Fail predicted as pass it is False Positive
# 0 value that is Pass predicted as Fail it is False Negative
# 1 value that is Pass predicted as Pass it is True Positive

# Calculating Training accuracy
Y_train_pred = model.predict(X_train)
train_accuracy = accuracy_score(Y_train,Y_train_pred)
print("Training Accuracy:",train_accuracy*100)

# Calculating Testing accuracy
Y_test_pred = model.predict(X_test)
test_accuracy = accuracy_score(Y_test,Y_test_pred)
print("Testing Accuracy:",test_accuracy*100)

# Comment: Training and Testing both Accuracy is 100% then the model is neither Overfitting nor 
# Underfitting. It is perfectly fitted model for this dataset.
# It usually happens when Dataset is very small or problem is very easy/linearly seperable.

# Question 7 in Assignmnet
import numpy as np

new_data = pd.DataFrame([[6, 85, 66, 7, 7]], columns=["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"])

prediction = model.predict(new_data)

if prediction[0] == 1:          # If 1st value of prediction is 1 then student is pass
    print("Student is Pass")
else:
    print("Student is fail")

