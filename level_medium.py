import cv2
import numpy as np
from scipy.signal import wiener as sp_wiener
from skimage.restoration import denoise_nl_means, estimate_sigma
from .common import to_u8

# Baseline Gaussian smoothing
def gaussian_smooth(img, sigma=1.5):
    return cv2.GaussianBlur(img, (0, 0), sigmaX=sigma)

# Adaptive Wiener (SciPy) – for Gaussian noise, no PSF needed
def wiener_filter(img, mysize=5):
    img_f = img.astype(np.float32)
    res = sp_wiener(img_f, mysize=mysize)  # mysize can be int or (m,n)
    return to_u8(res)

# Non-Local Means
def nlm_filter(img):
    sigma_est = np.mean(estimate_sigma(img, channel_axis=None))
    den = denoise_nl_means(img / 255.0,
                           h=1.15 * sigma_est,
                           fast_mode=True,
                           patch_size=5,
                           patch_distance=6,
                           channel_axis=None)
    return to_u8(den * 255)
