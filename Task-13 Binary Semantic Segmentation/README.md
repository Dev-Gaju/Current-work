### Working Flow on Segmentation

Segmentation is on of the popular invention of Deep Learning and this can apply too many areas on real life. In this section will discuss and apply pixel wise segmentation on the dataset of Kvasir Seg.

#### Dataset
It is an open-access dataset of gastrointestinal polyp images and corresponding segmentation masks, manually annotated and verified by an experienced gastroenterologist. There is 1000 polyp images with mask as ground Truth and also mention about the resolution of the dataset is 332x482 to 1920x1072 pixels.Those image files are encoded using JPEG compression. The dataset also have bounding box to identified the polyp on images.

#### EDA and Augmentation

On EDA section check several like check image size and mask size and identified big mask and Image length. Then try to preprocess dataset for model.Firstly, import dataset as image and mask then make dictionary to divided mask and image together for train, test and validation. In the task already mentioned that tran images size will be 900 and 50 , 50 for the validation and testing.

After dividing those images now apply augmentation on each part for betterment of the model.For three section create 2 augmentation path using Albumentation. In training part apply several flip and rotation with resize those images as a fixed size. On test and validation section apply same technique like resize and normalization.


#### Pytorch Segmentation model
Very popular and effective library for segmentation. Pytorch segmentation have different type of architecture and encoder as well as pretrained weights. Have difference types of parameter to chosing design of architecture and encoder skteps. In architecture section I chose Unet++ for my dataset and a encoder with resnet101 encoder. Adam optimizer with learning rate 0.0003 which is best for Adam.

#### Metrics and loss
In terms of loss and metrics segmentation model is difference from other traditional model. In segmentation most popular metrics is IOU(intersection over Union) and difference types of loss like focal loss, diceloss and so on. In this task mentioned to chose IOU and Dice Loss to apply this model. Besides that I also try to find out Dice-efficiency from DiceLoss. In can be calculate like 1-DiceLoss which is 0.90729 from my test dataset.

#### Result : 

In segmentation, Basically model try to classify each pixel and predict the result so Augmentation and preprocessing played very crucial part on that. I tried several augmentation and resizing paert from the libary Albumentations.Which is one of the best and very nicely present with torch. Trine 60 epoch using multiple GPU on Kaggle and got best val_loss on 47 epoch among 60. Then try to load that weight and predict the result from the test loader.

| Val_Loss|Dice_eff |Iou_training |IOU testing|
| ----- | ----- |-----|---------|
|0.11985| 0.90729|0.83299|0.787586|


#### Conclusion
Faced several dificulties like preprocess Image together and how to do fit the model together like mask and images. In this section Albumentatios helps, Thanks to Albumentatios. Then another way faced on reducing loss on Dice Loss, Technically diceloss have from_logits is True and I also used sigmoid as my activation function then it collaps with loss. Then my reporting boss tell me to check that and I find that error and use as from_logits=False on DiceLoss and model do well and both side. Loats of Improvement left like more EDA on Pixel wise and find perfect formate to find feed the data to model.