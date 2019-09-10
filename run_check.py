# -*- coding:utf-8 -*-

import os
import sys
import getopt
import glob
import time

from img_check.image_checker import similarity_check, get_image_exif_info

def get_image_gps (image_filepath):

    result = get_image_exif_info(image_filepath)

    print (result)

def check_similar_images(check_img_dir, report_filepath):

    # Load all the images and compare each other
    img_search_pattern = check_img_dir + "/*.jpg"

    img_files = glob.glob(img_search_pattern)
    file_count = len(img_files)

     # open result report file
    report_file = open(report_filepath, "w", encoding="uft-8")

    # output report title
    report_titles = ["源照片", "比较目标照片", "特征值相似度","哈希相似度","是否为相似照片" ]
    report_file.write(",".join(report_titles) + "\n")

    start_time = time.time()

    # Loop check all images
    for index in range(0, file_count):
        # load base image
        print ("Checking image ... : ", img_files[index])
        base_img_filepath = img_files[index]
        for index2 in range(index+1, file_count):
            check_img_filepath = img_files[index2]
            check_result = similarity_check(base_img_filepath, check_img_filepath)
            print ("Checking result : ", check_result)

            # output result to file
            report_file.write(
                ",".join([
                    check_result['src_img'],
                    check_result['compare_to_img'],
                    str(check_result['similarity']),
                    "YES" if check_result['isSimilar'] else "NO"
                ]) + "\n")

    report_file.close

    print ("Completed check. Check {} images in {} seconds".format(file_count, time.time()- start_time))

if __name__ == '__main__':

    if (len(sys.argv) <3):
        print ("Pls specify mode and image_dir parameter")

    mode = sys.argv[1]
    image_dir = sys.argv[2]
    if (mode == "similar-check") :

        if (len(sys.argv) > 3) :
            report_file = sys.argv[3]
        check_similar_images(image_dir, report_file)
    
    elif (mode == "image-gps") :

        get_image_gps(image_dir)

    else :
        print("Unsupported mode:", mode)

  
