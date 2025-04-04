# -*- coding: utf-8 -*-
"""Stroke_Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jikvT4bio4oBlrYwVgOnmKMXYxoVW7IX
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score,classification_report,precision_score,recall_score
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

data=pd.read_csv('healthcare-dataset-stroke-data.csv')
data.head(10)
## Displaying top 10 rows
data.info()
## Showing information about datase
data.describe()
## Showing data's statistical features

data.drop("id",inplace=True,axis=1)

cols=data.select_dtypes(include=['object']).columns
print(cols)
# This code will fetech columns whose data type is object.
le=LabelEncoder()
# Initializing our Label Encoder object
data[cols]=data[cols].apply(le.fit_transform)
# Transfering categorical data into numeric
print(data.head(10))

#correlation
plt.figure(figsize=(15,10))
sns.heatmap(data.corr(),annot=True,fmt='.2')

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(axis=1)
    return df[indices_to_keep].astype(np.float64)
clean_dataset(data)

classifier = SelectKBest(score_func=f_classif,k=5)
fits = classifier.fit(data.drop('stroke',axis=1),data['stroke'])
x=pd.DataFrame(fits.scores_)
columns = pd.DataFrame(data.drop('stroke',axis=1).columns)
fscores = pd.concat([columns,x],axis=1)
fscores.columns = ['Attribute','Score']
fscores.sort_values(by='Score',ascending=False)
cols=fscores[fscores['Score']>50]['Attribute']
print(cols)

X_train,X_test,Y_train,Y_test=train_test_split(data[cols],data['stroke'],random_state=1255,test_size=0.25)
#Splitting data
X_train.shape,X_test.shape,Y_train.shape,Y_test.shape

#Balancing Dataset
smote=SMOTE()
X_train,Y_train=smote.fit_resample(X_train,Y_train)
X_test,Y_test=smote.fit_resample(X_test,Y_test)
print(X_train.shape,X_test.shape,Y_train.shape,Y_test.shape)

"""### Random Forest classifier"""

# Fit (train) the Random Forest classifier
ranfor_clf = RandomForestClassifier()
ranfor_model = ranfor_clf.fit(X_train, Y_train)
Y_rfc = ranfor_clf.predict(X_test)

# Display the Confusion Matrix and Classification Report
print(confusion_matrix(Y_rfc, Y_test))
print(classification_report(Y_rfc, Y_test))
print("Accuracy {0:.2f}%".format(100*accuracy_score(Y_rfc, Y_test)))
cm_display = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(Y_rfc, Y_test),
                                    display_labels=[False, True])

# Plot the confusion matrix

cm_display.plot()
plt.show()

"""Support Vector Machine classifier"""

# Fit (train) the Support Vector Machine classifier
svm_clf = SVC()
svm_model = svm_clf.fit(X_train, Y_train)
Y_svm = svm_clf.predict(X_test)

# Display the Confusion Matrix and Classification Report
print(confusion_matrix(Y_svm, Y_test))
print(classification_report(Y_svm, Y_test))
print("Accuracy {0:.2f}%".format(100*accuracy_score(Y_svm, Y_test)))
cm_display = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(Y_svm, Y_test),
                                    display_labels=[False, True])

# Plot the confusion matrix
cm_display.plot()
plt.show()

"""KNN classifier"""

from sklearn.neighbors import KNeighborsClassifier
# Fit (train) the KNN classifier
knn_clf = KNeighborsClassifier()
knn_model = knn_clf.fit(X_train, Y_train)
Y_knn = knn_clf.predict(X_test)

# Display the Confusion Matrix and Classification Report
print(confusion_matrix(Y_knn, Y_test))
print(classification_report(Y_knn, Y_test))
print("Accuracy {0:.2f}%".format(100*accuracy_score(Y_knn, Y_test)))
cm_display = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(Y_knn, Y_test),
                                    display_labels=[False, True])

# Plot the confusion matrix
cm_display.plot()
plt.show()

"""Logistic Regression classifier"""



# Fit (train) the Logistic Regression classifier
logreg_clf = LogisticRegression()
logreg_model = logreg_clf.fit(X_train, Y_train)
Y_lrc = logreg_clf.predict(X_test)

# Display the Confusion Matrix and Classification Report
print(confusion_matrix(Y_lrc, Y_test))
print(classification_report(Y_lrc, Y_test))
print("Accuracy {0:.2f}%".format(100*accuracy_score(Y_lrc, Y_test)))
cm_display = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(Y_lrc, Y_test),
                                    display_labels=[False, True])

