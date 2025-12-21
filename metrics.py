import numpy as np
from skimage.metrics import structural_similarity as ssim

def mse(img1, img2):
    return np.mean((img1.astype("float") - img2.astype("float")) ** 2)

def psnr(img1, img2):
    m = mse(img1, img2)
    if m == 0:
        return 100
    return 20 * np.log10(255.0 / np.sqrt(m))

def ssim_wrap(gt, restored):
    return ssim(gt, restored)
