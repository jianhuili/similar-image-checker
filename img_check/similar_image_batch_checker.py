# -*- coding:utf-8 -*-

import cv2
import os
from shutil import copyfile, rmtree
import time
import glob

from .image_comparer import compare_image_by_hash, compare_image_by_feature, compare_image_by_orb


def similarity_check(source_image_filepath, compare_to_image_filepath):
    # load base image
    base_img = cv2.imread(source_image_filepath)

    check_img = cv2.imread(compare_to_image_filepath)

    feature_similarity = compare_image_by_orb(check_img, base_img)
   
    return dict(
        src_img = os.path.basename(source_image_filepath),
        compare_to_img = os.path.basename(compare_to_image_filepath),
        similarity = feature_similarity
    )

def check_similar_images(check_img_dir, result_dir, check_threshold):

    # Load all the images and compare each other
    img_search_pattern = check_img_dir + "/*.jpg"

    img_files = glob.glob(img_search_pattern)
    file_count = len(img_files)

     # open result report file
    # clear result dir
    if (os.path.exists(os.path.join(result_dir, "similar_images"))):
        rmtree(os.path.join(result_dir, "similar_images"))
    else :
        os.makedirs(os.path.join(result_dir, "similar_images"))

    report_filepath = os.path.join(result_dir,"result_report_{}.csv".format(time.strftime("%Y%m%H%M%S")) )
    report_file = open(report_filepath, "w", encoding="utf-8")

    # output report title
    report_titles = ["分组编号","源照片", "比较目标照片", "特征值相似度","是否为相似照片" ]
    report_file.write(",".join(report_titles) + "\n")

    start_time = time.time()

    found_similar_images = []
    group_index = 0
    # Loop check all images
    for index in range(0, file_count):

        base_img_filepath = img_files[index]

        # skip found similar images
        if (base_img_filepath in found_similar_images):
            continue

        # load base image
        print ("Checking image ... : ", img_files[index])
        group_index +=1
        for index2 in range(index+1, file_count):
            check_img_filepath = img_files[index2]

            check_result = similarity_check(base_img_filepath, check_img_filepath)
            print ("Checking result : ", check_result)

            isSimilar = "NO"
            if (check_result['similarity'] > 80):
                isSimilar = "YES"
            elif (check_result['similarity'] >= int(check_threshold)):
                isSimilar = "CONFIRM"

            # copy similar images to confirm result
            if (isSimilar != "NO") :
                print ("Find similar image!", check_result)

                if (base_img_filepath not in found_similar_images):
                    found_similar_images.append(base_img_filepath)
                
                if (check_img_filepath not in found_similar_images):
                    found_similar_images.append(check_img_filepath)

                # create similar image output dir if not exist
                similar_out_dir = os.path.join(result_dir, "similar_images",str(group_index))
                if not os.path.exists(similar_out_dir) :
                    os.makedirs(similar_out_dir)
                
                # save similar image copy
                if not os.path.exists(os.path.join(similar_out_dir,os.path.basename(base_img_filepath))):
                    copyfile(base_img_filepath, os.path.join(similar_out_dir,os.path.basename(base_img_filepath)))

                if not os.path.exists(os.path.join(similar_out_dir,os.path.basename(check_img_filepath))):
                    copyfile(check_img_filepath, os.path.join(similar_out_dir,os.path.basename(check_img_filepath)))

            # output result to file
            report_file.write(
                ",".join([
                    str(group_index),
                    check_result['src_img'],
                    check_result['compare_to_img'],
                    str(int(check_result['similarity'])),
                    isSimilar
                ]) + "\n")

    report_file.close

    print ("Completed check. Check {} images in {} seconds".format(file_count, time.time()- start_time))
