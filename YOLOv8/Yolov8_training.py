#YoloV8 training

# This file was adapted from Computer vision engineer's Image Segmentation YoloV8 Collection
# Source: https://github.com/computervisioneng/image-segmentation-yolov8
# The original source is licensed under the AGPL-3.0 license.

from ultralytics import YOLO
import torch

# def clear_gpu_memory():
#     torch.cuda.empty_cache()
#     torch.cuda.synchronize()
# checkpoint_path = './runs/segment/train12/weights/last.pt'
#
# Load the model from the checkpoint
# model = YOLO(checkpoint_path)

DATA_DIR = './data/'

model = YOLO('yolov8x-seg.pt')

model.train(data='./config.yaml', epochs=100, imgsz=640, batch=32)

# clear_gpu_memory()

