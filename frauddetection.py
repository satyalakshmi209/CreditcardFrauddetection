# -*- coding: utf-8 -*-
"""frauddetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UzuA2Z3AEt5H3mdZVoH4WhT167bWCThu
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv('/content/creditcard.csv')  # Replace with your actual file path

print(df.head())
print(df.info())

print(df.isnull().sum())

import matplotlib.pyplot as plt
import seaborn as sns

# Distribution of target variable
plt.figure(figsize=(6, 4))
sns.countplot(x='Class', data=df)
plt.title('Distribution of Target Variable (Class)')
plt.show()

scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df.drop(['Time', 'Amount', 'Class'], axis=1)), columns=df.columns[1:-2])

# Adding back the 'Time', 'Amount', and 'Class' columns
df_scaled['Time'] = df['Time']
df_scaled['Amount'] = df['Amount']
df_scaled['Class'] = df['Class']

# Correlation matrix
corr_matrix = df.corr()

# Plotting the correlation matrix
plt.figure(figsize=(20, 15))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Correlation with target variable
corr_with_target = corr_matrix['Class'].sort_values(ascending=False)
print(corr_with_target)

X = df_scaled.drop('Class', axis=1)
y = df_scaled['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

lr_classifier = LogisticRegression(random_state=42)
lr_classifier.fit(X_train, y_train)

y_pred = lr_classifier.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d")
plt.show()

# Classification Report
print(classification_report(y_test, y_pred))

# Accuracy Score
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")