from cgitb import reset
from math import degrees
import cv2
import subprocess
import tkinter as tk
from tkinter import filedialog

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import tensorflow as tf
import PIL
import PIL.Image
import numpy as np

def take_picture():
    # print ("it works")

    cam = cv2.VideoCapture(0)

    
    cv2.namedWindow("Take an image of burn: ") # DISPLAY VIDEO WINDOW

    while True:
        run = None
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        
        window_name = "Take an image of burn: "

        cv2.imshow(window_name, frame)
        cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1) # THIS PUTS IT AT FRONT BUT NOT FOCUSED

        output = None

        k = cv2.waitKey(1)
        if k%256 == 27: # ESCAPE BUTTON PRESSED
            print("Closing...")
            run = False
            break
        elif k%256 == 32: # SPACE pressed
            # img_name = "opencv_frame_{}.png".format(img_counter)
            # cv2.imwrite(img_name, frame)
            # print("{} written!".format(img_name))
            # img_counter += 1
            run = True

            image = frame

            # print (image)

            # cv2.imshow('image', image)

            # image2 = cv2.imread(image)

            predicted = model_predict(image)

            if predicted == 0:
                # first degree
                output = """First degree(7-10 days)

                            Immediate Symptoms:
                            Redness on outermost layer of skin(epidermis)
                            Swelling
                            Minor inflammation
                            No blistering

                            Treatment:
                            Running under cold water or place cool wet cloth over burn(avoid ice as it can agitate the burn)
                            Use skincare products(cream, ointments and pain medication)
                            Judge depending on severity and burn location whether seeking medical attention is necessary. Seek immediate attention if burn affects a widespread area and/ or located on the face, groin, hands and feet.
                            """
            elif (predicted == 1):
                # healthy skin
                output = 'You\'re Healthy!'
            elif (predicted == 2):
                # 2nd degree
                output = """Second Degree(2-3 weeks)
                            Immediate Symptoms
                            Blistering
                            Swelling
                            Extremely red and sore
                            White or discoloured
                            Treatment 
                            Running under cold water or place cool wet cloth over burn(avoid ice as it can agitate the burn)
                            Antibiotic cream for blisters(Don’t pop or pick at blisters, prevent infections)
                            Judge depending on severity and burn location whether seeking medical attention is necessary. Seek immediate attention if burn affects a widespread area and/ or located on the face, groin, buttocks, hands and feet.
                            """
            elif (predicted == 3):
                # 3rd degree
                output = """Third Degree(no set timeline)
                            Immediate symptoms
                            Dark brown and/or waxy and white colour
                            Char
                            Undeveloped blisters
                            Leathery texture 
                            painful/ numbing
                            Treatment
                            Contact emergency services immediately
                            While waiting, raise the unjust above the heart, ensure no clothing is in contact with the brun
                            Antibiotics(prevent infection)

                        """

            # 0- first degree
            # 1- healthy
            # 2- 2nd degrees
            # 3- third degree

            break
    
    cam.release()
    cv2.destroyAllWindows()

    if run:
        cv2.imshow("image", image)
        cv2.setWindowProperty("image", cv2.WND_PROP_TOPMOST, 1)
        while True:
            k = cv2.waitKey(1)

            if k%256 == 27: # waiting for escape
                break        
                
        # BELOW PRINTS THE ARRAY OF THE IMAGE
        # print (image)
    return run, output


