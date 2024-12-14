import pandas as pd
from sklearn.model_selection import train_test_split


def data_transform(inputdata,outputdata):
    df= pd.read_csv(r"C:\Users\BIG JA\desktop\houseprice\Bengaluru_House_Data.csv")
    df=df.fillna(df.mean())
    X=df.drop(columns=["price"])
    y=df["price"]
    X_train,X_test,y_train,y_test=train_test_split(X,y, test_size = 0.2, random_state=42)
    df.to_csv("C:\Users\BIG JA\desktop\houseprice\edited.csv", index=False)
    print(f"data transformed and saved to {"C:\Users\BIG JA\desktop\houseprice\edited.csv"}")


    return X_train,X_test,y_train,y_test