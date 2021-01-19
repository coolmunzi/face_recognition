**Introduction**

This Face Recognition project is based on MTCNN, MXNet and Keras. This project performs following
tasks:

1. Capture images of person's face using MTCNN from the webcam for training

2. Extract embeddings of face from the stored images using MXNET based Insightface

3. Train the Keras based model for face recognition using captured face embeddings and stored images

4. Using the model generated, predict the person's face from webcam feed.

**Applications of Face Recognition**

1. Online Account Verification
2. Attendance System
3. Office Security Clearance
4. Pension and Visa verification
5. Criminal suspect identification


**Tech Stack Used**

1. MTCNN for face detection

2. MXNet based Insightface for capturing facial embeddings

3. Keras for creating Face Recognition model

4. OpenCV for image processing

**Usage**

1. Clone the repository: 
   
   `git clone https://github.com/coolmunzi/face_recognition.git`
        
2. Navigate to the downloaded directory and install the dependencies:
  `pip install -r requirements.txt`
   
3. Start the project:
    `python main.py`
    

