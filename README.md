# **Churn Reduction Model Project**
******************************************************************************************************************************************************
## **About the Project**
******************************************************************************************************************************************************
### **Goals**

My goal for this project is to produce a model that will predict if a customer will leave Telco.  This model will be trained on 72 months of customer data, looking specifically at contract type, internet service, and tenure as significant drivers of churn. A CSV of individuals likely to churn will be provided at the end of the project.   
******************************************************************************************************************************************************
### **Background**
From http://www.dbmarketing.com/telecom/churnreduction.html, by Authur Hughes

-  As of 9/20/2020 annual churn rates for telecommunications companies average between 10 and 67 percent.

 - Roughly 75 percent of the subscribers signing up with a new carrier every year are coming from another wireless provider and hence are already churners. 

 - Industry retention surveys have shown that while price and product are important, most people leave any service because of dissatisfaction with the way they are treated.
******************************************************************************************************************************************************
### **Acknowledgement**
If you use this dataset in your research, please credit the authors

Codeup - https://codeup.com/
******************************************************************************************************************************************************
## **Data Dictionary**

- **Churn Rate (Churn):** The churn rate, also known as the rate of attrition or customer churn, is the rate at which customers stop doing business with an entity.

- **Heatmap:** A representation of data in the form of a map or diagram in which correlation values are represented as colors.

- **Correlation:** The interdependence of variable quantities.

- **Hypothesis Testing:** An act in statistics whereby an analyst tests an assumption regarding a population parameter.

- **Null Hypothesis $H_{0}$ :** A type of hypothesis used in statistics that proposes that there is no difference between certain characteristics of a population.

- **Alternative Hypothesis $H_{a}$ :** A type of hypothesis used in hypothesis testing that is contrary to the null hypothesis.

- **DSL:** "Digital Subscriber Line" DSL is a communications medium used to transfer digital signals over standard telephone lines.

- **Fiber:** Fiber optic cable is a high-speed data transmission medium. It contains tiny glass or plastic filaments that carry light beams. 

- **Chi Squared Test for Independence:** A statical test that ompares two variables in a contingency table to see if they are related.

- **P-value:** A p value is used in hypothesis testing to help you support or reject the null hypothesis. The p value is the evidence against a null hypothesis. The smaller the p-value, the stronger the evidence that you should reject the null hypothesis.

- **Model Fitting (fit):** A process that involves running an algorithm on data for which the target variable (“labeled” data) is known to produce a machine learning model.

- **Algorithm:** A process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer.   

- **Machine Learning Model:** A machine learning model is a file that has been trained (using an algorithm) to recognize certain types of patterns.

- **Logistic Regression Algorithm:** A classification algorithm, used when the value of the target variable is categorical in nature.

- **Decision Tree Algorithm:** A tree-structured classification algorithm, where internal nodes represent the features of a dataset, branches represent the decision rules and each leaf node represents the outcome.

- **Random Forrest Algorithm:** A classification algorithm consisting of many decisions trees. It uses bagging and feature randomness when building each individual tree to try to create an uncorrelated forest of trees whose prediction by committee is more accurate than that of any individual tree.

- **KNN Algorithm:** A simple, supervised machine learning algorithm that can be used to solve both classification and regression problems.

- **Classification Report:** Used to measure the quality of predictions from a classification algorithm. The report shows the main classification metrics precision, recall and f1-score on a per-class basis.

- **Confusion Matrix:** A table that is often used to describe the performance of a classification model (or "classifier") on a set of test data for which the true values are known.

- **Accuracy:** The ratio of number of correct predictions to the total number of input samples.

- **Precision:** The number of correct positive results divided by the number of positive results predicted by the classifier.

- **Recall:** The number of correct positive results divided by the number of all relevant samples (all samples that should have been identified as positive).

- **f1-score:** The harmonic mean between precision and recall.

- **CSV:** A CSV (comma-separated values) file is a text file that has a specific format which allows data to be saved in a table structured format.

******************************************************************************************************************************************************
## **Initial Thoughs and Hypotheses**
******************************************************************************************************************************************************
### **Thoughts**
- Overall Churn Rate 26% (Over 6 Years or 72 Months)
- Churn Rate > 50% for first 8 months of service
- Monthly Churn Rate Decreases Over Time (Month 1: 47%, Month 2: 14%, Month 3: 12%......)

### **Hypotheses**
- Hypotheses
    - A. Association between internet service type and churn
    - B. Association between lack of tech support and churn

- Statistical Tests:
    - A. Chi Squared Test For Independence - Independence between churn and internet services
    - B. Chi Squared Test For Independence - Independence between churn and tech support
******************************************************************************************************************************************************
### **Project Plan: Breaking it Down**

#### **acquire.py**
 - text

#### **prepare.py**
 - text

#### **Explore**
- text

#### **Model**
- text

#### **Conclusion**
- text
******************************************************************************************************************************************************
### **How to Reproduce**
- text