def upload_image():
    # subprocess.Popen(r'explorer /select,"C:/medi-scanner"')

    # root = tk.Tk()
    # root.withdraw()
    # root.wm_attributes('-topmost', 1)

    # file_path = filedialog.askopenfilename()
    
    # root.mainloop()

    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.title('Tkinter Open File Dialog')
    root.resizable(False, False)
    root.geometry('300x150')
    # root.withdraw()


    # filetypes = (
    #     ('photo files', '*.jfif'),
    #     ('All files', '*.*')
    # )

    filename = fd.askopenfilename()

    # showinfo(
    #     title='Selected File',
    #     message=filename
    # )

    open_button = ttk.Button(
    root,
    text='Open a File')

    open_button.pack(expand=True)


    # run the application
    root.mainloop()


    
    # print (file_path) # SAVES FILE PATH, FOR EXAMPLE, "C:/medi-scanner/Data/First Degree/first_degree (1).jfif"

    # WERE GONNA NEED THIS TO DISPLAY ON TOP!!!!!!!!!!!!

    image = cv2.imread(filename) # IMAGE IS SAVED IN VARIABLE AS NP ARRAY

    predicted = model_predict(image)

    if predicted == 0:
                # first degree
        output = """First degree(7-10 days)

                            Immediate Symptoms:
                            Redness on outermost layer of skin(epidermis)
                            Swelling
                            Minor inflammation
                            No blistering

                            Treatment:
                            Running under cold water or place cool wet cloth over burn(avoid ice as it can agitate the burn)
                            Use skincare products(cream, ointments and pain medication)
                            Judge depending on severity and burn location whether seeking medical attention is necessary. Seek immediate attention if burn affects a widespread area and/ or located on the face, groin, hands and feet.
                            """
    elif (predicted == 1):
                # healthy skin
        output = 'You\'re Healthy!'
    elif (predicted == 2):
                # 2nd degree
        output = """Second Degree(2-3 weeks)
                            Immediate Symptoms
                            Blistering
                            Swelling
                            Extremely red and sore
                            White or discoloured
                            Treatment 
                            Running under cold water or place cool wet cloth over burn(avoid ice as it can agitate the burn)
                            Antibiotic cream for blisters(Don’t pop or pick at blisters, prevent infections)
                            Judge depending on severity and burn location whether seeking medical attention is necessary. Seek immediate attention if burn affects a widespread area and/ or located on the face, groin, buttocks, hands and feet.
                            """
    elif (predicted == 3):
                # 3rd degree
        output = """Third Degree(no set timeline)
                    Immediate symptoms
                    Dark brown and/or waxy and white colour
                    Char
                    Undeveloped blisters
                    Leathery texture 
                    painful/ numbing
                    Treatment
                    Contact emergency services immediately
                    While waiting, raise the unjust above the heart, ensure no clothing is in contact with the brun
                    Antibiotics(prevent infection)

                        """

            # 0- first degree
            # 1- healthy
            # 2- 2nd degrees
            # 3- third degree
  

    # # BELOW OPENS THE IMAGE IN IMSHOW METHOD
    # window_name = 'image'
    # # Using cv2.imshow() method
    # # Displaying the image
    # cv2.imshow(window_name, image)
    # cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1) 
    # # waits for user to press any key
    # # (this is necessary to avoid Python kernel form crashing)
    # cv2.waitKey(0)
    # # closing all open windows
    # cv2.destroyAllWindows()

    # print (image)

    chose = None
    if image is not None: # IF USER CHOSE IMAGE
        chose = True
    else: # IF USER DID NOT CHOOSE IMAGE
        chose = False

    return chose, output # RETURN TRUE OR FALSE BASED ON IF UDER CHOSE AN IMAGE OR NOT

def model_predict (img):
    scanner_model = tf.keras.models.load_model("/medi-scanner/keras_save/burns")

    img = cv2.resize(img, dsize=(299, 299))

    # print(img)

    pred_img = img# .resize((299 , 299))
    pred_img = np.array(pred_img)/255.0
    pred_img = pred_img.reshape(1 , 299 , 299 , 3)

    res = scanner_model.predict(pred_img)

    print (res)
    print (np.argmax(reset))
    
    return np.argmax(res) # returns an integer

    # 0- first degree
    # 1- healthy
    # 2- 2nd degrees
    # 3- third degree


def main():
    bool, output = take_picture()
    print (output)
    # upload_image()
    
if __name__ == '__main__':
    main()