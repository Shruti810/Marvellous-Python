import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn.ensemble import VotingClassifier

def FakeTrueDataset(FakeDataset,TrueDataset):

    #Step 1 : Load the Dataset

    df_Fake = pd.read_csv(FakeDataset)
    df_True = pd.read_csv(TrueDataset)

    df_Fake['label'] = 0
    df_True['label'] = 1

    df = pd.concat([df_Fake,df_True], axis=0)

    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    print("Some sample values:",df.head())
    print("Size of Dataset:",df.shape)

    #Step 2 : Drop null values and Select useful columns

    df.dropna(inplace=True)
    print("Total Rows:",df.shape[0])
    print("Total Columns:",df.shape[1])

    #Step 3 : Use TF-IDF Vectorization to convert text into numerical features

    X_text = (
    df.drop(columns=['label'])
      .fillna('')                      # handle missing values
      .astype(str)
      .apply(lambda row: ' '.join(row)[:300], axis=1)   # combines all column values of each row into one single string            
    )

    tfidf = TfidfVectorizer(stop_words='english',max_features=200,max_df=0.5,min_df=10)

    X = tfidf.fit_transform(X_text)
    Y = df['label']

    print("Some elements of Independent Variable:")
    print(X)
    print("Some elements of Dependent Variable:")
    print(Y.head())

    #Step 4 : Train Models Logistic Regression and Decision Tree Classifier

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    Dtmodel = DecisionTreeClassifier(max_depth=3,random_state=42)
    Lrmodel = LogisticRegression(max_iter=1000)

    Dtmodel.fit(X_train,Y_train)
    DTY_pred = Dtmodel.predict(X_test)
    accuracy = accuracy_score(Y_test,DTY_pred)

    print("Accuracy of Decision Tree model is:",accuracy)

    Lrmodel.fit(X_train,Y_train)
    LrY_pred = Lrmodel.predict(X_test)
    Lraccuracy = accuracy_score(Y_test,LrY_pred)

    print("Accuracy of Logistic Regression model is:",Lraccuracy)

    #Step 5 : Soft Voting Classification

    soft_model = VotingClassifier(
    estimators=[
        ('lr',Lrmodel),     # 'lr','dt','knn' - is a keyword
        ('dt',Dtmodel)
    ],
    voting='soft'
    )

    soft_model.fit(X_train,Y_train)

    pred_soft = soft_model.predict(X_test)
    acc_soft = accuracy_score(pred_soft,Y_test)

    print("Soft Voting accuracy:",acc_soft)
    
    #Step 6 : Hard Voting Classification

    hard_model = VotingClassifier(
        estimators=[
            ('lr',Lrmodel),
            ('dt',Dtmodel)
        ],
        voting='hard'
    )
    
    hard_model.fit(X_train,Y_train)

    pred_hard = hard_model.predict(X_test)
    acc_hard = accuracy_score(pred_hard,Y_test)

    print("Hard Voting accuracy:",acc_hard)

    #Step 7 : Confusion Matrice

    cm_soft = confusion_matrix(Y_test,pred_soft)
    cm_hard = confusion_matrix(Y_test,pred_hard)

    print("Hard Voting Confusion Matrix:")
    print(cm_soft)
    print("Soft Voting Confusion Matrix:")
    print(cm_hard)

def main():
    FakeTrueDataset("Fake.csv","True.csv")

if __name__ == '__main__':
    main()
