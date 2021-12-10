import os
import face_recognition as fc
import datetime as dt
import cv2 as cv
import mediapipe as mp
import playsound as ps
from tkinter import *
from PIL import Image, ImageTk




















mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils



allfile = os.listdir('files')
encodeArray = []
name_array = []
for file in allfile:
    fileload = fc.load_image_file(f'files/{file}')
    file_encoding = fc.face_encodings(fileload)
    encodeArray.append(file_encoding)
    name_split = str(file).split('.')
    name = name_split[0]
    name_array.append(name)

# print(encodeArray)
# print(name_array)



class Face_match():
    def check_image(self):
        for (known_code_image, name) in zip(encodeArray, name_array):
            # print(unknown_encode_image)
            if len(unknown_encode_image)>0:
                results = fc.compare_faces([known_code_image[0]], unknown_encode_image[0])
                # print(results)
                if results[0] == True:
                    # os.path.exists('atn.csv')
                    ps.playsound('sc.mp3')
                    return name
















cap = cv.VideoCapture(0)
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
    while True:
        ret, image = cap.read()
        # rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)


        # face_locations = fc.face_locations(image)
        # print(face_locations)
        # if len(face_locations)>0:
        #     cv.rectangle(image,(face_locations[0][0], face_locations[0][1]),(face_locations[0][2], face_locations[0][3]),(0,255,255), thickness=10 )

        image.flags.writeable = False
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        results = face_detection.process(image)








        unknown_encode_image = fc.face_encodings(image)
        your_name=Face_match().check_image()
        print(your_name)

        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)
        # Flip the image horizontally for a selfie-view display.
        cv.putText(image,your_name,(50, 50),color=(0,255,255), thickness=2, fontFace=cv.FONT_ITALIC, fontScale=2)




        cv.imshow('MediaPipe Face Detection', cv.flip(image, 1))

        

        








      


        if cv.waitKey(10) & 0xff == ord('q'):
            break



cap.release()
cv.destroyAllWindows()