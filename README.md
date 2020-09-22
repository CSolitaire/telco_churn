# **Churn Reduction Model Project**
******************************************************************************************************************************************************
## **About the Project**
******************************************************************************************************************************************************
### **Goal**

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

- **Null Hypothesis:** A type of hypothesis used in statistics that proposes that there is no difference between certain characteristics of a population.

- **Alternative Hypothesis:** A type of hypothesis used in hypothesis testing that is contrary to the null hypothesis.

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
- Overall churn rate 26% (over 6 years or 72 months)
- Churn rate > 50% for first 8 months of service
- Monthly churn rate decreases over time (month 1: 47%, month 2: 14%, month 3: 12%......)
- Internet service is large negative and positive driver of churn

### **Hypotheses**
- Hypotheses
    - A. Customers with internet service are more likely to churn 
    - B. Customers with internet service and tech support are less likely to churn

- Statistical Tests:
    - A. Chi Squared Test For Independence - Independence between churn and internet services (DSL and Fiber) among internet subscribers
    - B. Chi Squared Test For Independence - Independence between churn and tech support (no support, online support) among internet subscribers
******************************************************************************************************************************************************
### **Project Plan: Breaking it Down**

#### **acquire.py**
- Data was acquired from MySQL telco_churn database hosted by codeup.com

#### **prepare.py**
 - prep_telco_data_explore (Data used for exploration and hypothesis testing)
   - Delete redundent columns: contract_type_id, internet_service_type_id, payment_type_id  
   - Replace partner, dependents, churn, phone_service, paperless billing, with boolean value
   - Change gender, payment_type, multiple_lines, online_security, online_backkup, device_protection, tech_support, streaming_tv, streaming_movies, contract_type, internet_service_type to categorical category codes
   - Add dummy variables as new columns in dataframe and rename them for payment_type, contract_type, internet_service_type 
   - Create new boolean column for internet_service
   - Change total_charges to a numeric variable
   - Replace 18 NaN values in total_charges with 0, because they represent customers who are new and are yet to have a total_charge
   - Create a new feature called tenure_years
   - Return df

 - prep_telco_data_model (Scaled data used for modeling)
   - prep_telco_data_explore (Data used for exploration and hypothesis testing)
   - Delete redundent columns: contract_type_id, internet_service_type_id, payment_type_id  
   - Replace partner, dependents, churn, phone_service, paperless billing, with boolean value
   - Change gender, payment_type, multiple_lines, online_security, online_backkup, device_protection, tech_support, streaming_tv, streaming_movies, contract_type, internet_service_type to categorical category codes
   - Add dummy variables as new columns in dataframe and rename them for payment_type, contract_type, internet_service_type 
   - Create new boolean column for internet_service
   - Change total_charges to a numeric variable
   - Replace 18 NaN values in total_charges with 0, because they represent customers who are new and are yet to have a total_charge
   - Create a new feature called tenure_years
   - Split data: train, validate, test
   - Scale data
   - Return train, validate, test

#### **Explore**
- Plot correlation matrix of all variables, identify those most highly correlated to churn
- Hypothesis testing and evaluation

#### **Model**
- Try different algorithms: logistic regression, decision tree, random forest, knn
- Which features are most influential?
- Evaluate on train
- Select top 3 models  
- Evaluate on validate
- Select top model
- Evaluate on Test
- Report test results

#### **Conclusion**
- linear regression model returned 79% accuracy on my test data (20% improvement over baseline (50%))
- Best model optimized for validate to reduce type II errors (predict no-churn but churn)
- Recall (51%): Not a great value. It means that when the model predicts a customer will not churn it is only correct 51% of the time
- Precision (63%): Also a great value. It means that when the model predict a customer will churn it is only correct 63% of the time

#### **Next Steps**
- Model needs work
- Need to go back and examine inputs to further optimize for Recall
- Model is better then the dummy but has a lot be desired
******************************************************************************************************************************************************
### **How to Reproduce**
1. Access Codup MySQL database and generate telco_churn data using following:
 sql_query = '''
                select * 
                from customers as c
                join contract_types as ct
                on ct.contract_type_id = c.contract_type_id
                join internet_service_types as i_s
                on i_s.internet_service_type_id = c.internet_service_type_id
                join payment_types as pt
                on pt.payment_type_id = c.payment_type_id;
                '''
2. Execute explore df
   - prep_telco_data_explore()
   - visualize data
   - explore correlations .corr()
   - select model inputs

3. Execute model df
   - prep_telco_data_model()
   - Build and execute logistic regression model
     - log = LogisticRegression(C=1, random_state = 123, solver='lbfgs')
   - Build and execute decision tree model
     - clf = DecisionTreeClassifier(max_depth=10, random_state=123)
   - Build and execute random forrest model
     - rf = RandomForestClassifier(bootstrap=True, 
                            class_weight=None, 
                            criterion='gini',
                            min_samples_leaf=10,
                            n_estimators=100,
                            max_depth=20, 
                            random_state=123)
   - Build and execute knn model
     - knn = KNeighborsClassifier(n_neighbors=5, weights='uniform')
   - Fit and evaluate models on train
     - log.fit(X_train_1, y_train)
     - clf.fit(X_train_2, y_train)
     - rf.fit(X_train_3, y_train)
     - knn.fit(X_train_4, y_train)
   - Choose top 3 preforming models (optimizing recall)
   - validate models on unseen data
     - y_pred_1 = log.predict(X_validate_1)
     - y_pred_2 = clf.predict(X_validate_2)
     - y_pred_4 = knn.predict(X_validate_4)
   - Choose top model (optimizing recall)
   - Evaluate on test
     - y_pred_test = log.predict(X_test)
   - Report findings