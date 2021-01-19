**Introduction**

This Face Recognition project is based on MTCNN, MXNet and Keras. This project performs following
tasks:

1. Capture images of person's face using MTCNN from the webcam for training

2. Extract features of face from the stored images using MXNET based Insightface

3. Train the Keras based model for face recognition using captured face embeddings and stored images

4. Using the model generated, predict the person's face from webcam feed.


**Applications of Face Recognition**

1. Online Account Verification
2. Attendance System
3. Office Security Clearance
4. Pension and Visa verification
5. Criminal suspect identification



**Tech Stack Used**

1. [MTCNN](https://github.com/ipazc/mtcnn) for face detection

2. [MXNet](https://mxnet.apache.org/) based [Insightface](https://github.com/deepinsight/insightface) for capturing facial features

3. [Keras](https://keras.io/) for creating Face Recognition model

4. [OpenCV](https://opencv.org/) for image processing

5. [DLib](https://github.com/davisking/dlib) for face tracking

**Usage**

1. Clone the repository: 
   
   `git clone https://github.com/coolmunzi/face_recognition.git`
        
2. Navigate to the downloaded directory and install the dependencies:
  `pip install -r requirements.txt`
   
3. Start the project:
    `python main.py`
   
4. Enter your name when prompted in the console.
5. Focus on webcam while our images are captured. Webcam will stop once 10
images are captured. You can increase this number if you want to improve the model accuracy.
   
6. The project will train a face recognition model based on the images 
captured and facial embeddings generated from these captured images
   
7. Once model is trained, webcam will start, and you can now face the webcam
to check the model prediction.
   
    
   
    

