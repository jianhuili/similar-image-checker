# -*- coding:utf-8 -*-
import os
import img_check.image_checker as image_checker

def test_get_image_exif_info():
    img_filepath = os.path.join(os.path.dirname(__file__),"../data/test_img_raw.jpg")

    exif_info = image_checker.get_image_exif_info(img_filepath)

    print("Image: {} ,Exif info: {}".format(img_filepath, exif_info))

def test_get_image_exif_info02():
    img_filepath = os.path.join(os.path.dirname(__file__),"../data/test_img01.jpg")

    exif_info = image_checker.get_image_exif_info(img_filepath)

    print("Image: {} ,Exif info: {}".format(img_filepath, exif_info))

def test_find_similar_images():
    img_dir = os.path.join(os.path.dirname(__file__),"../data/check_images")

    print ("image_dir:", img_dir)
    results = image_checker.find_similar_images(img_dir)

    print("Results: ",results)