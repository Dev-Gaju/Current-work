#### Workflow

Worked with Two Dataset from kaggle. One is DogVsCat and another is Dogbreed. Both dataset have variance type of images. In dogVsCat dataset there is 25,000 images But I just take only cat images from here with model and split on train and test dataset. In Dog Breed dataset have 120 category and 10222 dataset. For dog section take only 105 breed for training and remaining breed for test. Point is, If a breed in training in cann't be present on testing.

#### Collect and Copy
This task have done with google colab, From google colab have to integrate Kaggle with its API and download datset from there. Then do zip unzip process and some processing.

After that, Divided dataset with given Instruction and create folder as mentioned on isntruction. Two Mother folder on is training and another testing and both have two folders for dog & cat.

In dividing part, there is a rules and strictly mentioned that in train dataset both cat and dog have to 8995 images. It easy to take on catVsDog dataset but tough on Dogbreed dataset. Because two parameter here 105 breed and 8995 images. So, after calculation if take frist 105 breed then it be 8995 images. But if we take random breed then it will be missmached.

Then make label for train and test dataset from the given dataframe. After concat and rename their column name save to the directory.

 Folder Formate: 
         In **train**<br>
                 <br>- dog
                 <br>- cat
            <br> **test**
                 <br>-dog
                 <br>-cat
                 
Conclusion: Learn new stuff and enjoy the work, First face a little confusion then it clear and solved. Nurturing dataset between colab and kaggle very interesting and Ofcourse play with dataset also very extining. Thanks for those extiting Taskes.