# Plot the confusion matrix
cm_display.plot()
plt.show()

"""**Gaussian Naive Bayes model**"""

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train,Y_train)
Y_gnb = gnb.predict(X_test)
accuracy = accuracy_score(Y_test, Y_gnb)
precision = precision_score(Y_test, Y_gnb)
recall = recall_score(Y_test, Y_gnb)
f1 = f1_score(Y_test, Y_gnb)
conf_matrix = confusion_matrix(Y_test, Y_gnb)
print(f'Accuracy: {accuracy:.4f}')
print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(f'F1 Score: {f1:.4f}')
print('Confusion Matrix:')
print(conf_matrix)
print(classification_report(Y_gnb, Y_test))
cm_display = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(Y_gnb, Y_test),
                                    display_labels=[False, True])

# Plot the confusion matrix
cm_display.plot()
plt.show()

"""**ADA BOOST**"""

from sklearn.ensemble import AdaBoostClassifier
adaboost_model = AdaBoostClassifier(n_estimators=10000, random_state=42)

# Train the model
adaboost_model.fit(X_train, Y_train)

# Predict on the test set
Y_ada = adaboost_model.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(Y_test, Y_ada)
precision = precision_score(Y_test, Y_ada)
recall = recall_score(Y_test, Y_ada)
f1 = f1_score(Y_test, Y_ada)
conf_matrix = confusion_matrix(Y_test, Y_ada)

# Print the results
print(f'Accuracy: {accuracy:.4f}')
print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(f'F1 Score: {f1:.4f}')
print('Confusion Matrix:')
print(conf_matrix)
print(classification_report(Y_ada, Y_test))
cm_display = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(Y_ada, Y_test),
                                    display_labels=[False, True])

# Plot the confusion matrix
cm_display.plot()
plt.show()

"""**MLP**"""

from sklearn.neural_network import MLPClassifier
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create an MLP model
mlp_model = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)

# Train the model
mlp_model.fit(X_train, Y_train)

# Predict on the test set
Y_mlp = mlp_model.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(Y_test, Y_mlp)
precision = precision_score(Y_test, Y_mlp)
recall = recall_score(Y_test, Y_mlp)
f1 = f1_score(Y_test, Y_mlp)
conf_matrix = confusion_matrix(Y_test, Y_mlp)

# Print the results
print(f'Accuracy: {accuracy:.4f}')
print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(f'F1 Score: {f1:.4f}')
print('Confusion Matrix:')
print(conf_matrix)
print(classification_report(Y_mlp, Y_test))
cm_display = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(Y_mlp, Y_test),
                                    display_labels=[False, True])

# Plot the confusion matrix
cm_display.plot()
plt.show()

models = ['SVM', 'KNN', 'Random Forest','Logistic Regression','ADA Boost','Gaussian Naive Base','MLP']
accuracies = [accuracy_score(Y_test, Y_svm), accuracy_score(Y_test, Y_knn), accuracy_score(Y_test, Y_rfc),accuracy_score(Y_test, Y_lrc)
,accuracy_score(Y_test,Y_ada),accuracy_score(Y_test, Y_gnb),accuracy_score(Y_test, Y_mlp)]
precisions = [precision_score(Y_test, Y_svm), precision_score(Y_test, Y_knn), precision_score(Y_test, Y_rfc),precision_score(Y_test, Y_lrc)
,precision_score(Y_test, Y_ada),precision_score(Y_test, Y_gnb),precision_score(Y_test, Y_mlp)]
recalls = [recall_score(Y_test, Y_svm),recall_score(Y_test, Y_knn), recall_score(Y_test, Y_rfc),recall_score(Y_test, Y_lrc)
,recall_score(Y_test, Y_ada),recall_score(Y_test, Y_gnb),recall_score(Y_test, Y_mlp)]
f1_scores = [f1_score(Y_test, Y_svm),f1_score(Y_test, Y_knn), f1_score(Y_test, Y_rfc),f1_score(Y_test, Y_lrc)
,f1_score(Y_test, Y_ada),f1_score(Y_test, Y_gnb),f1_score(Y_test, Y_mlp)]

# Create a DataFrame for visualization
results_df = pd.DataFrame({'Model': models, 'Accuracy': accuracies, 'Precision': precisions, 'Recall': recalls, 'F1 Score': f1_scores})

# Visualize the results
plt.figure(figsize=(25, 6))
sns.barplot(x='Model', y='Accuracy', data=results_df, palette='viridis')
plt.title('Model Comparison: Accuracy on Stroke Dataset')
plt.ylim([0, 1])
plt.show()

print(results_df)

