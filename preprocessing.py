import pandas as pd
from sklearn.utils import resample
from sklearn.preprocessing import MinMaxScaler
import joblib


def fillType(df):
    # Make first row as column labels
    df.rename(columns=df.iloc[0], inplace=True)
    df.drop(df.index[0], inplace=True)

    # Fill empty values
    df['TotalCharges'] = df['TotalCharges'].replace(' ', 0)

    # Change data type to string and number
    df = df.astype('string')
    df['SeniorCitizen'] = df['SeniorCitizen'].astype('int64')
    df['tenure'] = df['tenure'].astype('int64')
    df['MonthlyCharges'] = df['MonthlyCharges'].astype('float')
    df['TotalCharges'] = df['TotalCharges'].astype('float')

    return df


def resampleData(df):
    df["Churn"] = df["Churn"].apply(lambda x: 1 if x == "Yes" else 0)

    df_1 = df[df["Churn"] == 1]

    df_0 = df[df["Churn"] == 0].sample(n=5174, random_state=123)
    df_1_upsample = resample(df_1, n_samples=5174, replace=True, random_state=123)

    df = pd.concat([df_1_upsample, df_0])

    return df


def prepareData(df):
    y = df[["Churn"]]

    # SplitData
    X = df[["SeniorCitizen", "Partner", "Dependents", "tenure", "InternetService", "OnlineSecurity",  "Contract", "PaymentMethod", "MonthlyCharges", "TotalCharges"]]

    # Encoding categorical variables
    X["Partner"] = X["Partner"].apply(lambda x: 1 if x == "Yes" else 0)
    X["Dependents"] = X["Dependents"].apply(lambda x: 1 if x == "Yes" else 0)
    X["InternetService"] = X["InternetService"].apply(lambda x: 1 if x == "Fiber optic" else 0)
    X["OnlineSecurity"] = X["OnlineSecurity"].apply(lambda x: 0 if x == "No" else 1)
    X["Contract"] = X["Contract"].apply(lambda x: 0 if x == "Month-to-month" else 1)
    X["PaymentMethod"] = X["PaymentMethod"].apply(lambda x: 1 if x == "Electronic check" else 0)

    # Feature Scaling
    mms = MinMaxScaler()  # Normalization

    X['tenure'] = mms.fit_transform(X[['tenure']])
    X['MonthlyCharges'] = mms.fit_transform(X[['MonthlyCharges']])
    X['TotalCharges'] = mms.fit_transform(X[['TotalCharges']])

    joblib.dump(mms, "scaler.pkl")

    return X, y
