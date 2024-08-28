
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split

def train_model(input_file):
    df = pd.read_csv(input_file)
    X = df.drop(columns=['Default'])
    y = df['Default']
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

    model = xgb.XGBClassifier(objective='binary:logistic', eval_metric='logloss')
    model.fit(X_train, y_train, eval_set=[(X_valid, y_valid)], early_stopping_rounds=10)
    model.save_model('xgb_model.json')

if __name__ == "__main__":
    train_model('data/processed_data.csv')
