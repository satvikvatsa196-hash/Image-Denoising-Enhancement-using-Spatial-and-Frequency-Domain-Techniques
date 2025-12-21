import numpy as np

def add_salt_pepper(img, amount=0.05):
    noisy = img.copy()
    num_salt = int(amount * img.size * 0.5)
    coords = np.random.randint(0, img.size, num_salt)
    noisy.flat[coords] = 255

    num_pepper = int(amount * img.size * 0.5)
    coords = np.random.randint(0, img.size, num_pepper)
    noisy.flat[coords] = 0
    return noisy

def add_gaussian_noise(img, sigma=20):
    noisy = img.astype("float32") + np.random.normal(0, sigma, img.shape)
    return np.clip(noisy, 0, 255).astype("uint8")

from scipy.signal import convolve2d

def motion_psf(length=15, angle=20):
    size = length*2 + 1
    psf = np.zeros((size,size), np.float32)
    center = size // 2

    for i in range(-length, length+1):
        x = int(center + i * np.cos(np.deg2rad(angle)))
        y = int(center + i * np.sin(np.deg2rad(angle)))
        if 0 <= x < size and 0 <= y < size:
            psf[y, x] = 1
    psf /= psf.sum()
    return psf

def apply_motion_blur(img, length=15, angle=20):
    psf = motion_psf(length, angle)
    blurred = convolve2d(img, psf, mode='same', boundary='wrap')
    return np.clip(blurred, 0, 255).astype(np.uint8), psf
