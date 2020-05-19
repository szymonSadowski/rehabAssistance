import argparse
import logging
import time

import cv2
import numpy as np

from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh

logger = logging.getLogger('TfPoseEstimator-WebCam')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

fps_time = 0

model = 'mobilenet_thin'
camera = 0

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='tf-pose-estimation realtime webcam')
    parser.add_argument('--camera', type=int, default=0)

    parser.add_argument('--resize', type=str, default='432x368',
                        help='if provided, resize images before they are processed. default=0x0, Recommends : 432x368 or 656x368 or 1312x736 ')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0,
                        help='if provided, resize heatmaps before they are post-processed. default=1.0')

    parser.add_argument('--model', type=str, default='mobilenet_thin',
                        help='cmu / mobilenet_thin / mobilenet_v2_large / mobilenet_v2_small')
    parser.add_argument('--show-process', type=bool, default=False,
                        help='for debug purpose, if enabled, speed for inference is dropped.')

    parser.add_argument('--tensorrt', type=str, default="False",
                        help='for tensorrt process.')

    args = parser.parse_args()
    cap = cv2.VideoCapture(camera)

    ret, cv_img = cap.read()
    w, h = model_wh(args.resize)

    e = TfPoseEstimator(get_graph_path(model), target_size=(w, h))
    while(True):

        ret, cv_img = cap.read()
        humans = e.inference(cv_img, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)

        cv_img = TfPoseEstimator.draw_humans(cv_img, humans, imgcopy=False)
        cv2.imshow('frame',cv_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.relase()
    cv2.destroyAllWindows()