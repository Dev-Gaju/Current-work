### Workflow Describe

In this notebook, Work with three multivariate time series datasets. One is huge big data, another is Class imbalance data, other one is partially time series data.

**Household Energy consumption** This dataset has `7` column and `2075259` rows with regression of approximately 157Mb tough to handle on my local computer. For the big dataset, I used the memory save method for less memory used. Then Check the Statistics model and fill the missing value with the mean. After that visualized some plots to get an Idea regarding feature engineering. Same way ACF and PCF check relations, Check seasonality, stationary Trends and so on.

**Occupancy Detection** Class Imbalance with time series classification data. It defines people in the room or not. There are several methods to handle class Imbalance but what about Time series data? For Time series data it has a specific library to maintain the sequence which is `SMOTEENN`. Rest of the process same as the previous dataset.

**EEG Eye state** Partially time series data because not mention any time column but have value sequentially. In this dataset have 15 column and `14980` rows with a binary classification dataset. Here time and date not mention but have a sequence. But when I try to predict the future in sequence not work properly then used train_test_split from sklearn to divide data. Used co-relation metrics to identify a relation and another plot.

Now Let's discuss Several models regarding classification and regression models.

**XGBoost** Used Xgboost with three of this dataset & the good news is this model did better all of this dataset. We knew that Xgboost is a supermodel on tabular data but in time series prediction it did a better job.

**SVM** Worked with SVM previously on classification & Regression task but not get a better result in term of accuracy but in the case of time series data get better result than expectation like more than Deep learning models.

Rdge: Lasso and Ridge are two regression models, I used here to predict time series regression but didn't do well.

LSTM: Long Sort Term Memory is shortly known as LSTM. It is a family member of RNN and has an extension of RNN. Basically, we know the problem about vanishing gradient descent in long sequences to overcome this LSTM come to work with text data. having Three get and more memory is best with large amounts of data. Applied LSTM with three datasets and get better results among two.

GRU: Gated Recurrent Unit shortly known as GRU, Works with sequence data. Which take input sequentially. Instead of three terms GPU used update and reset. Need less memory for fewer parameters and work better with small data. Applied three datasets and get better accuracy with two and less on one dataset.



**Rsult:** All the result are bellow from this task. For Eye-State Dataset.
| Model| MAE |ACC|
| -----| -----|---|
|XGboost|0.149|0.9423|
|SVC|-|0.874|
|LSTM|1.09|0.469|
|GRU|0.69|0.530|
              
              
Now household electric ower consumption, Regression model
| Model| R2_score |MAE|
| ----- | ----- |-----|
|XGboost|0.999|0.010|
|Auto_Reg|check|graph|
|LSTM|-|0.166|
|GRU|-|0.0832|
|Lasso|-|0.6425|
                

Occapancy & Detection result classification
| Model| MAE |ACC
| ----- | ----- |-----|
|XGboost|-|0.999|
|LSTM|0.27|0.9444|
|GRU|0.69|0.953|


**Conclusion:** Working with Time series is much critical and hard coz it works like real time data. Tabular data means feature engineering and selection but while working with time series data it more critical coz finding feature is more challenging. Face several challenge and some of them are overcome and some are still finding solution. Vast amount of knowledge gain and Update this repository while get better idea.



