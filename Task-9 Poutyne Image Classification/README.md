#### Workflow of Poutyne Image Classification

In this task, Done Image classification in a tricky way. Already told about the dataset creation in previous task so in this task do classification on that dataset. Used timm library from pytorch and apply one pretrained model with and without weights and save model after complete each epoch on google drive and google cloud bucket.

Poutyne is basically a little and smothe framework from pytorch here can train any model with less code than pytorch, everyone think that it like keras on pytorch. It have all the method and parameter and extention that shoud have a better model. It have experiment manager like mlflow, wandb and customize metrics and difference training segment.


##### EDA

In EDA segment, basically do little bit EDA like checking image size and other feature.First import image using os then used torch imagefolder for extract image with transform version and also tensor. Before going forward I want to thanks `Albumentations`, Excellent image augmentation library I used here, Its best because it a single interface to work with different computer vision tasks such as classification, semantic segmentation, instance segmentation, object detection, pose estimation.

Did some as usual image augmentation like Horzintal and vertical flip, Transpose, RadomBrightNess and Contrast to image visuality and shft of RGB and two types of distortion then lastly convert into tensor and load with dataloader with the batxh_size of 128 and 2 workers use for process those data. but note that on Test_set there is No augmentation just generall resize used.


#### Model: 
Already Mentioned that here will applied transfer learning, used just one model with and without weights. Lets just reveal the model name which is `EfficientNetv2-B2. This model basically an updated version of efficientNet where some issues and those are adressed here. Like go more further to increase training speed and  parameter efficiency. For both model used same epoch and learning rate and used cross_entropy and adam optimizer with 0.005 learning_rate.

#### Difference Call Back function

**Wandb** Used wandb here as experiment manager and check the parameters and loss and different epoch. Wandb is basically one of the best experiment manager with great visuality. Here I try to focus best loss and best valid and accuracy from all epoch.

**Model checkpoints and save Drive** Here save model on drive and local_envitonment. Basically save the whole model on drive also kaggle and main part is google cloud bucket from notebook. After completing each epoch model automaticaly save two directory.

**CSV Logger** For normal tracking loss and accuracy I implement here another callback function which is csv_logger it track the loss and acc for each epoch and visualized this after training.

All four callback function are called from the training portion to execute and it well better.

#### 
Lets discuss the loss and accuracy of each model, First check the training and validation part then will see the what happend on unseen data.

| Model| Accuracy |loss|
| ----- | ----- |-----|
|EfficinetNetV2-B2-Weights| 93.802|0.14629|
|EfficinetNetV2-B2-Random_weights|80.8|0.434|

Conclusion: Nice task very happy to complete, Faced some complexity on poutyne model intragration and training also on  introduced multiple callback function to the model pipeline and finally complete. 
