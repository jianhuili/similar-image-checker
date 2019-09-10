# -*- coding:utf-8 -*-

import cv2
import os
import numpy as np
import glob
import exifread

from .image_comparer import compare_image_by_hash, compare_image_by_feature, compare_image_by_orb


def compare_image(chk_img, base_img, mode="feature", algo=None):

    result = None
    if (mode == "feature"):

        # result = compare_image_by_feature(chk_img, base_img, algo)
        result = compare_image_by_orb(chk_img, base_img)

    elif (mode == "hash"):

        result = compare_image_by_hash(chk_img, base_img, algo)

    else:
        None

    return result


def similarity_check(source_image_filepath, compare_to_image_filepath):
    # load base image
    base_img = cv2.imread(source_image_filepath)

    check_img = cv2.imread(compare_to_image_filepath)

    feature_similarity = compare_image(check_img, base_img, "feature")

    hash_similarity = compare_image(check_img, base_img, "hash","MarrHildrethHash")

    return dict(
        src_img=os.path.basename(source_image_filepath),
        compare_to_img=os.path.basename(compare_to_image_filepath),
        similarity = feature_similarity,
        isSimilar =  (feature_similarity > 20)
    )


def check_images(check_img_dir, base_img_filepath, mode ="feature", algo = None):
    # load base image
    base_img = cv2.imread(base_img_filepath)

    # Load and compare all the images
    img_search_pattern = check_img_dir + "/*.jpg"
    for f in glob.iglob(img_search_pattern):
        image = cv2.imread(f)
        percentage_similarity = compare_image(image, base_img, mode, algo)

        # output similar check result
        print("Title: {},Similarity: {}\n".format(
            os.path.basename(f), percentage_similarity))

def get_image_exif_info(img_filepath):
   file = open(img_filepath, 'rb')
   exif_info = exifread.process_file(file, details=False)

#    print (exif_info)
   return dict(
       GPSLatitudeRef = str(exif_info.get('GPS GPSLatitudeRef')),
       GPSLatitude = str(exif_info.get('GPS GPSLatitude')),
       GPSLongitudeRef = str(exif_info.get('GPS GPSLongitudeRef')),
       GPSLongitude = str(exif_info.get('GPS GPSLongitude')),
       DateTime = str(exif_info.get('Image DateTime')),
   )

def find_similar_images(check_img_dir):

    check_results = []
    # Load all the images and compare each other
    img_search_pattern = check_img_dir + "/*.jpg"

    img_files = glob.glob(img_search_pattern)
    file_count = len(img_files)

    print ("File count:", file_count)

    for index in range(0, file_count):
        # load base image
        print ("Checking file ... : ", img_files[index])
        base_img_filepath = img_files[index]
        for index2 in range(index+1, file_count):
            check_img_filepath = img_files[index2]
            check_result = similarity_check(base_img_filepath, check_img_filepath)
            print ("Checking result : ", check_result)
            check_results.append(check_result)

    return check_results

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
