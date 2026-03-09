import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

def KNeighbourPlayPredictor(Datapath):
    Border = "-"*40
    #--------------------------------------------------------------
    # Step 1 : Load dataset
    #--------------------------------------------------------------
    print(Border)
    print("Step 1 : Load dataset")
    print(Border)

    df = pd.read_csv("PlayPredictor.csv")

    print("Few records from dataset:")
    print(df.head())

    #--------------------------------------------------------------
    # Step 2 : Remove Unwanted columns
    #--------------------------------------------------------------
    print(Border)
    print("Step 2 : Remove Unwanted columns")
    print(Border)

    print("Shape of dataset before removal of Unwanted column:",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)

    print("Shape of dataset after removal of Unwanted column:",df.shape)

    #--------------------------------------------------------------
    # Step 3 : Check missing value
    #--------------------------------------------------------------
    print(Border)
    print("Step 2 : Check missing value")
    print(Border)

    print("Missing value count : \n",df.isnull().sum())

    #--------------------------------------------------------------
    # Step 4 : Display Statistical Summary
    #--------------------------------------------------------------
    print(Border)
    print("Step 3 : Display Statistical Summary")
    print(Border)

    print(df.describe())

    #--------------------------------------------------------------
    # Step 5 : Encoding using LabelEncoder(Generally Label Encoding should be done before train test split)
    #--------------------------------------------------------------
    print(Border)
    print("Step 5 : Encoding using LabelEncoder")
    print(Border)

    cols = ['Whether','Temperature','Play'] 
    le = LabelEncoder()
    for col in cols:
        df[col] = le.fit_transform(df[col])
    print(df)

    #--------------------------------------------------------------
    # Step 6 : Corelation between columns
    #--------------------------------------------------------------
    print(Border)
    print("Step 6 : Corelation between columns")
    print(Border)

    print("Corelation matrix:")
    print(df.corr())

    #----------------------------------------------------------------
    # Step 7 : Split Dataset into Independent and Dependent variables
    #----------------------------------------------------------------
    print(Border)
    print("Step 7 : Split Dataset into Independent and Dependent variables")
    print(Border)

    X = df.drop(columns=['Play'])
    Y = df['Play']

    print("Shape of X:",X.shape)
    print("Shape of Y:",Y.shape)

    print(Border)
    print("Input Variables:",X.columns.to_list()) # .columns works only for Dataframe not for series
    print("Output Variables: Play") # Y is series means only one column is there 

    #----------------------------------------------------------------
    # Step 8 : Split Dataset for Training and Testing
    #----------------------------------------------------------------

    print(Border)
    print("Step 8 : Split Dataset for Training and Testing")
    print(Border)

    X_Train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_train shape:",X_Train.shape)
    print("X_test shape:",X_Test.shape)
    print("Y_train shape:",Y_Train.shape)
    print("Y_test shape:",Y_Test.shape)

    #----------------------------------------------------------------
    # Step 9 : Explore the multiple value of K
    #----------------------------------------------------------------

    print(Border)
    print("Step 9 : Split Dataset for Training and Testing")
    print(Border)

    accuracy_scores = []
    K_values = range(1,10)

    for K in K_values:
        model = KNeighborsClassifier(n_neighbors=K)
        model.fit(X_Train,Y_Train)
        Y_pred = model.predict(X_Test)
        accuracy = accuracy_score(Y_Test,Y_pred)
        accuracy_scores.append(accuracy)
    
    print(Border)
    print("Accuracy report of all K values from 1 to 20")
    for value in accuracy_scores:
        print(value)

    print(Border)

    #----------------------------------------------------------------
    # Step 10 : Find best value of K
    #----------------------------------------------------------------

    print(Border)
    print("Step 10 : Find best value of K")
    print(Border)

    best_KValue = list(K_values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best K value is:",best_KValue)

    #----------------------------------------------------------------
    # Step 11 : Build Final model using best value of K
    #----------------------------------------------------------------

    print(Border)
    print("Step 11 : Build Final model using best value of K")
    print(Border)

    Final_model = KNeighborsClassifier(n_neighbors=best_KValue)
    Final_model.fit(X_Train,Y_Train)
    Y_pred = Final_model.predict(X_Test)

    #----------------------------------------------------------------
    # Step 12 : Calculate Final accuracy
    #----------------------------------------------------------------

    print(Border)
    print("Step 12 : Calculate Final accuracy")
    print(Border)

    Final_accuracy = accuracy_score(Y_Test,Y_pred)
    print("Final accuracy is:",Final_accuracy)

    #----------------------------------------------------------------
    # Step 13 : Display Confusion matrix(Confusion matrix only shows test data)
    #----------------------------------------------------------------

    print(Border)
    print("Step 13 : Display Confusion matrix")
    print(Border)

    cm = confusion_matrix(Y_Test,Y_pred)
    print(cm)

    #----------------------------------------------------------------
    # Step 13 : Display Classification report
    #----------------------------------------------------------------

    print(Border)
    print("Step 13 : Display Classification report")
    print(Border)

    print(classification_report(Y_Test,Y_pred))

def main():
    Border = "-"*40
    print(Border)
    print("PlayPredictor using KNN:")
    print(Border)

    KNeighbourPlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()
