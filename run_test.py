import os

from img_check.image_checker import check_images

if __name__ == '__main__':

    check_img_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "data/check_images/"))
    print("check image dir:", check_img_dir)
    base_img_filepath = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "data/base_image.jpg"))
    print("base image:", base_img_filepath)
#    algos = [("hash", "phash"),
#             ("hash", "marrhildrethhash"),
#             ("hash", "averagehash"),
#             ("hash", "colormomenthash"),
#             ("hash", "radialvariancehash"),
#             ("hash", "blockmeanhash0"),
#             ("hash", "blockmeanhash1"),
#             ("feature", "orb")]
    algos = [("feature", "orb"),("hash", "marrhildrethhash")]
    for (mode, algo) in algos:
            print("Algo {}.{}".format(mode, algo))
            check_images(check_img_dir, base_img_filepath, mode, algo)
