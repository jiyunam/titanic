import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Load dataset
train_set = pd.read_csv('dataset/train.csv')

## Data visualization
train_describe = train_set.describe().to_excel('Train Dataset Breakdown.xlsx')

categorical_cols = ['Survived', 'Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']
ncols = 3
nrows = int(np.ceil(len(categorical_cols)/ncols))

fig, axes = plt.subplots(nrows,ncols, figsize = (14,10))

for idx, categorical_col in enumerate(categorical_cols):
    col_idx = idx//nrows
    row_idx = idx%nrows
    train_set[categorical_col].value_counts().plot.pie(ax=axes[row_idx,col_idx], title=categorical_col)

fig.savefig("Categorical Data.png")

