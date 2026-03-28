import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier

def DecisionTreeclassifierKNN(Datapath):

#Step 1 : Load the Dataset from csv file

    df = pd.read_csv(Datapath)
    print("Few entries from the Dataset")
    print(df.head())

#Step 2 : Clean the dataset by removing empty rows

    df.dropna(inplace=True)
    print("Total Rows:",df.shape[0])
    print("Total Columns:",df.shape[1])

#Step 3 : Seperate Independent and Dependent Variable
    X = df.drop(columns=['Outcome'])
    Y = df['Outcome']     # 1 means Patient is dibetic and 0 means Patient is not dibetic

    print("Shape of Independent Variable",X.shape)
    print("Shape of Dependent Variable",Y.shape)

    print("Input column:",X.columns.to_list())
    print("Output column: Outcome")

    print("All statistics values:")
    print(df.describe())

    print("Distribution of the target variable using graph:")

    sns.countplot(x = 'Outcome', data = df)
    plt.title("Distribution of Target Variable")
    plt.xlabel("Classes")
    plt.ylabel("Count")
    plt.show()

    print("Identifying outliers:")

    plt.figure(figsize=(12,6))
    sns.boxplot(data=df)
    plt.xticks(rotation=90) # rotation=90 means axis labels(text) is vertical
    plt.show()

    #sns.pairplot(df)
    #plt.show()

#Step 4 : Handling missing or zero values

    cols = ['BloodPressure','SkinThickness','Insulin','BMI']
    df[cols] = df[cols].replace(0, np.nan)
    df[cols] = df.groupby('Outcome')[cols].transform(lambda x: x.fillna(x.median()))
    print(df[cols])

#Step 5 : Split the dataset for Training and Testing

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Information of Training and Testing Data:")
    print("X_train shape:",X_train.shape)
    print("X_test shape:",X_test.shape)
    print("Y_train shape:",Y_train.shape)
    print("Y_test shape:",Y_test.shape)

#Step 6 : Feature Scaling

    scalar = StandardScaler()

    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("Feature Scaling is Done.")

#Step 7 : Building Decision Tree Model

    model = DecisionTreeClassifier(max_depth=3,random_state=42)
    model.fit(X_train_scaled,Y_train)
    Y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy of Decision Tree model is:",accuracy)

#Step 8 : Building KNN Model(Explor the multiple values of K)
#Hyperparameter Tuning(K)

    accuracy_scores = []
    K_values = range(1,10)

    for k in K_values:
        Knnmodel = KNeighborsClassifier(n_neighbors=k)
        Knnmodel.fit(X_train_scaled,Y_train)
        Y_Knnpred = Knnmodel.predict(X_test_scaled)
        accuracyKNN = accuracy_score(Y_test,Y_Knnpred)
        accuracy_scores.append(accuracyKNN)

    print("Accuracy of KNN model is:")
    for value in accuracy_scores:
        print(value)

#Step 9 : Display Confusion Matrix

    cm = confusion_matrix(Y_test,Y_pred)
    cmknn = confusion_matrix(Y_test,Y_Knnpred)

    print("Confusion matrix of Decision Tree:")
    print(cm)
    print("Confusion matrix of K Nearest Neighbour:")
    print(cmknn)

#Step 10 : Display Classification report

    print("Classification report of Decision tree:")
    print(classification_report(Y_test,Y_pred))
    print("Classification report of K Nearest Neighbour:")
    print(classification_report(Y_test,Y_Knnpred))

#Step 11 : Visualise Confusion matrix of Decision Tree

    sns.heatmap(cm,annot=True,fmt='d')
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion matrix")
    plt.show()

#Step 12 : Visualise Confusion matrix of KNN

    sns.heatmap(cmknn,annot=True,fmt='d') #annot=True (Show numbers inside each box of the heatmap), fmt='d'(Format of the numbers displayed) 'd' = integer (decimal) format
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion matrix")
    plt.show()

#Step 13 : Predict whether patient is diabetic

    new_data = pd.DataFrame([[6,148,72,35,0,33.6,0.627,40]],columns=X.columns)
    prediction = model.predict(new_data)

    if prediction[0] == 1:
        print("Patient is Diabetic")
    else:
        print("Patient is not Diabetic")


def main():
    DecisionTreeclassifierKNN("diabetes.csv")

if __name__ == '__main__':
    main()

