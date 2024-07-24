# Stroke-prediction-

# Overview
This project is aimed at predicting the risk of stroke using a dataset containing various health and demographic attributes. The dataset provides information such as age, gender, hypertension, heart disease, marital status, work type, residence type, average glucose level, BMI, and smoking status. These features are used to build predictive models to determine the likelihood of a stroke.

# Dataset
The dataset includes the following columns:

id: Unique identifier for each entry
gender: Gender of the individual
age: Age of the individual
hypertension: 0 if the individual does not have hypertension, 1 if they do
heart_disease: 0 if the individual does not have heart disease, 1 if they do
ever_married: "Yes" or "No" indicating marital status
work_type: Type of occupation
Residence_type: "Urban" or "Rural"
avg_glucose_level: Average glucose level in the blood
bmi: Body Mass Index
smoking_status: Smoking status of the individual
stroke: 1 if the individual has had a stroke, 0 otherwise
Machine Learning Models and Performance
The following machine learning models were used to predict stroke risk:

# Models used
SVM	
KNN	
Random Forest	
Logistic Regression	
AdaBoost	
Gaussian Naive Bayes	
MLP	

# Best Model
The AdaBoost model achieved the highest performance metrics. This model is identified as the most suitable for predicting strokes in this dataset.

# Conclusion
This project demonstrates the application of various machine learning algorithms to predict stroke risk using demographic and health data. The results highlight the potential of AdaBoost in medical predictions, aiding in early detection and preventive healthcare strategies.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
