# MLSP2018
# run sequence 
python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7


python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle

python recognize_video.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle


#Development Plan
- [x] Delete files not needed from repo
- [] Make a script for starting the program
- [] Clean the code up and make it wokring
- [] Allow adding users on the fly
