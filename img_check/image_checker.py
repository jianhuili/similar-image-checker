# -*- coding:utf-8 -*-

import cv2
import os
import numpy as np
import glob

from .image_comparer import compare_image_by_hash, compare_image_by_feature, compare_image_by_orb 

def compare_image(chk_img, base_img, mode="hash", algo=None):
   
    result = None
    if (mode == "feature"):

        # result = compare_image_by_feature(chk_img, base_img, algo)
        result = compare_image_by_orb(chk_img, base_img)

    elif (mode == "hash"):

         result =  compare_image_by_hash(chk_img, base_img, algo)

    else:
        None

    return  result


def check_images(check_img_dir, base_img_filepath, mode, algo):
    # load base image
    base_img = cv2.imread(base_img_filepath)

    # Load and compare all the images
    img_search_pattern = check_img_dir + "/*.jpg"
    for f in glob.iglob(img_search_pattern):
        image = cv2.imread(f)
        percentage_similarity = compare_image(image, base_img, mode, algo )

        # output similar check result
        print("Title: {},Similarity: {}\n".format(os.path.basename(f), percentage_similarity))

if __name__ == '__main__':

   check_img_dir = "data/check_images/"
   base_img_filepath = "data/base_image.jpg"

   algos = [("hash", "phash"),
            ("hash", "marrhildrethhash"),
            ("hash", "averagehash"),
            ("hash", "colormomenthash"),
            ("hash", "radialvariancehash"),
            ("hash", "blockmeanhash0"),
            ("hash", "blockmeanhash1"),
            ("feature", "orb")]

   for (mode, algo) in algos:
    print("Algo {}.{}".format(mode, algo))
    check_images(check_img_dir, base_img_filepath, mode, algo)
  
