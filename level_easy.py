import cv2
from .common import to_u8

def median_restore(noisy, k=3):
    return cv2.medianBlur(noisy, k)

def unsharp(img, k=0.6, sigma=1.0):
    blur = cv2.GaussianBlur(img, (0,0), sigma)
    return to_u8(img + k * (img - blur))
