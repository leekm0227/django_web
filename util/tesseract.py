import os
import numpy as np
import time
from PIL import ImageGrab, Image
from multiprocessing import Process
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata" --oem 1'
top = 400
left = 150
width = 400
height = 200


def run(bytes_img):
    img = Image.open(bytes_img)
    return pytesseract.image_to_string(img, lang='kor+eng', config=config)


class Test:
    proc = Process()
    img = None

    def __init__(self):
        pass

    def run(self):
        while True:
            self.img = np.array(ImageGrab.grab(bbox=(left, top, left + width, top + height)))
            cv2.imshow('test', cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))

            # self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            # self.img = cv2.GaussianBlur(self.img, (5, 5), 0)
            # self.img = cv2.adaptiveThreshold(self.img, 255, 1, 1, 11, 2)
            # cv2.imshow('test2', cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))

            if not self.proc.is_alive():
                print("set process")
                self.proc = Process(target=self.tesseract)
                self.proc.start()

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

    def tesseract(self):
        if self.img is not None:
            start = time.time()
            result = pytesseract.image_to_string(self.img, lang='kor+eng', config=config)
            os.system('cls')
            print(result.strip())
            print("=" * 20)
            print("sec : {}".format(time.time() - start))


if __name__ == "__main__":
    Test().run()
