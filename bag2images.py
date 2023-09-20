#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2016 Massachusetts Institute of Technology

"""Extract images from a rosbag.
"""

import os
import argparse

import cv2

import rosbag
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge

def main():
    """Extract a folder of images from a rosbag.
    """
    parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
    parser.add_argument("bag_file", help="Input ROS bag.")
    parser.add_argument("output_dir", help="Output directory.")
    parser.add_argument("image_topic", help="Image topic.")

    args = parser.parse_args()

    print ("Extract images from %s on topic %s into %s" % (args.bag_file,
                                                          args.image_topic, args.output_dir))

    bag = rosbag.Bag(args.bag_file, "r")
    bridge = CvBridge()
    count = 0
    save_count = 126
    for topic, msg, t in bag.read_messages(topics=[args.image_topic]):
        if count % 5 ==0:
            cv_img = bridge.compressed_imgmsg_to_cv2(msg, desired_encoding="passthrough")

            cv2.imwrite(os.path.join(args.output_dir, "frame%06i.png" % save_count), cv_img)
            print ("Wrote image %i" % save_count)
            save_count += 1
        
        count += 1

    bag.close()

    return

if __name__ == '__main__':
    main()


# python bag_2_images.py /home/ailab/Downloads/all-deliveryA.bag /home/ailab/wook/bag_deliver /canlab/image_raw/compressed 형태로!