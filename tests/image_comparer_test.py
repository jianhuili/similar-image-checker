# -*- coding:utf-8 -*-
import pytest
import cv2
import os
import time

import img_check.image_comparer as image_comparer

def test_compare_image_with_orb():
    chk_img_filepath = os.path.join(os.path.dirname(__file__),"../data/check_images/same.jpg")
    print(chk_img_filepath)
    base_img_filepath = os.path.join(os.path.dirname(__file__),"../data/base_image.jpg")
    print(base_img_filepath)

    chk_img = cv2.imread(chk_img_filepath)
    base_img = cv2.imread(base_img_filepath)
    stime = time.time()
    result = image_comparer.compare_image_by_feature(chk_img, base_img, "orb")
    print("Comparasion result: {}, {}, {}ms".format("orb", result, (time.time()-stime)*1000))
def test_compare_image_with_phash():
    chk_img_filepath = os.path.join(os.path.dirname(__file__),"../data/check_images/same.jpg")
    print(chk_img_filepath)
    base_img_filepath = os.path.join(os.path.dirname(__file__),"../data/base_image.jpg")
    print(base_img_filepath)
    chk_img = cv2.imread(chk_img_filepath)
    base_img = cv2.imread(base_img_filepath)
    stime = time.time()
    result = image_comparer.compare_image_by_hash(chk_img, base_img, "phash")

    print("Comparasion result: {}, {}, {}ms".format("phash", result, (time.time()-stime)*1000))

def test_compare_image_with_marrhildrethhash():
    chk_img_filepath = os.path.join(os.path.dirname(__file__),"../data/check_images/same.jpg")
    print(chk_img_filepath)
    base_img_filepath = os.path.join(os.path.dirname(__file__),"../data/base_image.jpg")
    print(base_img_filepath)
    chk_img = cv2.imread(chk_img_filepath)
    base_img = cv2.imread(base_img_filepath)
    stime = time.time()
    result = image_comparer.compare_image_by_hash(chk_img, base_img, "marrhildrethhash")

    print("Comparasion result: {}, {}, {}ms".format("marrhildrethhash", result, (time.time()-stime)*1000))

def test_compare_image_with_colormomenthash():
    chk_img_filepath = os.path.join(os.path.dirname(__file__),"../data/check_images/same.jpg")
    print(chk_img_filepath)
    base_img_filepath = os.path.join(os.path.dirname(__file__),"../data/base_image.jpg")
    print(base_img_filepath)
    chk_img = cv2.imread(chk_img_filepath)
    base_img = cv2.imread(base_img_filepath)

    stime = time.time()
    result = image_comparer.compare_image_by_hash(chk_img, base_img, "colormomenthash")

    print("Comparasion result: {}, {}, {}ms".format("colormomenthash", result, (time.time()-stime)*1000))

def test_compare_image_with_radialvariancehash():
    chk_img_filepath = os.path.join(os.path.dirname(__file__),"../data/check_images/same.jpg")
    print(chk_img_filepath)
    base_img_filepath = os.path.join(os.path.dirname(__file__),"../data/base_image.jpg")
    print(base_img_filepath)
    chk_img = cv2.imread(chk_img_filepath)
    base_img = cv2.imread(base_img_filepath)

    stime = time.time()

    result = image_comparer.compare_image_by_hash(chk_img, base_img, "radialvariancehash")

    print("Comparasion result: {}, {}, {}ms".format("radialvariancehash", result, (time.time()-stime)*1000))

def test_compare_image_with_blockmeanhash0():
    chk_img_filepath = os.path.join(os.path.dirname(__file__),"../data/check_images/same.jpg")
    print(chk_img_filepath)
    base_img_filepath = os.path.join(os.path.dirname(__file__),"../data/base_image.jpg")
    print(base_img_filepath)
    chk_img = cv2.imread(chk_img_filepath)
    base_img = cv2.imread(base_img_filepath)

    stime = time.time()

    result = image_comparer.compare_image_by_hash(chk_img, base_img, "blockmeanhash0")

    print("Comparasion result: {}, {}, {}ms".format("blockmeanhash0", result, (time.time()-stime)*1000))

def test_compare_image_with_blockmeanhash1():
    chk_img_filepath = os.path.join(os.path.dirname(__file__),"../data/check_images/same.jpg")
    base_img_filepath = os.path.join(os.path.dirname(__file__),"../data/base_image.jpg")
    chk_img = cv2.imread(chk_img_filepath)
    base_img = cv2.imread(base_img_filepath)

    stime = time.time() 
    result = image_comparer.compare_image_by_hash(chk_img, base_img, "blockmeanhash1")

    print("Comparasion result: {}, {}, {}ms".format("blockmeanhash1", result, (time.time()-stime)*1000))
