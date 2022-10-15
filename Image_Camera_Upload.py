import cv2
import subprocess

def take_picture():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Take an image of burn: ") # DISPLAY VIDEO WINDOW

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Take an image of burn: ", frame)

        k = cv2.waitKey(1)
        if k%256 == 27: # ESCAPE BUTTON PRESSED
            print("Closing...")
            break
        elif k%256 == 32: # SPACE pressed
            # img_name = "opencv_frame_{}.png".format(img_counter)
            # cv2.imwrite(img_name, frame)
            # print("{} written!".format(img_name))
            # img_counter += 1
            image = frame
            break

    cam.release()
    cv2.destroyAllWindows()

    cv2.imshow("image", image)
    while True:
        k = cv2.waitKey(1)

        if k%256 == 27:
            break        
            
    # BELOW PRINTS THE ARRAY OF THE IMAGE
    # print (image)


def upload_image():
    # subprocess.Popen(r'explorer /select,"C:/medi-scanner"')

    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    print (file_path) # SAVES FILE PATH, FOR EXAMPLE, "C:/medi-scanner/Data/First Degree/first_degree (1).jfif"


    image = cv2.imread(file_path) # IMAGE IS SAVED IN VARIABLE AS NP ARRAY
  

    # BELOW OPENS THE IMAGE IN IMSHOW METHOD
    window_name = 'image'
    # Using cv2.imshow() method
    # Displaying the image
    cv2.imshow(window_name, image)
    # waits for user to press any key
    # (this is necessary to avoid Python kernel form crashing)
    cv2.waitKey(0)
    # closing all open windows
    cv2.destroyAllWindows()


def main():
    # take_picture()
    upload_image()
    
if __name__ == '__main__':
    main()