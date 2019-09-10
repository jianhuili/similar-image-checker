import cv2
import os
from img_check.image_comparer import compare_image_by_hash

base_img = None
blur_img = None
shift_img = None
resize_img = None

def init_img_data(base_img_filepath):
    blur_img_filepath = os.path.join(os.path.dirname(__file__),"../data/attack_images/","image_blur.jpg")
    shift_img_filepath = os.path.join(os.path.dirname(__file__),"../data/attack_images/","image_shift.jpg")
    resize_img_filepath = os.path.join(os.path.dirname(__file__),"../data/attack_images/","image_resize.jpg")

    base_img = cv2.imread(base_img_filepath)

    ## gaussian blur attack
    blur_img = cv2.gaussianBlur(base_img, {7,7}, 2, 2)
    cv2.imwrite(blur_img_filepath, blur_img)

    ##after shift attack

    ## detect similar image after resize
    (h,w,c) = base_img.shape
    resize_img = cv2.resize(base_img, {h-100, w-100})
    cv2.imwrite(resize_img_filepath, resize_img)

def compute(algo):
    print("algo: {}".format(algo))
    # compare blur attack image
    result = compare_image_by_hash(blur_img, base_img, algo)
    print("gaussian blur attack result: ".format(result))

    # compare blur attack image
    result = compare_image_by_hash(resize_img, base_img, algo)
    print("resize attack result : ".format(result))

def main():
    compute("phash")
