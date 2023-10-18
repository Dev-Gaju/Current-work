#### WorkFlow for Model Serving

Basically its a combine task where I am doing multiple litle task to complete this. I already mention in the task-9 where train two model basically one model with two version one is pretrained weight an another is random weight with EfficientNetv2b2. Now here first convert the model to ONNX(Open Neural Network Exchange) to serve the model via docker.


##### ONNX Conversion:
An open source artificial intelligence ecosystem where machine learning model can be converted in a general formate. Like any kind of model can be converted to this version Pytorch, tensorflow, keras also general machine Learning model and then serve the docker. For this task I do my two best model to convert and use with FastAPI.

##### FastAPI
Modern Web Framework for building RESTFull API in python like all are do in FLASK. Using this we can do anything like PUT, POST, DELETE and also create Route using FASTAPI. Here this task I used it to create image classification model serving with that. 

#### Docker 
Docker is a platform for building, deploying, and running containerized applications. It provides a standard way to package and distribute applications, making it easy to run the same code on different environments. Docker containers are isolated from each other, providing a lightweight and portable runtime environment for applications.


#### WSL
WSL define as windows susbsystem for Linux which helps you to to run a Linux file on operating system. It requires less resources than a full virtual machine. WSL helps to run Linux command alongside windows command line. In windows there is version and WSL2 is offer faster performance.


Generally, In this job process complete multiple types of works to get the job done. After converting this model this import with ONxruntime them proprocess the data with openCV and shows multiple endpoint. Using fastAPI with swagger create two endpoints and thats work. After that do the task with docker like creating docker image and run it from the docker.


**Conclusion:** Faced multiple types of dificulties while try to push the model with Docker like WSL error and also not finding the path of main file. Install several libraries with RUN funtion and do finally get done with the help of my boss.Learn a lot from this task like serving model from FASTAPI also docarize the model.
