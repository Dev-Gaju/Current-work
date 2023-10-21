### Workflow for Time series Analysis[Univariate]

In this task work with Time series data. Time series data learn from past data and predict future. Time series data basically have two category univariate and multivariate. Its have difference techniue to split dataset to train and test. Worked with two dataset one is monthly sunspots and another is daily temperature.


#### EDA

- **Time dependency** : Univariate time series order chronologically & value of each time point influence by previous observation.

- **Trend** : Trend measure the long term data movement or pattern over the time. Basically used to check increased or decreased in a certain pattern. It can be linear or exponenial or any other complex pattern.

- **Seasonality** Calculate the repeating pattern in regular time intervel, Suppose sales can be increase in every holidy.

- **Stationarity** Essential Properties of time series data. A time series data is called statitionary if stationary properties such as mean, variance and auto-corelation remain same over time. No stationary data more challenging to manage.

- **Autocorrelation**: Measured degree of similarity between observation over time period regardless of the influence of other lags. Positive auto-corelation means have positive relation with past value negetive means have relation with past in reverse ways.

- **lags** define number of time period or represent the temporal distance between current and past observation. lags basically time intervel between season.

- **Partial Autocorrelation**: Partial autocorrelation measures the correlation between a time series observation and its lagged values after removing the effects of the `intermediate lags`.

- **Correlation & Causation** Two essetial part in statistics. Corelation can be define between two variable or multiple. Values are correlated means if one varible increase other varible also increase, change together.Causation, on the other hand, refers to a cause-and-effect relationship between two or more variables.When one variable causes a change in another variable, there is a causal relationship between them.

####  Analyzing and Modeling

- **Smoothing Techniques** : Techniques like moving averages and exponential smoothing can help remove noise and highlight underlying trends in the time series.

- **AR** : Basically a model with predict future from it past value. From ARIMA model it depend the value p to predict future.
 
- **MA** Moving average is a simple model of time series which predict future from past errors. It calculate using ARIMA model & parameter will be q.

- **ARMA** ARMA model is the combination of both model. It works with previous value and previous error. It gives better result than previous two. 

- **ARIMA** : Have three Part Auto-regression, Integreated and Moving Average.Both ARIMA and ARMA are same but slightly difference. Like Non-stationary time series converting into stationary time series.Here used d parameter to differenting between Starionary vs Non Stationary.

#### Result
In this time series work, used two univariate dataset to predict future. In Temperature dataset apply four model AR, MA, ARMA, ARIMA. Between this four model ARMA have the less amount of MAE `1.7319` & AR have maximum MAE which is `3.858`.

More Important part is This four model work far better in Temperature dataset then Sunspots dataset.In sunsposts dataset max model mae is `47.8061` which comes from agian AR and best model mae is `13.3607`. So ARMA is winner in both dataset.

#### Conclusion: 
Task was very interesting and engaging, Learns a lot of thing from this one, like seasonality, trend, stationary and other things. Also apply difference model to the those dataset and parameter tuning.Also face some dificulties like fit data on model and predction result from dataset plot.