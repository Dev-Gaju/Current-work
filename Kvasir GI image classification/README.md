##### Working Flow

In this task, Given a multi-class image classification dataset and FastVit paper and have to implement the paper from timm library with that dataset on subclass Image dataset and several accuracy metrics like F1-score, top-3 and top-5 accuracy.

#### Dataset
Autometic detection on diseases by use computer is an important but strill unexplored on reaserch. Human digestive system may be affected several diseases like esophageal, stomach and colerectal cancer amccounts for 2.8 million new casses and 1.8 million deaths every year.Kvasir a dataset containing image from inside the gastrointesnial(GI) track. Collection of image are classifies into three important anatomical landmarks and three clinically significant with two image of related endoscopic polyp removal. There is total 8000 images and each class contain 1000 images.The dataset consist image with difference resolution from 720x576 to 1920x1072 pixels and organized with separate folder name accordingly.


#### EDA
As mentioned in dataset is a multiclass classification with medical images. Check basic notes like size, shape, pixel contribution, color contribution and view each images from each class. Count the shape from each resolution and got there is 5137 images from  576x720 resolution and 2122 images from 1024x1280 resolution and every images from 3 channel. Then try to find the inerpolation are of images by doing crop, rotation, flip,resiging, transpose and so on.

#### Pytorch Lighting
PyTorch is extremely easy to use to build complex AI models. But once the research gets complicated and things like multi-GPU training, 16-bit precision and TPU training get mixed in, users are likely to introduce bugs. Pytorch Lighting solves exactly this issue and lighting struture pytorch code so it can details and abstract on training.Basically it was created proffesional researcher and PHD students for working with AI research.

#### Data Preparation and Model Build
FastVit paper is a recent paper from transformer and its gained SOTA result on several sector with ImageNet-1k dataset. In this paper authors trained their image with 256x256 and find-tuned with 384x384 resolution. So I choose fine-tuned image size for this model which is 384x384. Then differentiate this images with label and data with sub-Image classes. After classified those images with labels as well as divided into three section training, validation, testing size with 5564, 1600, 832 accordingly.In that paper used 1024 batch-size but my computional shortage apply 64 batch-size. Then do difference augmentation on difference part like simple resize and normalizaion apply on testing and validation part and training part applied difference technique from albamentation library. Forgot to mension that here I follow image classification technique from the paper.
Again faced computational problem for selecting upper benchmark model with high top-1 accuracy.When I try to select FastViT-SA12, or SA34 got computational error and out of VRAM. But then try to apply multiple GPU from kaggle that worked but facing error with mixed-precision protocol coz in my task mentioned that work with mixed precision and notebook-ddb not working with mixed-precision and such kind of dificulties then I choose the small one which is FastVit-T8. and follow other parameters like learning rate 0.001, AdamW optimizer with weight decay 0.05 and so on. last but not the least used wandb to track to accuracy and error.

#### Result and Accuracy: 
Now time to write the result of this injected model on the Kvasir dataset. This result containing the last epoch of the model which is 40th epoch of the model. Getting better accuracy on training and testing but validation have little bit less than those two.
| Model| Accuracy |loss|F1-Score|Top-3|Top-5|
| ----- | ----- |-----|-----|-----|-----|
|FastVit-t8|92.37| 0.263|0.9220|0.99875|1.0|

#### Conclusion:
Another more interesting task done. Face dificulties on mixed-precision with multiple GPU and cannot get done. Basically main thing is when I run code with kaggle notebook and stratregy="ddb_notebook" with multiple-gpu and mixed-precision then it give me error but without mix-precision got me there. for this reason just tried out the little model with less top-1 accuracy from fastvit. 

