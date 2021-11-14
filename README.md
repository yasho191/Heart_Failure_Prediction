# Heart_Failure_Prediction

## Research paper link:
https://ieeexplore.ieee.org/document/9587466

## Abstarct of the work done:
The research aims on prediction of a heart failure using different machine learning algorithms and hybrid fusion techniques like majority voting of the best performing classifiers. This paper focuses on a majority based algorithm which uses the 3 best performing machine learning models out of the 10 selected machine learning models such as Logistic Regression, Decision Tree, Random Forest, Bagging Classifier, Gradient Boosting Classifier, Extreme Gradient Boosting Classifier, Extreme Gradient Boosting Random Forest, Extra Trees, Categorical Boosting Classifier and K-Nearest Neighbours. The top 3 classifiers are selected on the basis of their accuracy, f1-score and training time required. The minimum accuracy and F1-score score threshold is set to 90% so as to achieve better real world performance of the algorithm in terms of the ability to produce higher accuracy as well as the low time complexity. The proposed model combined the 3 best performing models using the voting method which yielded an Accuracy of 96.67%, a F1-Score of 95.24% and an AUC Score of 95% on the used data set.

## Dataset : 
https://archive.ics.uci.edu/ml/datasets/Heart+failure+clinical+records

The dataset has been taken from the UCI data repository.

## Aim :
- Develop a robust hybrid machine learning algorithm for prediction of heart failure in a patient so that the patient can keep a track of his/her heart conditions and take the right precautions.
- To read the complete notebook along with all the visulizations please download the files.


# Problem Description

To create a model in order to predict the likelihood of a patient dying due to heart failure.
This a binary clasification problem since the target class (Death Event) consists of two classes True or False

# About the Dataset
Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worlwide.
Heart failure is a common event caused by CVDs and this dataset contains 12 features that can be used to predict mortality by heart failure.

Most cardiovascular diseases can be prevented by addressing behavioural risk factors such as tobacco use, unhealthy diet and obesity, physical inactivity and harmful use of alcohol using population-wide strategies.

People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.

# Feature description

1. Age: age of patient (in years)
2. Anaemia: Decrease of red blood cells or hemoglobin
3. High blood pressure: If a patient has hypertension
4. Creatinine phosphokinase: Level of the CPK enzyme in the blood (mcg/L)
5. Diabetes: If the patient has diabetes
6. Ejection fraction: Percentage of blood leaving the heart at each contraction
7. Sex: Woman or man
8. Platelets: Platelets in the blood (kiloplatelets/mL)
9. Serum creatinine: Level of creatinine in the blood (mg/dL)
10. Serum sodium: Level of sodium in the blood (mEq/L)
11. Smoking: If the patient smokes
12. Time: Follow-up period (in days)
13. (target) death event: If the patient died during the follow-up period
