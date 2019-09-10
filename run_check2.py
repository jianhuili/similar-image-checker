# -*- coding:utf-8 -*-

import os
import sys
import getopt

from img_check.similar_image_batch_checker import check_similar_images

def main():
    try :
        opts, args = getopt.getopt(sys.argv[1:], "o:s:", ["output=", "threshold="])  
    
    except  getopt.GetoptError as err: 
        # print help information and exit:
        print (str(err)) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    print ("opts: {}".format(opts))

    image_dir = args[0]
    output = "results"
    threshold = 15
    for key, val in opts:  
        if key in ("-o", "--output"):  
            output = val
        if key in ("-s", "--threshold"):  
            threshold = val
        print (key, val)

    check_similar_images(image_dir, output, threshold)


if __name__ == '__main__':
    main()
    
