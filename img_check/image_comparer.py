# -*- coding:utf-8 -*-
import cv2
import numpy as np

# 计算汉明距离
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count

def compare_image_by_hash(check_img, base_img, algo="phash") :
    hash_algo = None
    if (algo.lower() == "marrhildrethhash"):
        hash_algo = cv2.img_hash.MarrHildrethHash_create()
    elif (algo.lower() == "averagehash"):
        hash_algo = cv2.img_hash.AverageHash_create()
    elif (algo.lower() == "colormomenthash"):
        hash_algo = cv2.img_hash.ColorMomentHash_create()
    elif (algo.lower() == "radialvariancehash"):
        hash_algo = cv2.img_hash.RadialVarianceHash_create()
    elif (algo.lower() == "blockmeanhash0"):
        hash_algo = cv2.img_hash.BlockMeanHash_create(0)
    elif (algo.lower() == "blockmeanhash1"):
        hash_algo = cv2.img_hash.BlockMeanHash_create(1)
    else : # phash
        hash_algo = cv2.img_hash.PHash_create()

    # # gray image
    # base_img = cv2.cvtColor(base_img,cv2.COLOR_BGR2GRAY)
    # check_img = cv2.cvtColor(check_img,cv2.COLOR_BGR2GRAY)

    base_hash = hash_algo.compute(base_img)
    chk_hash = hash_algo.compute(check_img)

    return hash_algo.compare(base_hash, chk_hash)


def compare_image_by_feature(check_img, base_img, algo="orb") :

    # Sift and Flann
    algo_ins = None
    if (algo.lower() =="sift") :
        algo_ins = cv2.xfeatures2d.SIFT_create()
    elif (algo.lower() =="surf"):
        algo_ins = cv2.xfeatures2d.SURF_create()
    else :
        algo_ins = cv2.ORB_create()
    
    kp_1, desc_1 = algo_ins.detectAndCompute(base_img, None)
    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # 1) Check if 2 images are equals
    if base_img.shape == check_img.shape:
        print("The images have same size and channels")

        difference = cv2.subtract(base_img, check_img)
        b, g, r = cv2.split(difference)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("Similarity: 100% (equal size and channels)")
            return 100

    # 2) Check for similarities between the 2 images
    kp_2, desc_2 = algo_ins.detectAndCompute(check_img, None)

    # convert format
    if (desc_1.dtype != np.float32):
        desc_1 = np.asarray(desc_1, dtype=np.float32)
    
    if (desc_2.dtype != np.float32):
        desc_2 =np.asarray(desc_2, dtype=np.float32)
    
    matches = flann.knnMatch(desc_1, desc_2, k=2)

    good_points = []
    for m, n in matches:
        if m.distance > 0.6*n.distance:
            good_points.append(m)

    number_keypoints = 0
    if len(kp_1) >= len(kp_2):
        number_keypoints = len(kp_1)
    else:
        number_keypoints = len(kp_2)

    percentage_similarity = len(good_points) / number_keypoints * 100
    
    return percentage_similarity

def compare_image_by_orb(check_img, base_img) :
    # gray image
    # base_img = cv2.cvtColor(base_img,cv2.COLOR_BGR2GRAY)
    # check_img = cv2.cvtColor(check_img,cv2.COLOR_BGR2GRAY)

    # Sift and Flann
    algo_ins = cv2.ORB_create()
    
    kp_1, desc_1 = algo_ins.detectAndCompute(base_img, None)
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

    # 1) Check if 2 images are equals
    if base_img.shape == check_img.shape:
        # print("The images have same size and channels")

        difference = cv2.subtract(base_img, check_img)
        b, g, r = cv2.split(difference)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("Similarity: 100% (equal size and channels)")
            return 100.0

    # 2) Check for similarities between the 2 images
    kp_2, desc_2 = algo_ins.detectAndCompute(check_img, None)

    matches = matcher.match(desc_1, desc_2)
    # print ("matches:",matches)

    good_points = []
    for m in matches:
        # print(m.distance)
        if m.distance < 50:
            good_points.append(m)

    number_keypoints = 0
    if len(kp_1) >= len(kp_2):
        number_keypoints = len(kp_1)
    else:
        number_keypoints = len(kp_2)

    percentage_similarity = len(good_points) / number_keypoints * 100
    
    return percentage_similarity
