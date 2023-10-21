### Workflow if California House Prices Dataset

This notebook contain the code of mention dataset. Basically this is Regression Dataset, Regression define output as contious way. From EDA to Feature Engineering & Model building everything have done in this notebook. 

#### Dataset :
This dataset have 20640 row and 10 column. Among 10 column all are numerical except `ocean_proximity` which is a categorical column & have 5 properties.

#### EDA
In this Section, Try to play data on various way and visualized. First check the missing values and have some which fillup with mode value of these column. Then try to do several plot like scatter plot between two variable to find their linear relarionship then KDE plot to find the nature of each column. After all that apply pairplot to identified relationship to the regressor or our main value which is `median_house_value`. Then look at the correlation matrix to find strogly positively corelated or negetively corelated column. After all the technique have to check outlier present or Not. If present then try to handle those by using `zscore`. After all that EDA convert categorical column into numerical and did a llittle bit feature Engineering.

#### Supervised Regression Algorithm:

**Metrics:** I used R-squaed metrics for determine the model performance. R_sqaued is a known of co-efficient of determination is a terms that used to identified the fitted score on Regression model.A score is close to 0 mean model not well and a score is close to 1 means model fitted very well, sometimes score close to 1 can't be very good or overfiting score if the model is complex and data have noise.
 
 **Linear Regression :** We all know about this Linear Model which have a classification model also. In this notebook I used simple linear regression model & got `0.668` r2_squared value.
 
 **SVM :** In SVM or SVR regressor model I used simple version with `rbf` kernel but standardScaller used in dataset section which give better r2_squared score `0.74526` than Linear Regression.
 
 **KNN :** In this model which have given worse r2_squared value `0.2185218`, In documantation said KNN is polpular on classification task not do very well on regression. KNN also highly sensetive on noise and outlier of the data also not work on high dimension space.
 
**Decision Tree :** This model works better than the other two model like Linear regression & KNN. This model produce `0.67914` r_sqaured score which is better.In this model I checked the importance feature using its default method.

**Adaboost:** Adaboost not done so well as I expected as a boosting algorithm. It have score `0.540818` which is less than Decision tree and Linear Regression.

**MLP :** Multi Layer Perceptron is a type of atrificial neural networks that consist interconnection on Multiple layer. If a feedforward neural network which means data flow in one direction without any cycle or feedback loops.

**XGBOOST** Best score achiever in this dataset, without any parameter tuning it achieved `0.854657`. Xgboost is a gradient boosting algorithm which works on gradually build weak learners and combines their prediction to make strong learning which we can call also ensemble learning. After using parameter tuning on optuna it gives better score than the normal one.


#### Result
There are several kind of model in Machine Learning sector, difference model have difference working way and in this dataset if we think without boosting model then it was the best for given such a brillaint score than others. But when we go one steps further then got better we can say best score which is `0.865234`. So for this dataset Xgboost with parameter tuning on Optuna is the winner.


#### Conclusion

Regression Terms is a popular section on machine learning, I aplied several model and did several EDA and feature engineering to achieve better score. Using Optuna on parameter tuning have faced several problems this xgboost not work well good with all parameters. In the further section there is a more scope to improve the score by using difference model like `hill-climbing` or `LGBM` or do some better feature engineering.
