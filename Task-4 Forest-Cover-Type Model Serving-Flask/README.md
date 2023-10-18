#### Model Serving

In this repositoy, I did model serving with flask. There Types of Model chosen for this dataset. Best classifier, Second best and ensemble classifier. Ensemble give the better result among those. Basically, Ensemble is combination of four model random Forest, MLP, XgBoost, LightGBM. LightGBM have is the best single model and random forest second as well. Accuracy for those model is `0.897`, `0.9077` and `0.9166` random forest, LightGBM and Blending perpectively. 

In this model serving repository, predict three different result with same type of data.Used pickle to save and load model. In serving section used feature engineering technique and data pre-processing. Design a single html paage for taking user input and sending feedback from server. To featching input from user point used javascript with json formate.Then convert values as comma separated way. 

So after feature engineering and pre-processing, Now its prediction time. For prediction Single model used as usual way but when work with ensemble learning or blendinig all the model relative blending have to impoert then prediction with meta_model.

Prediction send to the index file from python script with post method. Then catch it with jquery and visualized with html section. Note that before sending convert data into json formate. 

In the end, very interesting repository and learn a lot from this work. Faced issues on differenc section & solve by walking on google.