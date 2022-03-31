# import lib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset w/ pandas library
df = pd.read_csv("dataset_titanic.csv")
print(df.shape)
print(df.head())

df.drop(columns=['Passengerid', 'Fare', 'zero', 'zero.1',
                 'zero.2', 'zero.3', 'zero.4', 'zero.5', 'zero.6',
                 'Parch', 'zero.7', 'zero.8', 'zero.9', 'zero.10', 'zero.11',
                 'zero.12', 'zero.13', 'zero.14', 'zero.15', 'zero.16',
                 'Embarked', 'zero.17', 'zero.18'], inplace=True)
print(df.shape)

df.dropna(inplace=True)
print('after drop missing value :', df.columns)

sns.barplot(x="Sex", y="2urvived", data=df, ci=None)
sns.barplot(x="Pclass", y="2urvived", data=df, ci=None)
plt.show()
