import cv2
import numpy as np
import os

def imread_gray(path):
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)

def imwrite(path, img):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    cv2.imwrite(path, img)

def to_u8(x):
    return np.clip(x, 0, 255).astype(np.uint8)
