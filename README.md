# MLSP2018
# run sequence 
python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 <br />
python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle <br />
python recognize_video.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle <br />

or <br /> 

on windows, double click runvideo.bat

#Development Plan
- [x] Delete files not needed from repo
- [x] Make a script for starting the program 
- [] Clean the code up and make it wokring
- [] Allow adding users on the fly
