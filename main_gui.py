from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
import face_recognition as fc
import datetime as dt
import cv2 as cv
import mediapipe as mp
import playsound as ps
import csv
from tkinter.messagebox import *
import json









root = tk.Tk()
root.geometry('600x600+100+60')



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


attendance = []



# def check_per_name(name):
#     if len(attendance)>0:
#         for data in attendance:
#             if data['name'] == name:
#                 pass 
#             else:
#              attendance.append({'name':name,'time':str(dt.datetime.now())})
#              print(attendance)


class Face_match():


   






    def check_image(self, unknown_encode_image):
        for (known_code_image, name) in zip(encodeArray, name_array):
            # print(unknown_encode_image)
            if len(unknown_encode_image)>0:
                results = fc.compare_faces([known_code_image[0]], unknown_encode_image[0])
                # print(results)
                if results[0] == True:
                    # os.path.exists('atn.csv')
                    
                    if len(attendance)==0:
                         attendance.append({'name':name,'time':str(dt.datetime.now())})
                         ps.playsound('sc.mp3')
                    else:
                     for data in attendance:
                        print(data)
                        if data['name'] == name:
                            pass
                        else:
                            attendance.append({'name':name,'time':str(dt.datetime.now())})
                            print(attendance)
                     ps.playsound('sc.mp3')

                    return name

 



def start():
 mp_face_detection = mp.solutions.face_detection
 mp_drawing = mp.solutions.drawing_utils
 cap = cv.VideoCapture(0)
 cap.set(cv.CAP_PROP_FRAME_WIDTH, 620)
 cap.set(cv.CAP_PROP_FRAME_HEIGHT, 620)
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
        your_name=Face_match().check_image(unknown_encode_image)
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


















# attendance value send to the server

def get_attendance():
    print(attendance)


def get_csv_file():
    if os.path.exists('your_value.csv') == True:
        with open('your_value.csv', mode='a') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            employee_writer.writerow(attendance)
    else:
       with open('your_file.csv', 'w+') as employee_file:
           employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
           employee_writer.writerow(attendance)


def get_json_file():

    

    if os.path.exists('your_value.json') == True:
        with open('your_value.json', mode='a') as employee_file:
            json_value = json.dump(attendance,employee_file)
    else:
       with open('your_value.json', 'w+') as employee_file:
           json_value = json.dump(attendance,employee_file)





def delete_file(path):
    get_question_value = messagebox.askokcancel('Delete','Are you sure you want to delete it?')
    if get_question_value == True :
        print('delete done')
        os.remove(path)
    else:
        print('delete cancel')



    

    



   









btn = Button(root, text='click me', bg='blue', fg='white',width=100,command=start)
btn.pack()

btn = Button(root, text='process me', bg='blue', fg='white',width=100,command=get_csv_file)
btn.pack()
btn = Button(root, text='Delete', bg='red', fg='white',width=100,command= lambda: delete_file('your_file.csv'))
btn.pack()
btn = Button(root, text='Get json value', bg='gray', fg='white',width=100,command=get_json_file)
btn.pack()


# token_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
# token_entry.place(x=490.0, y=137+25, width=321.0, height=35)
# token_entry.focus()

imageBtn = tk.PhotoImage(file='generate.png')

path_picker_button = tk.Button(
    image = imageBtn,
    text = '',
    compound = 'center',
    fg = 'white',
    borderwidth = 0,
    highlightthickness = 0,
   
   )

path_picker_button.place(
    x = 783, y = 319,
    width = 224,
    height = 32)





root.mainloop()