import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def MarvellousClassifier(Datapath):
    Border = "-"*40

    #Step 1 : Load the Dataset from csv file

    print(Border)
    print("Step 1 : Load the Dataset from csv file")
    print(Border)

    df = pd.read_csv(Datapath)
    print("Few entries from dataset")
    print(df.head())
    print(Border)

    #Step 2 : Clean the dataset by removing empty rows

    print(Border)
    print("Step 2 : Clean the dataset by removing empty rows")
    print(Border)

    df.dropna(inplace=True)
    print("Total rows:",df.shape[0])
    print("Total columns:",df.shape[1])

    #Step 3 : Seperate Independent and Dependent Variables

    print(Border)
    print("Step 3 : Seperate Independent and Dependent Variables")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X:",X.shape)
    print("Shape of Y:",Y.shape)

    print(Border)
    print("Input columns :",X.columns.to_list())
    print("Output columns : Class")

    #Step 4 : Split the dataset for Training and Testing

    print(Border)
    print("Step 4 : Split the dataset for Training and Testing")
    print(Border)

    X_Train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(Border)
    print("Information of trainig and Testing data")
    print("X_train shape:",X_Train.shape)
    print("X_test shape:",X_Test.shape)
    print("Y_train shape:",Y_Train.shape)
    print("Y_test shape:",Y_Test.shape)
    print(Border)

    #Step 5 : Feature Scaling

    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)

    scalar = StandardScaler()
    #Independent variable Scaling
    X_Train_scaled = scalar.fit_transform(X_Train)
    X_Test_scaled = scalar.fit_transform(X_Test)

    print("Feature scaling is Done")

    #Step 6 : Explore the multiple values of k
    #Hyperparameter Tuning(k)

    accuracy_scores = []
    K_values = range(1,20)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_Train_scaled,Y_Train)
        Y_pred = model.predict(X_Test_scaled)
        accuracy = accuracy_score(Y_Test,Y_pred)
        accuracy_scores.append(accuracy)

    print(Border)
    print("Accuracy report of all K values from 1 to 20")
    for value in accuracy_scores:
        print(value)

    print(Border)

    #Step 7 : Plot graph of K vs Accuracy

    print(Border)
    print("Step 7 : Plot graph of K vs Accuracy")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker = 'o')
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.title("K values vs Accuracy")
    plt.xticks(list(K_values))
    plt.grid()
    #plt.show()

    #Step 8 : Find best value of K

    print(Border)
    print("Step 8 : Find best value of K")
    print(Border)

    best_K = list(K_values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best K value is:",best_K)

    #Step 9 : Build Final model using best value of K

    print(Border)
    print("Step 9 : Build Final model Using best value of K")
    print(Border)

    Final_model = KNeighborsClassifier(n_neighbors=best_K)
    Final_model.fit(X_Train_scaled,Y_Train)
    Y_pred = Final_model.predict(X_Test_scaled)

    #Step 10 : Calculate Final accuracy

    print(Border)
    print("Step 10 : Calculate Final accuracy")
    print(Border)

    accuracy = accuracy_score(Y_Test,Y_pred)
    print("Final Accuracy is:",accuracy)

    #Step 11 : Display Confusion matrix
    print(Border)
    print("Step 11 : Display Confusion matrix")
    print(Border)

    cm = confusion_matrix(Y_Test,Y_pred)
    print(cm)

    #Step 12 : Display Classification report
    print(Border)
    print("Step 11 : Display Classification report")
    print(Border)

    print(classification_report(Y_Test,Y_pred))

def main():
    Border = "-"*40
    print(Border)
    print("Wine classifier using KNN:")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()