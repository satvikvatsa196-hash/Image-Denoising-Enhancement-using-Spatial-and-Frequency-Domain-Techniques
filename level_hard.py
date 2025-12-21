import numpy as np
from skimage.restoration import richardson_lucy, unsupervised_wiener
from .common import to_u8
from skimage.filters import unsharp_mask
from src.level_medium import nlm_filter
from skimage import restoration
import cv2

def rl_deblur(noisy_blur, psf, iters=25):
    img = noisy_blur.astype(np.float32) / 255.0
    psf = psf / np.sum(psf)

    rl = richardson_lucy(img, psf, num_iter=iters)
    rl = np.clip(rl, 0, 1)

    from skimage.filters import unsharp_mask
    rl = unsharp_mask(rl, radius=1.2, amount=2.2)
    rl = np.clip(rl, 0, 1)

    return (rl * 255).astype(np.uint8)



from skimage import restoration

def blind_wiener_deblur(noisy_blur, psf, balance=0.005):
    img = noisy_blur.astype(np.float32) / 255.0
    psf = psf / np.sum(psf)

    bw = restoration.wiener(img, psf, balance=balance)
    bw = np.clip(bw, 0, 1)

    #  mild sharpening
    bw = unsharp_mask(bw, radius=1.0, amount=1.5)
    bw = np.clip(bw, 0, 1)

    return (bw * 255).astype(np.uint8)


from skimage.restoration import denoise_nl_means, estimate_sigma

def post_denoise(img):
    img = img.astype(np.float32) / 255.0
    sigma = np.mean(estimate_sigma(img, channel_axis=None))

    nlm = denoise_nl_means(img, h=1.0*sigma, fast_mode=True,
                           patch_size=5, patch_distance=6, channel_axis=None)

    nlm = np.clip(nlm, 0, 1)

    # Re-sharpen after denoise
    final = unsharp_mask(nlm, radius=1.1, amount=2.0)
    final = np.clip(final, 0, 1)

    return (final * 255).astype(np.uint8)


