### WorkFlow for Forest Cover-Type Prediction
This notebook describe the dataset with classification technique and apply several model.First did EDA & pre-processing then Feature Engineering then execute several algorithms. Here Introduce two new terms from ensemble learning `Blending & VottingClassifiers`.

**Dataset**
Surprisingly the test portion of this dataset is much bigger than train size. In trining portion there is 15120 rows and 55 columns & all are numerical where test size is 565892.

**EDA**
As usual load dataset, While loading dataset if I load train test dataset together then do all other stuff then my notebook show me the `running out of memory`. No missing value in the dataset. Checking the each class distribution & also each column distribution with scatter plot. Try to find out relatiosnship between colmuns. Here used violin plot to check outliers and solve with zscore

**Normalized vs MinMaxScaler**: Both brings data to the range of 0-1. But handle differently, Normalizer can reduce outliers better than MinMax, MinMax works between Column but Normalizer works on row.

Each & every algorithm here I used with two types of dataset. One is just apply remove after the outliers & another way is feature engineering.

**Linear Classification** Logistic regression basically works better on binary data, faced many dependencies on multiclass classification.its did good on feature enginnering portion rather the removing outliers `0.71759` & `0.677647`.

**SVM :** SVM cannot support multiclass classification natively & works better on binary classification and small dataset. So in multiclass classification same execuation is applicable, it break data from multi-class problem to multi-binary problems.

**KNN :** Main advantage of using KNN is it support multiclass classification. Basically it do better on multiclass classification and achieve better score. this model did well on this dataset too `76025` achived.

**Decsion Tree** More important of this model is, its work better on both side data. 

**AdaBoost** In the terms of adaboost it made for binary classification but in the case of multiclass classification it work better on variation of data. In this dataset it works very bad which is `0.5145`. 

**Random Forest** My second best model in this dataset which also boost the accuracy on blending.

**MLP** This algorithm varied on difference sector to works, Sometimes did better on simple dataset & not do well on complex dataset. For this dataset it works prety well and given decent acuracy which is 
`0.84093`

**LightGBM** The winner of this dataset. It work best with Parameter tuning with Optuna and feature engineerng `0.905092`.

**Result**
Worked difference types of model and from the uppor portion we know that every model have difference dependencies and difference working formula. So in this dataset work good on LightGBM and bad with Adaboost. More interesting thing is LightGBM works better than Voting but not blending. How our blending accuracy is `0.90806`

**Motivation**
In tabular classification problem main part is feature engineering. If anyone can findout better feature then a simple model can be the game changer. Did feature engineering but this dataset is very tricky and tried to do well.Try to solve the skewness and apply Pseudo-labeling. Will check apply one or two more model in the blending section then differenciate the accuracy.
