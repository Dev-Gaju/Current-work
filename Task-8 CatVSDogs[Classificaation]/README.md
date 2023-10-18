#### WorkFlow

In this task, Done Image classification is a tricky way. Already told you about the dataset creation in the previous task so in this task do classification on that dataset. Used Keras pipeline from tensorflow and apply several pre-trained models with and without weights and save the model after completing each epoch on google drive and google cloud bucket.


##### EDA

In this portion, create an image directory for train and testing and some Image augmentation with ImageGenerator like shear_range, zoom_range also different flips. Then convert the dataset with train validation and test. Already mentioned that there is no data for validation that's why take validation data from the training portion and used flow_from_directory to create dataset. 

Before creating a dataset for the model check the image shapes and those that are not the same to each other. Try to make an aspect ratio and find the perfect target size but didn't get on that. Utilized batch size with selecting model and image shape also.

##### Models

-InceptionV3: This model used factorization and parallel convolution. Apply InceptionV3 with random weights not imageNet and the image shape was 224,224. For the random  weight initializer, we have to do a trainable layer false for model betterment.

- EfficientNetV2-B2: Used more wider and deeper model than efficient v1. Used this model with pre-trained weight to check if the model classified our truly unseen dataset from the test dog version. This model used only 15 epoch basically I trained those model on Google Colab which have a very limited GPU.


Customs Model: Create a Customs Model on Keras with difference types of filters. Used dropout for not do overfitting on both side convolution and also dense. After training this model on 20 epoch getting training_acc was .8628 and validation was .8733 and also loss of 0.3292 and .3030 respectively. But very bad accuracy on unseen dog test data.

#### Customs Callback Function:
Apply a single customs callback function to save output on the Drive and google cloud bucket Using the Callback method from Callback. Also used a learning rate scheduler and early stopping.
Result: This result will represent the loss of accuracy on the test set coz already mentioned above about the training and validation accuracy with loss.

| Model| Accuracy |loss|
| ----- | ----- |-----|
|InceptionV3|0.90680|0.223|
|EfficinetNetV2-B2|0.730135|0.4853|
|Customs|0.7392|0.6346|


Conclusion: Interesting task, to learn new things. Face a problem of how to save the model on the drive and cloud bucket, First thing was to use two functions to do that but after some thinking find a way to save both sections in a simple function and did that. Apply three different moods and those react on a different perspective. Also importing the pre-trained models and working with those are so amazing thanks to Tensorlow and Keras.


