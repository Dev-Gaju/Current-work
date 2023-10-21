##### Working Flow

This task is related to task-11 where I create a model from fastVit using Kvasir dataset dataset. In this task also apply classification but difference way like just extract those feature using that fastVit model with previous model best weight and apply several machine learning algorithm with this feature.

#### Dataset
Autometic detection on diseases by use computer is an important but still unexplored on reaserch. Human digestive system may be affected several diseases like esophageal, stomach and colerectal cancer amccounts for 2.8 million new casses and 1.8 million deaths every year.Kvasir a dataset containing image from inside the gastrointesnial(GI) track. Collection of image are classifies into three important anatomical landmarks and three clinically significant with two image of related endoscopic polyp removal. There is total 8000 images and each class contain 1000 images.The dataset consist image with difference resolution from 720x576 to 1920x1072 pixels and organized with separate folder name accordingly.

Using this dataset create a feature extraction dataset using FastVit. Just a query in the Fastvit model improvised the classification layer with sequntial layer and the output of each image will be 768 instead of 8 that means instead of using classification values take feature for 8000 images and make a pickle file.

#### EDA
As mentioned in dataset is a multiclass classification with medical images. Check basic notes like size, shape, pixel contribution, color contribution and view each images from each class. Count the shape from each resolution and got there is 5137 images from  576x720 resolution and 2122 images from 1024x1280 resolution and every images from 3 channel. Then try to find the inerpolation are of images by doing crop, rotation, flip,resiging, transpose and so on.


#### Pytorch Lighting
PyTorch is extremely easy to use to build complex AI models. But once the research gets complicated and things like multi-GPU training, 16-bit precision and TPU training get mixed in, users are likely to introduce bugs. Pytorch Lighting solves exactly this issue and lighting struture pytorch code so it can details and abstract on training.Basically it was created proffesional researcher and PHD students for working with AI research.

#### Data Preparation and Model Build
FastVit paper is a recent paper from transformer and its gained SOTA result on several sector with ImageNet-1k dataset. In this paper authors trained their image with 256x256 and find-tuned with 384x384 resolution. So I choose fine-tuned image size for this model which is 384x384. Then differentiate this images with label and data with sub-Image classes. After classified those images with labels as well as divided into three section training, validation, testing size with 5564, 1600, 832 accordingly.In that paper used 1024 batch-size but my computional shortage apply 64 batch-size. Then do difference augmentation on difference part like simple resize and normalizaion apply on testing and validation part and training part applied difference technique from albamentation library. Forgot to mension that here I follow image classification technique from the paper.

Now after that process, This time just create model from timm with `pretrain_weight=False` and `Feature_only=False` then improvised the model head for feature not classification result. In this case just used 768 as output instead of 8. Then apply that model with imageFolder from batch_size=1 and image_size same as mention before. after extracted those feature save as pickle file.

For your information, I just want to mentioned is that I used single model feature extration with SVM,KNN,random Forest, LGBM, XGB and Adaboost also same model applied on combine dataset which extracted from three model.


#### Result and Accuracy: 
Now time to write the result of this injected model on the Kvasir dataset's eatures. This result containing the model accuracy which comes from difference model.This result from single dataset.

| Model| Accuracy |
| ----- | ----- |
|SVM|84.7|
|KNN|80.2|
|Adaboost|58.4|
|Random Forest|80.6|
|LGBM|82.7|
|XGB|82.00|

Lets view the result of combine dataset.

| Model| Accuracy |
| ----- | ----- |
|SVM|99.0|
|KNN|98.8|
|Adaboost|99.4|
|Random Forest|99.8|
|LGBM|99.6|
|XGB|99.6|

#### Conclusion:
Interesting task done, Learn lot of things on this segment and faced some dificulties on extract embedding from VIt model also rearrange the shape an so one. The best model with single data is SVM and with combine data winner model is random forest.

