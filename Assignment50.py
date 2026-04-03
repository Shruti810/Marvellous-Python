import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

def Logisticregression(Datapath):

#Step 1: Load the Dataset

    df = pd.read_csv(Datapath)
    print("Few entries of Dataset:")
    print(df.head())

#Step 2 : Clean the Dataset by removing empty rows

    df.dropna(inplace=True)
    print("Total Rows:",df.shape[0])
    print("Total Columns:",df.shape[1])

#Step 3 : Seperate Independent and Dependent variables

    X = df.drop(columns=['y'])
    Y = df['y']

    print("Shape of Independent Variable:",X.shape)
    print("Shape of Dependent Variable:",Y.shape)








def main():
    Logisticregression("bank-full.csv")
    
if __name__ == '__main__':
    main()