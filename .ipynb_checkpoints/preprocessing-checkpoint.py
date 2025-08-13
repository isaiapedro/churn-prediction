import pandas as pd
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from scipy.signal import butter, filtfilt

def fillType(df):

    # Make first row as colum labels
    df.rename(columns=df.iloc[0], inplace = True)
    df.drop(df.index[0], inplace = True)

    # Drop missing values
    df['InternetService'] = df['InternetService'].fillna("None")

    df['CustomerID'] = df['CustomerID'].astype(str).astype(int)
    df['Age'] = df['Age'].astype(str).astype(int)
    df['Gender'] = df['Gender'].astype(str)
    df['Tenure'] = df['Tenure'].astype(str).astype(int)
    df['MonthlyCharges'] = df['MonthlyCharges'].astype(str).astype(float)
    df['ContractType'] = df['ContractType'].astype(str)
    df['InternetService'] = df['InternetService'].astype(str)
    df['TotalCharges'] = df['TotalCharges'].astype(str).astype(float)
    df['TechSupport'] = df['TechSupport'].astype(str)
    df['Churn'] = df['Churn'].astype(str)
    
    return df

def prepareData(df):
    #Churn
    y = df[["Churn"]]
    y["Churn"] = y["Churn"].apply(lambda x: 1 if x == "Yes" else 0)

    #SplitData
    X = df[["Age", "Gender", "Tenure", "MonthlyCharges","ContractType","InternetService","TechSupport"]]

    #Age
    X.loc[X['Age'] <= 36, 'Age'] = 0
    X.loc[(X['Age'] > 36) & (X['Age'] <= 42), 'Age'] = 1
    X.loc[(X['Age'] > 42) & (X['Age'] <= 47), 'Age'] = 2
    X.loc[(X['Age'] > 47) & (X['Age'] <= 53), 'Age'] = 3
    X.loc[(X['Age'] > 53), 'Age'] = 4

    #Gender
    X["Gender"] = X["Gender"].apply(lambda x: 1 if x == "Female" else 0)
    
    #Tenure
    X.loc[X['Tenure'] <= 13, 'Tenure'] = 0
    X.loc[(X['Tenure'] > 13), 'Tenure'] = 1
    
    #MonthlyCharges
    X.loc[X['MonthlyCharges'] <= 60, 'MonthlyCharges'] = 0
    X.loc[(X['MonthlyCharges'] > 60) & (X['MonthlyCharges'] <= 90), 'MonthlyCharges'] = 1
    X.loc[(X['MonthlyCharges'] > 90), 'MonthlyCharges'] = 2

    X['MonthlyCharges'] = X['MonthlyCharges'].astype(int)

    #ContractType
    X["ContractType"] = X["ContractType"].apply(lambda x: 0 if x == "Month-to-Month" else 1)
    
    #InternetService
    X["InternetService"] = X["InternetService"].apply(lambda x: 0 if x == "None" else 1)

    #TechSupport
    X["TechSupport"] = X["TechSupport"].apply(lambda x: 0 if x == "No" else 1)
    
    return X, y

    
def resampleData(df):

    df_0 = df[df["Churn"] == 0]

    df_0_upsample = resample(df_1, n_samples = 883, replace = True, random_state = 123)
    df_1 = df[df["Churn"]==1].sample(n =883, random_state=123)

    df = pd.concat([df_1, df_0_upsample])
    
    return df

def preprocessData(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandarScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    return X_train, X_test, y_train, y_test