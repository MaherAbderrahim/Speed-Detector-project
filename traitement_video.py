import cv2
import numpy as np
def extraire_toute_les_frame(videofile):
    cap = cv2.VideoCapture(videofile)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    frames_array = np.array(frames)
    return (frames_array)

##detcetion des voiture et leur modele et donner un id pour chaque voiture

##definir le modele pour la longueur de la voiture

##executer le modele

##faire un dictionnaire avec les id et les modeles 

def calcul_nbframe_unefois(id,frames):
    nbframe = 0
    for i in frames:
        nbframe += 1
        ##detecter la voiture avec id
        ##creer la ligne suivant le dernier point de la voiture
        ##detecter quand le premier point de la voiture passe la ligne
        ##si la voiture est detecter alors
        break 
    return (nbframe)
def calcul_nbframe_moyenne(id,frames):
    nbframes = [0]
    i=0
    for i in range(sum(nbframes),len(frames)):
        nbframes.append(calcul_nbframe_unefois(id,frames))
    return (sum(nbframes)/len(nbframes))

