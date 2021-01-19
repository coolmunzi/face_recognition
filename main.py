from utils import capture_faces as cap_face, facial_recognition_model_training as face_recog_model_train, \
    generate_face_embeddings as gen_face_emb
from utils.face_predictor import FacePredictor

if __name__ == '__main__':
    name = input("Enter name of the person: ")
    MAX_IMAGES = 10
    PATH = f'./dataset/{name}'

    #Collect the training data
    cf = cap_face.TrainingDataCollector()
    print("[Event]----------Collecting images for face detector training----------")
    cf.collectImages(MAX_IMAGES, name, PATH)


    print("[Event]------------Capturing Face Embeddings--------------------")
    gfe = gen_face_emb.GenerateFaceEmbedding()
    gfe.genFaceEmbedding(PATH)

    print("[Event]------------Starting Face Recognition Model Training--------------------")
    frmt = face_recog_model_train.TrainFaceRecogModel()
    frmt.trainKerasModelForFaceRecognition()

    print("[Event]------------Starting Prediction from Webcam feed--------------------")
    faceDetector = FacePredictor()
    faceDetector.detectFace()






