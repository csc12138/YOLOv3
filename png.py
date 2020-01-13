import numpy as np
from PIL import Image
import os
import cv2 as cv


def convert_to_png(dict_in, dict_out):
    print("[*] Checking image format:")
    current_num = 0
    total_num = len(os.listdir(dict_in))
    for file in os.listdir(dict_in):
        read_img = dict_in + '/' + file.strip()
        read_img_fullname = os.path.basename(read_img)
        read_img_name, read_img_format = os.path.splitext(read_img_fullname)
        # if read_img_format == '.png':
        #    current_num += 1
        #    print(current_num, "/", total_num)
        #    continue
        img = Image.open(read_img)
        save_img = dict_out + '/' + read_img_name + '.jpg'
        img.save(save_img)
        current_num += 1
        print(current_num, "/", total_num)


def normal_size(dict_in, dict_out):
    print("[*] Resize image:")
    current_num = 0
    total_num = len(os.listdir(dict_in))
    for file in os.listdir(dict_in):
        read_img = dict_in + '/' + file.strip()
        read_img_fullname = os.path.basename(read_img)
        img = cv.imread(read_img)
        w = img.shape[1]
        h = img.shape[0]

        # crop
        # w1 = int(w*0.25)
        # w2 = int(w*0.75)
        # h1 = int(h*0.2)
        # h2 = int(h*0.6)
        # cropped = img[h1:h2, w1:w2]
        # w = cropped.shape[1]
        # h = cropped.shape[0]

        if w > 800 or h > 800:
            if w > h:
                img = cv.resize(img, (800, 800 * h // w), interpolation=cv.INTER_AREA)
            else:
                img = cv.resize(img, (800 * w // h, 800), interpolation=cv.INTER_AREA)

        # increase
        # if w < 600 or h < 600:
        #     if w > h:
        #         img = cv.resize(img, (600, 600 * h // w), interpolation=cv.INTER_CUBIC)
        #     else:
        #         img = cv.resize(img, (600 * w // h, 600), interpolation=cv.INTER_CUBIC)

        save_img = dict_out + '/' + read_img_fullname
        cv.imwrite(save_img, img)
        current_num += 1
        print(current_num, "/", total_num)


if __name__ == "__main__":
    dic1 = 'E:/E - Course/course/2019-20-MSC-sem2/Dissertation/drive/2 Windows/Uninstalled Windows/jpg'
    dic2 = 'E:/E - Course/course/2019-20-MSC-sem2/Dissertation/drive/2 Windows/Uninstalled Windows/'
    normal_size(dic1, dic2)

