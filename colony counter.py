import cv2
import numpy as np;
import os
import datetime
from settings import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk



class Colony_count:
    def __init__(self):
        self.image_type = "Positive"
        self.camera_num = 0
        self.thresh = 175
        self.circlecertainty = 40
        self.minradius = 1
        self.maxradius = 150

    def run(self):
        self.root = Tk()
        self.root.title(TITLE)
        self.root.configure(background=BGCOLOR)
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        a = Label(self.root, text='Insert a Petri Plate and press the button', bg=BGCOLOR, font="80")
        a.pack()
        self.can = Canvas(self.root, height=CAN_HEIGHT, width=CAN_WIDTH)
        self.can.place(x=IMGCAN_X, y=IMGCAN_Y)
        self.img = Image.open(IMG_FILE)
        self.img = self.img.resize((CAN_WIDTH, CAN_HEIGHT))
        self.img = ImageTk.PhotoImage(self.img)
        self.gray_can = Canvas(self.root, height=GRAY_CAN_HEIGHT, width=GRAY_CAN_WIDTH)
        #self.gray_can.place(x=WIDTH-CAN_WIDTH, y=HEIGHT-CAN_HEIGHT)
        self.gray_image = cv2.imread(IMG_FILE)
        self.gray_image = cv2.cvtColor(self.gray_image, cv2.COLOR_BGR2GRAY)
        self.thresh, self.gray_image = cv2.threshold(self.gray_image, self.thresh, 255, cv2.THRESH_BINARY)
        self.gray_image = Image.fromarray(self.gray_image)
        self.gray_image = self.gray_image.resize((CAN_WIDTH, CAN_HEIGHT))
        self.gray_image = ImageTk.PhotoImage(self.gray_image)

        self.title = Label(self.root, text="Plate Reader", bg=BGCOLOR)
        self.title.pack()

        self.thresh_text = Label(self.root, text=f"Thresh: {self.thresh}")
        self.thresh_text.place(x=THRESH_X, y=THRESH_Y)
        self.thresh_button = Button(self.root, text="Threshold:", command=self.change_thresh, width=THRESHBUTTON_WIDTH)
        self.thresh_button.place(x=THRESHBUTTON_X, y=THRESHBUTTON_Y)
        self.thresh_input = Entry(self.root, width=THRESHINPUT_WIDTH)
        self.thresh_input.place(x=THRESHINPUT_X, y=THRESHINPUT_Y)
        self.thresh_input.insert(0, str(self.thresh))

        self.camera_text = Label(self.root, text=f"Camera number: {self.camera_num}")
        self.camera_text.place(x=CAMNUM_X, y=CAMNUM_Y)
        self.camera_button = Button(self.root, text="Camera number:", command=self.change_camera, width=CAMNUMBUTTON_WIDTH)
        self.camera_button.place(x=CAMNUMBUTTON_X, y=CAMNUMBUTTON_Y)
        self.camera_input = Entry(self.root, width=CAMINPUT_WIDTH)
        self.camera_input.place(x=CAMINPUT_X, y=CAMINPUT_Y)
        self.camera_input.insert(0, str(self.camera_num))

        self.circlecertainty_text = Label(self.root, text=f"Circle certainty: {self.circlecertainty}")
        self.circlecertainty_text.place(x=CIRCLECERTAINTY_X, y=CIRCLECERTAINTY_Y)
        self.circlecertainty_button = Button(self.root, text="Circle certainty:", command=self.change_circlecertainty, width=CIRCLECERTAINTYBUTTON_WIDTH)
        self.circlecertainty_button.place(x=CIRCLECERTAINTYBUTTON_X, y=CIRCLECERTAINTYBUTTON_Y)
        self.circlecertainty_input = Entry(self.root, width=CIRCLECERTAINTYINPUT_WIDTH)
        self.circlecertainty_input.place(x=CIRCLECERTAINTYINPUT_X, y=CIRCLECERTAINTYINPUT_Y)
        self.circlecertainty_input.insert(0, str(self.circlecertainty))

        self.maxsize_text = Label(self.root, text=f"Max colony size: {self.maxradius}")
        self.maxsize_text.place(x=MAXSIZE_X, y=MAXSIZE_Y)
        self.maxsize_button = Button(self.root, text="Max colony size:", command=self.change_maxsize, width=MAXSIZEBUTTON_WIDTH)
        self.maxsize_button.place(x=MAXSIZEBUTTON_X, y=MAXSIZEBUTTON_Y)
        self.maxsize_input = Entry(self.root, width=MAXSIZEINPUT_WIDTH)
        self.maxsize_input.place(x=MAXSIZEINPUT_X, y=MAXSIZEINPUT_Y)
        self.maxsize_input.insert(0, str(self.maxradius))

        self.minsize_text = Label(self.root, text=f"Min colony size: {self.minradius}")
        self.minsize_text.place(x=MINSIZE_X, y=MINSIZE_Y)
        self.minsize_button = Button(self.root, text="Min colony size:", command=self.change_minsize, width=MINSIZEBUTTON_WIDTH)
        self.minsize_button.place(x=MINSIZEBUTTON_X, y=MINSIZEBUTTON_Y)
        self.minsize_input = Entry(self.root, width=MINSIZEINPUT_WIDTH)
        self.minsize_input.place(x=MINSIZEINPUT_X, y=MINSIZEINPUT_Y)
        self.minsize_input.insert(0, str(self.minradius))

        self.image_type_text = Label(self.root, text=f"Image type: {self.image_type}")
        self.image_type_text.place(x=IMGTYPE_X, y=IMGTYPE_Y)
        self.image_type_clicked = StringVar()
        self.image_type_clicked.set(f"Positive")
        self.image_type_drop = OptionMenu(self.root, self.image_type_clicked, "Positive", "Negative")
        self.image_type_button = Button(self.root, text="Select button type:", command=self.change_image_type, width=IMGTYPEBUTTON_WIDTH)
        self.image_type_button.place(x=IMGTYPE_BUTTON_X, y=IMGTYPE_BUTTON_Y)
        self.image_type_drop.place(x=IMGTYPE_INPUT_X, y=IMGTYPE_INPUT_Y)

        self.storesettings_button = Button(self.root, text="Store Settings", command=None, width=STORESETTINGSBUTTON_WIDTH)
        self.storesettings_button.place(x=STORESETTINGSBUTTON_X, y=STORESETTINGSBUTTON_Y)

        self.button = Button(self.root, text="Read Sample", command=self.readSample)
        self.button.pack()
        self.can.create_image((CAN_WIDTH//2, CAN_HEIGHT//2), image=self.img)
        self.gray_can.create_image((GRAY_CAN_WIDTH//2, GRAY_CAN_HEIGHT//2), image=self.gray_image)
        self.root.mainloop()
        cv2.destroyAllWindows()

    def replace_images(self):
        self.img = Image.open(IMG_FILE)
        self.img = self.img.resize((CAN_WIDTH, CAN_HEIGHT))
        self.img = ImageTk.PhotoImage(self.img)
        if self.image_type == "Positive":
            self.gray_image = cv2.imread("test12gray.png")
        elif self.image_type == "Negative":
            self.gray_image = cv2.imread("test12grayinvert.png")
        (self.thresh, self.gray_image) = cv2.threshold(self.gray_image, self.thresh, 255, cv2.THRESH_BINARY)
        self.gray_image = Image.fromarray(self.gray_image)
        self.gray_image = self.gray_image.resize((CAN_WIDTH, CAN_HEIGHT))
        self.gray_image = ImageTk.PhotoImage(self.gray_image)
        self.can.create_image((CAN_WIDTH//2, CAN_HEIGHT//2), image=self.img)
        self.gray_can.create_image((GRAY_CAN_WIDTH//2, GRAY_CAN_HEIGHT//2), image=self.gray_image)

    def store_data(self):
        updated_time = datetime.datetime.now()
        second = updated_time.second
        minute = updated_time.minute
        hour = updated_time.hour
        day = updated_time.day
        month = updated_time.month
        year = updated_time.year
        minute = str(minute)
        if minute in NUMBER_LIST:
            minute = "0" + minute
        if second in NUMBER_LIST:
            second = "0" + second
        with open(os.path.join(GAMEFILE, TEXT_FILE), 'a') as f:
            f.write(f"Colony Count: {self.colony_count}, Time: {month}/{day}/{year}, {hour}:{minute}:{second}\n")
        f.close()

    def readSample(self):
        self.image_type = self.image_type_clicked.get()
        self.cap = cv2.VideoCapture(self.camera_num)
        s, im = self.cap.read()
        cv2.imwrite(IMG_FILE, im)
        self.imagedata_original = cv2.imread(IMG_FILE, 1)
        self.originalImage = cv2.imread(IMG_FILE)
        self.grayImage = cv2.cvtColor(self.originalImage, cv2.COLOR_BGR2GRAY)
        self.thresh, self.bwi = cv2.threshold(self.grayImage, self.thresh, 255, cv2.THRESH_BINARY)
        cv2.imwrite(GRAYIMG_FILE, self.bwi)
        self.inverted_image = cv2.bitwise_not(self.bwi)
        cv2.imwrite(INVERT_GRAYIMG_FILE, self.inverted_image)
        self.gray_blurred = cv2.blur(self.grayImage, (7, 7))
        self.gray_blurred_inverted = cv2.blur(self.inverted_image, (1, 1))
        self.detected_circles = cv2.HoughCircles(self.gray_blurred if self.image_type == "Positive" else self.gray_blurred_inverted,
                                                 DETECTION_METHOD, 1, 20, param1=50, param2=self.circlecertainty, minRadius=self.minradius, maxRadius=self.maxradius)
        if self.detected_circles is not None:
            self.detected_circles = np.uint16(np.around(self.detected_circles))
            for pt in self.detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]
                cv2.circle(self.originalImage, (a, b), r, BGR_GREEN, 2)
                cv2.circle(self.originalImage, (a, b), 1, BGR_BLUE, 3)
        cv2.imwrite(IMG_FILE, self.originalImage)
        try:
            self.colony_count = len(self.detected_circles[0])
        except TypeError:
            self.colony_count = 0
        try:
            self.dot_count.destroy()
        except:
            pass
        self.dot_count = Label(self.root, text=f"Colony Count: {self.colony_count}")
        self.dot_count.place(x=COLONYCOUNT_X, y=COLONYCOUNT_Y)
        cv2.imwrite(IMG_FILE, self.originalImage)

        self.cap.release()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.replace_images()
        self.store_data()

    def change_thresh(self):
        self.thresh_text.destroy()
        text = self.thresh_input.get()
        try:
            self.thresh = int(text)
        except ValueError:
            self.thresh = 0
        self.thresh_text = Label(self.root, text=f"Thresh: {self.thresh}")
        self.thresh_text.place(x=THRESH_X, y=THRESH_Y)

    def change_camera(self):
        self.camera_text.destroy()
        text = self.camera_input.get()
        try:
            self.camera_num = int(text)
        except ValueError:
            self.camera_num = 0
        self.camera_text = Label(self.root, text=f"Camera number: {self.camera_num}")
        self.camera_text.place(x=CAMNUM_X, y=CAMNUM_Y)

    def change_circlecertainty(self):
        self.circlecertainty_text.destroy()
        text = self.circlecertainty_input.get()
        try:
            self.circlecertainty = int(text)
        except ValueError:
            self.circlecertainty = 0
        self.circlecertainty_text = Label(self.root, text=f"Circle certainty: {self.circlecertainty}")
        self.circlecertainty_text.place(x=CIRCLECERTAINTY_X, y=CIRCLECERTAINTY_Y)

    def change_maxsize(self):
        self.maxsize_text.destroy()
        text = self.maxsize_input.get()
        try:
            if int(text) >= int(self.maxradius):
                self.maxradius = int(text)
            else:
                self.maxradius = self.minradius
                messagebox.showerror('Colony Size Erorr', 'The Maximum size of a colony can not be smaller than the minimum size.')
                self.maxsize_input.delete(0, len(self.maxsize_input.get()))
                self.maxsize_input.insert(0, self.maxradius)
        except ValueError:
            self.maxradius = 0
        self.maxsize_text = Label(self.root, text=f"Max colony size: {self.maxradius}")
        self.maxsize_text.place(x=MAXSIZE_X, y=MAXSIZE_Y)

    def change_minsize(self):
        self.minsize_text.destroy()
        text = self.minsize_input.get()
        try:
            if int(text) <= int(self.maxradius):
                self.minradius = int(text)
            else:
                self.minradius = self.maxradius
                messagebox.showerror('Colony Size Erorr', 'The Minimum size of a colony can not be bigger than the maximum size.')
                self.minsize_input.delete(0, len(self.minsize_input.get()))
                self.minsize_input.insert(0, self.minradius)
        except ValueError:
            self.minradius = 0
        self.minsize_text = Label(self.root, text=f"Min colony size: {self.minradius}")
        self.minsize_text.place(x=MINSIZE_X, y=MINSIZE_Y)

    def change_image_type(self):
        self.image_type = self.image_type_clicked.get()
        self.image_type_text.destroy()
        self.image_type_text = Label(self.root, text=f"Image type: {self.image_type}")
        self.image_type_text.place(x=IMGTYPE_X, y=IMGTYPE_Y)
        if self.image_type == "Positive":
            self.gray_image = cv2.imread("test12gray.png")
        elif self.image_type == "Negative":
            self.gray_image = cv2.imread("test12grayinvert.png")
        (self.thresh, self.gray_image) = cv2.threshold(self.gray_image, self.thresh, 255, cv2.THRESH_BINARY)
        self.gray_image = Image.fromarray(self.gray_image)
        self.gray_image = self.gray_image.resize((CAN_WIDTH, CAN_HEIGHT))
        self.gray_image = ImageTk.PhotoImage(self.gray_image)
        self.can.create_image((CAN_WIDTH//2, CAN_HEIGHT//2), image=self.img)
        self.gray_can.create_image((GRAY_CAN_WIDTH//2, GRAY_CAN_HEIGHT//2), image=self.gray_image)

if __name__ == '__main__':
    colony_count = Colony_count()
    colony_count.run()
